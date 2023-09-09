import random

from pso.core.particles import Particles

class PSOUtils:

    def __init__(self, problem, num_of_particles=100):

        self.problem = problem
        self.num_of_particles = num_of_particles

    def create_initial_particles(self):
        particles = Particles()
        for _ in range(self.num_of_particles):
            individual = self.problem.generate_particle()
            self.problem.calculate_objective(individual)
            particles.append(individual)
        return particles