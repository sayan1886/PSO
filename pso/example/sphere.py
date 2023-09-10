import sys
from pathlib import Path

import numpy as np
# import matplotlib.pyplot as plt

from pso.example.config import config
from pso.core.evolution import Evolution
from pso.core.problem import Problem
from pso.plot.plot import PSOContourPlot as Plot

# benchmark problem on spehre
# Sphere => f(x) = sumation ( {i=1  to p} x_i^2 )
# x_i in [-5.12, 5.12]				
# x^* = (0,0,...,0); f(x^*) = 0
def f1(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i] ** 2
    return sum
    
def f2(x, y):
    return (x-3.14)**2 + (y-2.72)**2 + np.sin(3*x+1.41) + np.sin(4*y-1.73)

if __name__ == "__main__":
    executing_file_path = sys.argv[0]
    example_name = Path(executing_file_path).stem
    configs = config.get_config(example_name)
    print(configs)
    
    problem = Problem(objective=f1, objective_type=configs.objective.objective_type,
                      num_of_variables=configs.num_of_gene, 
                      variables_range=[(configs.range.min, configs.range.max)],
                      expand=configs.objective.expand, 
                      same_range=configs.range.variable_range, 
                      n_chromosome=configs.num_of_chromosomes,
                      inertia_weight_constant=configs.inertia_weight_constant,
                      cognitive_coefficient=configs.cognitive_coefficient,
                      social_coefficient=configs.social_coefficient)
    
    evo = Evolution(problem=problem, 
                    num_of_iterations=configs.num_of_iterations, 
                    num_of_particles=configs.num_of_particles)
    
    
    gBests = evo.evolve()
    
    plot = Plot(objective=f1)
    plot.plot(gBests)
