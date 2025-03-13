import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Define fixed large square size
squareLength = 10  # Side length of large square
noOfTrials = 1000  # Number of repetitions per setup

# Define varying parameters
aValues = [2, 3, 4, 5]  # Different small square sizes
cValues = [1, 5, 10, 20]  # Different particle concentrations

# Define color assignment
colors = ['b', 'g', 'y', 'r']  # Blue, Green, Yellow, Red

# Store stuff in a list later on
results = []

# Part (2c)
# Choose specific a and c to measure
exampleA = aValues[0]
exampleC = cValues[0]

N = int(exampleC * squareLength**2) # Compute total particles from concentration, ensure it is an integer!
smallXMin = (squareLength - exampleA) / 2
smallXMax = (squareLength + exampleA) / 2
smallYMin = (squareLength - exampleA) / 2
smallYMax = (squareLength + exampleA) / 2

countsTest = []

# Repeat for statistics
for _ in range(noOfTrials):
    xPos = np.random.uniform(0, squareLength, N)
    yPos = np.random.uniform(0, squareLength, N)

    count_inside = np.sum(
        (smallXMin <= xPos) & (xPos <= smallXMax) &
        (smallYMin <= yPos) & (yPos <= smallYMax)
    )
    countsTest.append(count_inside)

# Compute and print mean and standard deviation
theoreticalMean = (exampleA **2 * N) / (squareLength ** 2)
average = np.mean(countsTest)
standardDev = np.std(countsTest)
print(f"For a={exampleA}, c={exampleC}: Theoretical mean = {theoreticalMean:.3f}, Actual Mean = {average:.3f}, Standard Deviation = {standardDev:.3f}")


# Part (2d)

# Iterate over various values of a
for a in aValues:

    # Iterate over various values of c
    for c in cValues:

        # Compute total particles from concentration

        N = int(c * squareLength**2)  
        smallXMin = (squareLength - a) / 2
        smallXMax = (squareLength + a) / 2
        smallYMin = (squareLength - a) / 2
        smallYMax = (squareLength + a) / 2
        
        counts = []  # Store counts for this (a, c) pair

        for _ in range(noOfTrials):
            # Generate N random molecule positions
            xPos = np.random.uniform(0, squareLength, N)
            yPos = np.random.uniform(0, squareLength, N)

            # Count how many fall inside the small square
            count_inside = np.sum(
                (smallXMin <= xPos) & (xPos <= smallXMax) &
                (smallYMin <= yPos) & (yPos <= smallYMax)
            )
            counts.append(count_inside)

        # Compute mean and standard deviation
        mean_count = np.mean(counts)
        std_count = np.std(counts)
        
        # Compute relative fluctuation (signal to noise ratio)
        delta_c_over_c = std_count / mean_count 
        
        results.append((a, c, delta_c_over_c))

# Convert results to numpy array
results = np.array(results)

# Extract values
# Initialize empty lists to store computed values
a_inv_sqrt = []  # List to hold a^(-1/2) values
c_inv_sqrt = []  # List to hold c^(-1/2) values

# Loop over each entry in results and compute a^(-1/2) and c^(-1/2)
for entry in results:

    # Extract from the data
    a_value = entry[0]  
    c_value = entry[1]
    
    # Raise values to the appropriate power
    a_inv = a_value ** (-0.5)
    c_inv = c_value ** (-0.5)

    # Append to list
    a_inv_sqrt.append(a_inv)  
    c_inv_sqrt.append(c_inv) 

# Convert lists to numpy arrays
a_inv_sqrt = np.array(a_inv_sqrt)
c_inv_sqrt = np.array(c_inv_sqrt)

delta_c_over_c = results[:, 2]

#delta-c / c vs a^(-1/2) 
plt.figure(figsize=(8, 5))

for i, c in enumerate(cValues):
    mask = results[:, 1] == c  # Select data for specific c
    x = a_inv_sqrt[mask]
    y = delta_c_over_c[mask]
    
    # Assign color based on the index
    color = colors[i]

    # Perform linear fit
    slope, intercept, r_value, _, _ = linregress(x, y)
    fit_line = slope * x + intercept
    
    # Plot data points and fit line
    plt.scatter(x, y, color=color, edgecolor='black') 
    plt.plot(x, fit_line, color=color, linestyle="--",
             label=f"c={c}: y = {slope:.3f}x + {intercept:.3f}, r={r_value:.3f}")

plt.xlabel(r"$a^{-1/2}$")
plt.ylabel(r"$\delta c / c$")
plt.title(r"Scaling of $\delta c / c$ with Small Box Size")
plt.legend(loc="upper left", fontsize=9, frameon=True)  # Auto-generated legend with proper colors
plt.show()

# delta-c / c vs c^(-1/2)
plt.figure(figsize=(8, 5))

for i, a in enumerate(aValues):
    mask = results[:, 0] == a  # Select data for specific a
    x = c_inv_sqrt[mask]
    y = delta_c_over_c[mask]
    
    # Assign color based on the index
    color = colors[i] 

    # Perform linear fit
    slope, intercept, r_value, _, _ = linregress(x, y)
    fit_line = slope * x + intercept
    
    # Plot data points and fit line
    plt.scatter(x, y, color=color, edgecolor='black') 
    plt.plot(x, fit_line, color=color, linestyle="--",
             label=f"a={a}: y = {slope:.3f}x + {intercept:.3f}, r={r_value:.3f}")  

# Axis labels and title
plt.xlabel(r"$c^{-1/2}$")
plt.ylabel(r"$\delta c / c$")
plt.title(r"Scaling of $\delta c / c$ with Particle Concentration")

# Legend (auto-colored and matching lines)
plt.legend(loc="upper left", fontsize=9, frameon=True)

# Show plot
plt.show()
