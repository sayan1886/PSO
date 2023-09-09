from pso.core.particle import Particle

class Problem:

    def __init__(self, objective, num_of_variables, variables_range, n_chromosome=8,
                 inertia_weight_constant = 0.5, cognitive_coefficient= 0.1,
                 social_coefficient= 0.1, expand=True, same_range=False):
        self.num_of_variables = num_of_variables
        self.objective = objective
        self.expand = expand
        self.variables_range = []
        self.n_chromosome = n_chromosome
        self.n_gene = num_of_variables
        self.inertia_weight_constant = inertia_weight_constant
        self.cognitive_coefficient = cognitive_coefficient
        self.social_coefficient = social_coefficient
        self.chromosome = None
        if same_range:
            for _ in range(num_of_variables):
                self.variables_range.append(variables_range[0])
        else:
            self.variables_range = variables_range

    def generate_particle(self):
        particle = Particle(variables_range=self.variables_range, 
                              n_chromosome=self.n_chromosome, 
                              n_gene=self.n_gene, 
                              inertia_weight_constant=self.inertia_weight_constant,
                              cognitive_coefficient=self.cognitive_coefficient,
                              social_coefficient=self.social_coefficient)
        return particle

    def calculate_objective(self, particle):
        if self.expand:
            particle.objective = self.objective
        else:
            particle.objective = self.objective