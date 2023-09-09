import random

class Particle(object):

    def __init__(self, variables_range, n_chromosome=8, n_gene=1, chromosome = None,
                 inertia_weight_constant = 0.5, cognitive_coefficient= 0.1,
                 social_coefficient= 0.1):
        self.variables_range = variables_range
        self.n_chromosome = n_chromosome
        self.n_gene = n_gene
        self.inertia_weight_constant = inertia_weight_constant
        self.cognitive_coefficient = cognitive_coefficient
        self.social_coefficient = social_coefficient
        self.pBest = None
        self.velocity = None
        self.position = None
        self.objective = None
        if chromosome is None:
            chromosome = self.__generate_random_chromosome()
        self.chromosome = chromosome.copy()
        

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.features() == other.features()
        return False
    
     # genarate a randome chromosome with number of gene
    def __generate_random_chromosome(self):
        chromosome = [0] * self.n_gene
        for i in range(self.n_gene):
            chromosome[i] = self.__generate_random_gene().copy()
        return chromosome
    
    # genarate a randome gene main unit of chromosome
    def __generate_random_gene(self):
        gene = [0] * self.n_chromosome
        for i in range(self.n_chromosome):
            gene[i] = random.randint(0,1)
        return gene
    
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
    
    def features(self):
        return self.__corresponding_value()