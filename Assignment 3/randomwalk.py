import random
import matplotlib.pyplot as plt
import numpy as np
import time
from scipy.stats import norm  # For Gaussian distribution

# Parameters
noOfWalkers = 10000  # Number of walkers
steps = 1000  # Only calculating MSD for 1000 steps

def randomWalker(finalPositions, steps):

    # Simulate multiple random walks
    msdValues = np.zeros(steps + 1)  # To store Mean Square Displacement at each step

    for _ in range(noOfWalkers):
        position = 0  # Start at x = 0

        # Perform random walk
        for t in range(1, steps + 1):  
            position += random.choice([-1, 1])  # Move left (-1) or right (+1), there is an equal chance
            msdValues[t] += position ** 2  # Sum squared displacement, can use position since initial position is 0
        
        finalPositions.append(position)  # Store final position
    
    return msdValues / noOfWalkers  # Compute average MSD

# Time frames for histogram
stepList = [100, 500, 1000]
msdValues = None  # Store MSD for 1000 steps 

# Run simulations and plot histograms
for step in stepList:
    finalPositions = []  # Store where each walker ends up
    start_time = time.time()
    
    # Calculate MSD only for 1000 steps
    if step == 1000:
        msdValues = randomWalker(finalPositions, step)
    else:
        randomWalker(finalPositions, step)
    
    # Plot histogram (probability distribution)
    plt.figure(figsize=(8, 5))
    plt.hist(finalPositions, bins=50, density=True, alpha=0.7, color="blue", edgecolor="black")

    # Overlay theoretical Gaussian distribution
    mu, sigma = 0, np.sqrt(step)
    x = np.linspace(min(finalPositions), max(finalPositions), 1000)
    plt.plot(x, norm.pdf(x, mu, sigma), 'r-', linewidth=2, label="Theoretical Gaussian")

    # Labels and title
    plt.xlabel("Final Position")
    plt.ylabel("Probability Density")
    plt.title(f"Probability Distribution of 1D Random Walk (Steps = {step})")
    plt.legend()
    plt.grid()
    plt.show()
    
    end_time = time.time()
    print(f"Plot loaded in {end_time - start_time:.2f} seconds.")

# Plot MSD for 1000 steps
if msdValues is not None:
    plt.figure(figsize=(8, 5))
    plt.plot(range(len(msdValues)), msdValues, label="Simulated MSD", color="blue")

    # Expected MSD relation (MSD ≈ steps)
    t_values = np.arange(0, steps + 1)
    plt.plot(t_values, t_values, 'k--', label="Theoretical MSD (MSD = steps)")

    # Labels and title
    plt.xlabel("Time Steps")
    plt.ylabel("Mean Square Displacement (MSD)")
    plt.title("Mean Square Displacement vs. Time (1000 Steps)")
    plt.legend()
    plt.grid()
    plt.show()
