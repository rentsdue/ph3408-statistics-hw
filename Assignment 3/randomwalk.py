import random
import matplotlib.pyplot as plt

# Parameters
noOfWalkers = 10000  # Number of walkers (more = smoother distribution)
steps = 1000  # Total steps each walker takes

# Simulate multiple random walks
finalPositions = []  # Store where each walker ends up

for _ in range(noOfWalkers):
    position = 0  # Start at x = 0
    for _ in range(steps):  # Perform random walk
        position += random.choice([-1, 1])  # Move left (-1) or right (+1), equal probability
    finalPositions.append(position)  # Store final position

# Plot histogram (probability distribution)
plt.figure(figsize=(8, 5))
plt.hist(finalPositions, bins=30, density=True, alpha=0.7, color="blue", edgecolor="black")

# Labels and title
plt.xlabel("Final Position")
plt.ylabel("Probability Density")
plt.title(f"Probability Distribution of 1D Random Walk (Steps = {steps})")
plt.grid()
plt.show()
