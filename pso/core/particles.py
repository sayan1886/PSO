class Particles:

    def __init__(self):
        self.particles = []
        self.gBest_chromosome = None
        self.gBest = None
        self.gBest_position = None

    def __len__(self):
        return len(self.particles)

    def __iter__(self):
        return self.particles.__iter__()
    
    def __str__(self) -> str:
        gBest = []
        if self.gBest_chromosome is not None:
            for i in range(len(self.gBest_chromosome)):
                gene = ''.join(str(x) for x in self.gBest_chromosome[i])
                gBest.append(gene)
        gBest_str = ''.join(str(x) for x in gBest)
        particles_str = ' '.join(str(x) for x in self.particles)
        return '''
                        {0} 
gBest_chromosome:       {1}
gBest:                  {2}'''.format(
            particles_str, gBest_str, self.gBest) 
        return 

    def extend(self, new_individuals):
        self.particles.extend(new_individuals)

    def append(self, new_individual):
        self.particles.append(new_individual)
        
    def get(self, index):
        return self.particles[index]