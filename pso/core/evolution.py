from tqdm import tqdm

from pso.core.utils import PSOUtils
from pso.core.particles import Particles
from pso.core.particle import Particle

class Evolution:

    def __init__(self, problem, num_of_iterations=50, num_of_particles=20):
        self.utils = PSOUtils(problem=problem, 
                            num_of_particles=num_of_particles)
        self.particles: Particles = None
        self.num_of_iterations = num_of_iterations
        self.num_of_particles = num_of_particles

    def evolve(self):
        self.particles = self.utils.create_initial_particles()
        for i in tqdm(range(self.num_of_iterations)):
            for j in range(self.num_of_particles):
                particle:Particle = self.particles.get(index=j)
                self.utils.problem.evaluate_pBest(particle=particle)
            self.utils.problem.evaluate_gBest(self.particles)
            self.utils.update_position(particles=self.particles, 
                                       gBest=self.utils.problem.gBest_chromosome)
        
        print(self.utils.problem.gBest)