import sys
from pathlib import Path

import numpy as np
# import matplotlib.pyplot as plt

from pso.example.config import config
from pso.core.evolution import Evolution
from pso.core.problem import Problem

# benchmark problem on spehre
# Sphere => f(x) = sumation ( {i=1  to p} x_i^2 )
# x_i in [-5.12, 5.12]				
# x^* = (0,0,...,0); f(x^*) = 0
def f1(x):
    return np.sum(x ** 2)

if __name__ == "__main__":
    executing_file_path = sys.argv[0]
    example_name = Path(executing_file_path).stem
    configs = config.get_config(example_name)
    print(configs)
    
    problem = Problem(objective=f1, 
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
    
    evol = evo.evolve()
    # func = [i.objectives for i in evol]

    # function1 = [i[0] for i in func]
    # function2 = [i[1] for i in func]
    # plt.title("MOO Benchmark Problem SCH")
    # plt.xlabel('Function 1', fontsize=15)
    # plt.ylabel('Function 2', fontsize=15)
    # plt.scatter(function1, function2)
    # plt.show()
