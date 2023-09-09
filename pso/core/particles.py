class Particles:

    def __init__(self):
        self.particles = []
        self.fronts = []

    def __len__(self):
        return len(self.particles)

    def __iter__(self):
        return self.particles.__iter__()

    def extend(self, new_individuals):
        self.particles.extend(new_individuals)

    def append(self, new_individual):
        self.particles.append(new_individual)