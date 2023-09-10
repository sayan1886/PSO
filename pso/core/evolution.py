from tqdm import tqdm

from pso.core.utils import PSOUtils
from pso.core.particles import Particles
from pso.core.particle import Particle

# https://slideplayer.com/slide/5167619/
# https://ieeexplore.ieee.org/document/4433821
class Evolution:

    def __init__(self, problem, num_of_iterations=50, num_of_particles=20):
        self.utils = PSOUtils(problem=problem, 
                            num_of_particles=num_of_particles)
        self.particles: Particles = None
        self.num_of_iterations = num_of_iterations
        self.num_of_particles = num_of_particles
        self.gBests = []
        self.gBests_position = []

    def evolve(self):
        self.particles = self.utils.create_initial_particles()
        for _ in tqdm(range(self.num_of_iterations)):
            # print('''\n\n**iteration: {0}**
# particles:    {1}'''.format(i, self.particles))
            for j in range(self.num_of_particles):
                particle:Particle = self.particles.get(index=j)
                self.utils.problem.calculate_objective(particle=particle)
                self.utils.problem.evaluate_pBest(particle=particle)
            self.utils.problem.evaluate_gBest(self.particles)
            self.gBests.append(self.particles.gBest)
            self.gBests_position.append(self.particles.gBest_position)
            self.utils.update_position(particles=self.particles, 
                                       gBest=self.particles.gBest_chromosome)
        
        print(self.particles.gBest)
        pBest = []
        pBest_position = []
        for i in range(self.num_of_particles):
            particle:Particle = self.particles.get(index=i)
            pBest.append(particle.pBest)
            pBest_position.append(particle.position())
        return self.gBests, self.gBests_position, pBest, pBest_position