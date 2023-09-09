from tqdm import tqdm

from pso.core.utils import PSOUtils
from pso.core.particles import Particles

class Evolution:

    def __init__(self, problem, num_of_iterations=100, num_of_particles=20):
        self.utils = PSOUtils(problem=problem, 
                            num_of_particles=num_of_particles)
        self.particles = None
        self.num_of_iterations = num_of_iterations
        self.num_of_particles = num_of_particles

    def evolve(self):
        self.particles = self.utils.create_initial_particles()
        
        for i in tqdm(range(self.num_of_iterations)):
            print(i)