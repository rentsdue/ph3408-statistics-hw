# Write a code to simulate a 1-dimensional random walk of a particle on a grid. Start
# from x = 0. In each step, the point has an equal probability to jump to the left or
# right. Repeat multiple times and plot how the probability distribution of the particle
# position change with time (you only need to show three different time points)

# Python code for 1D Random Walk
import random
import numpy as np
import matplotlib.pyplot as plt

# Probability to move left or right (the same)
probLeft = probRight = 0.5

# statically defining the starting position
start = 0
positions = [start]

for _ in range(1000):
    move = random.choices(["left", "right"], weights=[probLeft, probRight])[0]
    
    if move == "left" and positions[-1] > 1:
        positions.append(positions[-1] - 1)  # Move left
    elif move == "right" and positions[-1] < 4:
        positions.append(positions[-1] + 1)  # Move right
    else:
        positions.append(positions[-1])  # Stay in place if at boundary

# Plot the results
plt.plot(positions)
plt.xlabel("Step")
plt.ylabel("Position")
plt.title("1D Random Walk (Left & Right)")
plt.show()