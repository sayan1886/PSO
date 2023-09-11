import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# https://machinelearningmastery.com/visualization-for-function-optimization-in-python/
# https://machinelearningmastery.com/a-gentle-introduction-to-particle-swarm-optimization/
class PSOContourPlot():
    
    def __init__(self, objective, num_of_iterations, num_of_variable, 
                 expandable, range_min, range_max):
        self.objective = objective
        self.num_of_iterations = num_of_iterations
        self.num_of_variable = num_of_variable
        self.expandable = expandable
        self.range_min = range_min
        self.range_max = range_max
        
    def plot(self, gBests):
        plt.plot(gBests, label="best")
        plt.title("Binary PSO Benchmark Sphere")
        plt.ylabel('Fitness')
        plt.xlabel('Generations')
        plt.legend(['Best Fitness'], loc='best')
        plt.show()
        
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
        
    def get_contour_base(self, particles_pos, velocity, 
                          gBest, gBest_pos, pBest, pBest_pos):
        inputs = np.linspace(self.range_min, self.range_max, 100)
        x, y = np.meshgrid(inputs, inputs)
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
            
        pos_x = []
        pos_y = []    
        for i in range(len(particles_pos)):
            pos_x.append(particles_pos[i][0])
            pos_y.append(particles_pos[i][1])
            
        v_x = []
        v_y = []    
        for i in range(len(velocity)):
            v_x.append(velocity[i][0])
            v_y.append(velocity[i][1])
            
        # Set up base figure: The contour map
        fig, ax = plt.subplots(figsize=(8,6))
        fig.set_tight_layout(True)
        img = ax.imshow(results, extent=[self.range_min, self.range_max, 
                        self.range_min, self.range_max], origin='lower', 
                        cmap='viridis', alpha=0.5)
        fig.colorbar(img, ax=ax)
        ax.plot([x_min], [y_min], marker='x', markersize=5, color="white")
        contours = ax.contour(x, y, results, 10, colors='black', alpha=0.4)
        ax.clabel(contours, inline=True, fontsize=8, fmt="%.0f")
        pbest_plot = ax.scatter(pBest_x, pBest_y, marker='o', 
                                color='black', alpha=0.5)
        p_plot = ax.scatter(pos_x, pos_y, marker='o', color='blue', alpha=0.5)
        # p_arrow = ax.quiver(pos_x, pos_y, v_x, v_y, color='blue', width=0.005, 
                            # angles='xy', scale_units='xy', scale=1)
        gbest_plot = plt.scatter(gBest_x, gBest_y, marker='*', s=100, 
                                 color='red', alpha=0.4)
        ax.set_xlim([self.range_min, self.range_max])
        ax.set_ylim([self.range_min, self.range_max])
        return ax, fig, v_x, v_y, pbest_plot, p_plot, None, gbest_plot
    
    def animate(frame, ax, v_x, v_y, pBest, pbest_plot, p_plot, p_arrow,
                gBest, gbest_plot):
        "Steps of PSO: algorithm update and show in plot"
        title = 'Iteration {:02d}'.format(frame)
        # Set picture
        ax.set_title(title)
        pbest_plot.set_offsets(pBest.T)
        p_plot.set_offsets(pBest.T)
        p_arrow.set_offsets(pBest.T)
        # p_arrow.set_UVC(v_x, v_y)
        gbest_plot.set_offsets(gBest.reshape(1,-1))
        return ax, pbest_plot, p_plot, p_arrow, gbest_plot
    
    def startAnimate(self, fig, ax, v_x, v_y, 
                pBest, pbest_plot, p_plot, p_arrow,
                gBest, gbest_plot):
        ani = self.animate
        _ = FuncAnimation(fig, ani, frames=list(range(1,self.num_of_iterations)), 
                             interval=500, blit=False, repeat=True,
                             fargs=(ax, v_x, v_y, pBest, pbest_plot, 
                                    p_plot, p_arrow, gBest, gbest_plot))
        # anim.save("PSO.gif", dpi=120, writer="imagemagick")
        plt.show()