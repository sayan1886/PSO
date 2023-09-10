import matplotlib.pyplot as plt
import numpy as np

class PSOContourPlot():
    
    def __init__(self, objective) -> None:
        self.objective = objective
        
    def plot_contour(self, gBest):
        # Contour plot: With the global minimum showed as "X" on the plot
        x, y = np.array(np.meshgrid(np.linspace(0,5,100), np.linspace(0,5,100)))
        obj = []
        for i in range(len(x)):
            obj.append([self.objective(x[i]), self.objective(y[i])])
        z = np.array(obj)
        x_min = x.ravel()[z.argmin()]
        y_min = y.ravel()[z.argmin()]
        plt.figure(figsize=(8,6))
        plt.imshow(z, extent=[0, 5, 0, 5], origin='lower', cmap='viridis', alpha=0.5)
        plt.colorbar()
        plt.plot([x_min], [y_min], marker='x', markersize=5, color="white")
        contours = plt.contour(x, y, z, 10, colors='black', alpha=0.4)
        plt.clabel(contours, inline=True, fontsize=8, fmt="%.0f")
        plt.show()

    def plot(self, gBests):
        plt.plot(gBests, label="best")
        plt.title("Binary PSO Benchmark Sphere")
        plt.ylabel('Fitness')
        plt.xlabel('Generations')
        plt.legend(['Best Fitness'], loc='best')
        plt.show()