import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Random walk function that adds either 1 or -1 to each element in the initial array
def iterate(positions):
    step = np.random.choice([-1, 1], size=len(positions))
    return positions + step

N = 1000
num_iterations = 200
num_steps = 1
initial_coordinates = np.zeros(N)

plt.figure(figsize=(10, 6))

start_color = np.array([1, 0, 0])
end_color = np.array([0, 0, 1])

bin_width = 2
min_position, max_position = -num_steps * num_iterations / 6, num_steps * num_iterations / 6

average_positions = []
variances = []
standard_deviations = []

# Iterative calculation of standard deviation, variance, and average position
for i in range(num_iterations):
    print(f"Iteration {i}")
    for _ in range(num_steps):
        initial_coordinates = iterate(initial_coordinates)
    
    avg_position = np.mean(initial_coordinates)
    variance = np.var(initial_coordinates)
    std_deviation = np.std(initial_coordinates)
    
    average_positions.append(avg_position)
    variances.append(variance)
    standard_deviations.append(std_deviation)

    # Interpolation calculation for graph color change
    interpolation_factor = i / (num_iterations - 1)
    color = start_color * (1 - interpolation_factor) + end_color * interpolation_factor
    
    plt.hist(initial_coordinates, bins=np.arange(min_position, max_position + bin_width, bin_width), 
             alpha=0.5, color=color, label=f"{i * num_steps} steps" if i == 0 else "")

plt.title(f"Histograms of Final Positions of {N} Particles after Random Walks")
plt.xlabel("Final Position")
plt.ylabel("Number of Particles")
plt.grid(True)
plt.savefig("random_walk_hist.png")
plt.close()  

plt.figure(figsize=(10, 6))
plt.plot(range(num_iterations), average_positions, label="Average Position", color='blue')
plt.plot(range(num_iterations), variances, label="Variance", color='red')
plt.plot(range(num_iterations), standard_deviations, label="Standard Deviation", color='green')

plt.xlabel("Number of Iterations")
plt.ylabel("Value")
plt.title(f"Statistics of {N} Particles Over {num_iterations} Iterations")
plt.legend()
plt.grid(True)
plt.savefig("random_walk_stats.png")  
plt.close() 
