import numpy as np

class Particle(object):

    def __init__(self, variables_range, n_chromosome=8, n_gene=1):
        self.variables_range = variables_range
        self.n_chromosome = n_chromosome
        self.n_gene = n_gene
        self.pBest = None
        self.pBest_chromosome = None
        self.objective = None
        self.velocity_min = 0.1
        self.velocity_max = 0.9
        self.chromosome, self.velocity = self.__generate_random_chromosome()
        

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.position() == other.position()
        return False
    
    def __str__(self):
        chromosome = []
        for i in range(self.n_gene):
            gene = ''.join(str(x) for x in self.chromosome[i])
            chromosome.append(gene)
        chromosome_str = ''.join(str(x) for x in chromosome)
        
        velocity = []
        for i in range(self.n_gene):
            gene = ','.join(str(x) for x in self.velocity[i])
            velocity.append(gene)
        velocity_str = ','.join(str(x) for x in velocity)
        
        pBest = []
        if self.pBest_chromosome is not None:
            for i in range(self.n_gene):
                gene = ''.join(str(x) for x in self.pBest_chromosome[i])
                pBest.append(gene)
        pBest_str = ''.join(str(x) for x in pBest)
        
        return '''
chromosome:             {0} 
Velocity:               {1}
pBest_chromosome:       {2}
pBest:                  {3}'''.format(
            chromosome_str, velocity_str, pBest_str, self.pBest) 
    
     # genarate a randome chromosome with number of gene
    def __generate_random_chromosome(self):
        chromosome = [0] * self.n_gene
        velocity = [0] * self.n_gene
        for i in range(self.n_gene):
            chromosome[i], velocity[i] = self.__generate_random_gene()
        return chromosome, velocity
    
    # genarate a randome gene main unit of chromosome
    def __generate_random_gene(self):
        gene = [0] * self.n_chromosome
        velocity_gene = [0] * self.n_chromosome
        for i in range(self.n_chromosome):
            gene[i] = np.random.randint(0,1)
            # v_id = v_min + (v_max - v_min) * rand()
            velocity_gene[i] = self.velocity_min + \
                (self.velocity_max - self.velocity_min) * \
                    np.random.uniform(0, 1)
        return gene.copy(), velocity_gene.copy()
    
    # encode chromosome will return array of integer 
    # where each integer denote a enocded gene
    def __encode_chromosome(self):
        # array of integer represent encoded genes 
        # converted from binary string array or gene
        encoded_chromosome = [0] * self.n_gene
        for i in range(self.n_gene):
            encoded_chromosome[i] = self.__encode_gene(self.chromosome[i])
        return encoded_chromosome
    
    # encode gene(binary string array) to integer value
    def __encode_gene(self, gene):
        # convert binary list to string
        binary_string = ''.join(map(str, gene))
        # convert binary string to integer
        encoded_gene = int(binary_string, 2) 
        return encoded_gene
    
    # evaluate corresponding chormosome value 
    def __corresponding_value(self):
        # array of integer represent encoded genes
        encoded_chromosome = self.__encode_chromosome()
        corresponding_value = [0] * self.n_gene
        for i in range(self.n_gene):
            corresponding_value[i] = self.__corresponding_gene_value(
                                        encoded_chromosome[i])
        return corresponding_value
    
    # calcualate corresponfing gene value using interpolation
    # where y_min = config.bounday.min y_max = config.bounday.min
    # x_max = 2^chormosomeLength - 1 and x_min = 0
    # x will encoded gene value
    # y = y_min + (y_max - y_min) / (x_max - x_min) * (x - x_min)
    def __corresponding_gene_value(self, encoded_gene):
        # y = self.__get_y()
        y_min = self.variables_range[0][0]
        y_max = self.variables_range[0][1]
        corresponding_value = (y_min + 
                        ((y_max - y_min) / 
                        (2 ** self.n_chromosome - 1) - 0) * 
                        (encoded_gene - 0))
        return corresponding_value
    
    # TODO: need to add variable range y 
    def __get_y(self, gene_index):
        y = self.variables_range[0]
        if(len(self.variables_range)) > 1:
            y = self.variables_range[gene_index] 
        return y
    
    def position(self):
        return self.__corresponding_value()
    
    def update_position_velocity(self, gBest_chromosome):
        for i in range(self.n_gene):
            for j in range(self.n_chromosome):
                self.chromosome[i][j], self.velocity[i][j] = \
                        self.update_bit_position_velocity(
                            bit_pos=self.chromosome[i][j], 
                            bit_velocity=self.velocity[i][j],
                            pBest_bit=self.pBest_chromosome[i][j],
                            gBest_bit=gBest_chromosome[i][j])
    
    # f(v_id(t)) = 1 / (1 + e ** -v_id(t))
    # v_id(t) = v_id(t -1) + U_1 * (p_id - x_id(t - 1)) + U_2 * (p_gd - x_id(t - 1))
    # where U_1 and U_2 random number between 0 and 3 and some U_1 + U_2 < 4.0
    # id is the best solution found for the individual
    # gd is the best solution found for the swarm
    # we might consider a range of v_min and v_max so that f(v_id(t)) does not 
    # approach too closely to 0 or 1
    # we might need correct v_id value to the range
    # now we will chose a random number between 0 & 1 and compare with f(v_id(t))
    # x_ij(t + 1) = 1 if r_ij < sig(v_ij (t + 1))  otherwise 0
    def update_bit_position_velocity(self, bit_pos, bit_velocity, 
                                     pBest_bit, gBest_bit):
        u1 = np.random.uniform(0, 3)
        u2 = np.random.uniform(0, 3)
        while u1 + u2 >= 4.0:
            u1 = np.random.uniform(0, 3)
            u2 = np.random.uniform(0, 3)
            
        bit_velocity_next = bit_velocity  + u1 * (pBest_bit - bit_pos) \
            + u2 * (gBest_bit - bit_pos)
        sigmoid_v_bit = (1 / (1 + np.exp(-bit_velocity_next)))
        
        if bit_velocity_next < self.velocity_min:
            bit_velocity_next = self.velocity_min
        elif bit_velocity_next > self.velocity_max:
            bit_velocity_next = self.velocity_max
            
        bit_position_next = 0
        r = np.random.uniform(0, 1)
        if r < sigmoid_v_bit:
            bit_position_next = 1
        return bit_position_next, bit_velocity_next