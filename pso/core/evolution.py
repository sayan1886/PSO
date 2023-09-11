from tqdm import tqdm

from pso.core.utils import PSOUtils
from pso.core.particles import Particles
from pso.core.particle import Particle
# from pso.plot.plot import PSOContourPlot

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
        # plot = PSOContourPlot(objective=self.utils.problem.objective,
        #                       num_of_iterations=self.num_of_iterations,
        #                       num_of_variable=self.utils.problem.num_of_variables, 
        #                       expandable=self.utils.problem.expand,
        #                       range_min=self.utils.problem.variables_range[0][0],
        #                       range_max=self.utils.problem.variables_range[0][1])
        
        for _ in tqdm(range(self.num_of_iterations)):
            # print('''\n\n**iteration: {0}**
# particles:    {1}'''.format(i, self.particles))
            pBest = []
            pBest_position = []
            particle_position = []
            velocity = []
            for j in range(self.num_of_particles):
                particle:Particle = self.particles.get(index=j)
                self.utils.problem.calculate_objective(particle=particle)
                self.utils.problem.evaluate_pBest(particle=particle)
                pBest.append(particle.pBest)
                pBest_position.append(particle.position())
                particle_position.append(particle.position())
                velocity.append(particle.velocity)
                
            self.utils.problem.evaluate_gBest(self.particles)
            self.gBests.append(self.particles.gBest)
            self.gBests_position.append(self.particles.gBest_position)
            self.utils.update_position_velocity(particles=self.particles, 
                                       gBest=self.particles.gBest_chromosome)
            # ax, fig, v_x, v_y, pbest_plot, p_plot, p_arrow, gbest_plot = \
            #     plot.get_contour_base(particles_pos=particle_position, 
            #                         velocity=velocity,
            #                         gBest=self.gBests,
            #                         gBest_pos=self.gBests_position,
            #                         pBest=pBest, pBest_pos=pBest_position)
            # plot.startAnimate(fig=fig, ax=ax, v_x=v_x, v_y=v_y, 
            #         pBest=pBest, pbest_plot=pbest_plot, p_plot=p_plot, 
            #         p_arrow=p_arrow, gbest_plot=gbest_plot, gBest=self.gBests)
        
        print(self.particles.gBest)
        pBest = []
        pBest_position = []
        for i in range(self.num_of_particles):
            particle:Particle = self.particles.get(index=i)
            
        return self.gBests, self.gBests_position, pBest, pBest_position