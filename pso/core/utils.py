from pso.core.particles import Particles
from pso.core.particle import Particle
from pso.core.problem import Problem

class PSOUtils:

    def __init__(self, problem:Problem = None, num_of_particles=100):
        self.problem = problem
        self.num_of_particles = num_of_particles

    def create_initial_particles(self) -> Particles:
        particles = Particles()
        for _ in range(self.num_of_particles):
            particle = self.problem.generate_particle()
            self.problem.calculate_objective(particle=particle)
            particles.append(particle)
        return particles
    
    def update_position_velocity(self, particles:Particles, gBest):
        for i in range(len(particles)):
            particle:Particle = particles.get(index=i)
            particle.update_position_velocity(gBest)