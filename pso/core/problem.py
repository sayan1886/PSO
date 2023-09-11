from pso.core.particle import Particle
from pso.core.particles import Particles

# https://slideplayer.com/slide/5167619/
class Problem:

    def __init__(self, objective, num_of_variables, variables_range, 
                 objective_type="min", n_chromosome=8,
                 expand=True, same_range=False):
        self.num_of_variables = num_of_variables
        self.objective = objective
        self.objective_type = objective_type
        self.expand = expand
        self.variables_range = []
        self.n_chromosome = n_chromosome
        self.n_gene = num_of_variables

        if same_range:
            for _ in range(num_of_variables):
                self.variables_range.append(variables_range[0])
        else:
            self.variables_range = variables_range

    def generate_particle(self):
        particle = Particle(variables_range=self.variables_range, 
                              n_chromosome=self.n_chromosome, 
                              n_gene=self.n_gene)
        return particle

    def calculate_objective(self, particle:Particle):
        if self.expand:
            particle.objective = self.objective(*particle.position())
        else:
            particle.objective = self.objective(particle.position())
            
    def evaluate_pBest(self, particle:Particle):
        if self.objective_type == "min":
            if (particle.pBest is None or 
                particle.objective <= particle.pBest): 
                particle.pBest = particle.objective
                particle.pBest_chromosome = particle.chromosome
        else:
            if (particle.pBest is None or 
                particle.objective >= particle.pBest): 
                particle.pBest = particle.objective
                particle.pBest_chromosome = particle.chromosome
                
    def evaluate_gBest(self, particles:Particles):
        if self.objective_type == "min":
            soted_particles = sorted(particles, key=lambda particle: 
                particle.pBest, reverse=False)
            pBest_min_particle:Particle = soted_particles[0]
            pBest_min = pBest_min_particle.objective
            if (particles.gBest is None or 
                pBest_min <= particles.gBest):
                particles.gBest = pBest_min
                particles.gBest_position = pBest_min_particle.position()
                particles.gBest_chromosome = pBest_min_particle.chromosome
        else:
            soted_particles = sorted(particles, key=lambda x: x.pBest, reverse=True)
            pBest_max_particle:Particle = soted_particles[0]
            pBest_max = pBest_max_particle.objective
            if (particles.gBest is None or 
                pBest_max >= particles.gBest):
                particles.gBest = pBest_max
                particles.gBest_position = pBest_max_particle.position()
                particles.gBest_chromosome = pBest_max_particle.chromosome
        
    