import matplotlib.pyplot as plt
import numpy as np

# https://machinelearningmastery.com/visualization-for-function-optimization-in-python/
# https://machinelearningmastery.com/a-gentle-introduction-to-particle-swarm-optimization/
class PSOContourPlot():
    
    def __init__(self, objective, num_of_variable, expandable, 
                 range_min, range_max):
        self.objective = objective
        self.num_of_variable = num_of_variable
        self.expandable = expandable
        self.range_min = range_min
        self.range_max = range_max
        
    def plot_scatter(self):
        # sample input range uniformly at 0.1 increments
        inputs = np.arange(self.range_min, self.range_max, 0.1)
        # compute targets
        results = []
        for i in range(len(inputs)):
            # copy same elememt into each column
            input = [inputs[i]] * self.num_of_variable
            obj = None
            if self.expandable:
                obj = self.objective(*input)
            else:
                obj = self.objective(input)
            results.append(obj)
        # simulate a sample made by an optimization algorithm
        np.random.seed(1)
        sample = self.range_min + np.random.rand(10) * (self.range_max - self.range_min)
        # evaluate the sample
        sample_eval = []
        for i in range(len(sample)):
            # copy same elememt into each column
            sample_input = [sample[i]] * self.num_of_variable
            obj = None
            if self.expandable:
                obj = self.objective(*sample_input)
            else:
                obj = self.objective(sample_input)
            sample_eval.append(obj)
        # create a line plot of input vs result
        plt.plot(inputs, results)
        # # define the known function optima
        # optima_x = 0.0
        # # draw a vertical line at the optimal input
        # plt.axvline(x=optima_x, ls='--', color='red')
        # plot the sample as black circles
        plt.plot(sample, sample_eval, 'o', color='black')
        # show the plot
        plt.show()
        
    def plot_contour(self, gBest, gBest_pos, pBest, pBest_pos):
        # sample input range uniformly at 0.1 increments
        inputs = np.linspace(self.range_min, self.range_max, 100)
        x, y = np.meshgrid(inputs, inputs)
        # compute targets
        results = []
        for i in range(len(x)):
            input = [x[i], y[i]]
            obj = None
            if self.expandable:
                obj = self.objective(*input)
            else:
                obj = self.objective(input)
            results.append(obj)
        results = np.array(results)

        x_min = x.ravel()[results.argmin()]
        y_min = y.ravel()[results.argmin()]
        
        gBest_x = []
        gBest_y = []
        for i in range(len(gBest)):
            gBest_x.append(gBest_pos[i][0])
            gBest_y.append(gBest_pos[i][1])
            
        pBest_x = []
        pBest_y = []
        for i in range(len(pBest)):
            pBest_x.append(pBest_pos[i][0])
            pBest_y.append(pBest_pos[i][1])
            
        plt.figure(figsize=(10,8))
        plt.imshow(results,
                   extent=[self.range_min, self.range_max, self.range_min, 
                            self.range_max], origin='lower', cmap='viridis', 
                   alpha=0.5)
        plt.colorbar()
        plt.plot([x_min], [y_min], marker='x', markersize=5, color="white")
        contours = plt.contour(x, y, results, 10, colors='black', alpha=0.4)
        plt.clabel(contours, inline=True, fontsize=8, fmt="%.0f")
        # plot gBest
        plt.scatter(gBest_x, gBest_y, gBest, marker='o', 
                    color='red', alpha=0.5)
        # plt pBest
        plt.scatter(pBest_x, pBest_y, pBest, marker='o', 
                    color='blue', alpha=0.5)
        # plt.legend(['gBest', 'pBest'], loc='best')
        # show the plot
        plt.show()
        
    def plot(self, gBests):
        plt.plot(gBests, label="best")
        plt.title("Binary PSO Benchmark Sphere")
        plt.ylabel('Fitness')
        plt.xlabel('Generations')
        plt.legend(['Best Fitness'], loc='best')
        plt.show()