# 3.4 Replot Luria and Delbrück’s experimental data 22 and 23. The data are in NTULearn ->
# Course -> Content and named LDexpt_22.csv and LDexpt_23.csv, respectively. What is
# the best fit you can get while fitting the data with a Poisson distribution? Below is how Luria
# and Delbrück plot the data and compare it to the theoretical prediction in their original paper.
# In your opinion, does the experimental data follow the expected distribution?

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Experiment 22
expt22 = np.array([
    [0, 57],
    [1, 20],
    [2, 5],
    [3, 2],
    [4, 3],
    [5, 1],
    [6, 7],
    [11, 2],
    [21, 2],
    [51, 0],
    [101, 0],
    [201, 0],
    [501, 1],
    [1001, 0]
])

# Experiment 23
expt23 = np.array([
    [0, 29],
    [1, 17],
    [2, 4],
    [3, 3],
    [4, 3],
    [5, 2],
    [6, 5],
    [11, 6],
    [21, 7],
    [51, 5],
    [101, 2],
    [201, 4],
    [501, 0],
    [1001, 0]
])

# Function to process dataset
def processData(data, title):
    values = np.repeat(data[:, 0], data[:, 1])
    values_limited = values[values <= 6] # Ignore values below 6
    
    # Averages for both cases
    average = np.mean(values)
    limitedAvg = np.mean(values_limited)
    
    # X-axes for both cases
    xValues = np.arange(0, max(values) + 1)
    xValuesLimited = np.arange(0, max(values_limited) + 1)

    # Plotting the poisson fit
    poisson_pmf = poisson.pmf(xValues, mu=average)
    poisson_pmf_limited = poisson.pmf(xValuesLimited, mu=limitedAvg)
    
    plt.figure(figsize=(12, 5))
    
    # Full data plot
    plt.subplot(1, 2, 1)
    plt.hist(values, bins=np.arange(-0.5, max(values) + 1.5, 1), 
             density=True, alpha=0.6, color='b', label="Experimental Data")
    plt.plot(xValues, poisson_pmf, 'ro-', markersize=5, 
             label=f'Poisson Fit ($\lambda$={average:.2f})')
    plt.xlabel("Number of Mutants per Culture")
    plt.ylabel("Probability Density")
    plt.title(f"Poisson Fit - {title} (Full Data)")
    plt.legend()
    plt.grid()
    
    # Limited data plot
    plt.subplot(1, 2, 2)
    plt.hist(values_limited, bins=np.arange(-0.5, max(values_limited) + 1.5, 1), 
             density=True, alpha=0.6, color='g', label="Experimental Data (≤6)")
    plt.plot(xValuesLimited, poisson_pmf_limited, 'ro-', markersize=5, 
             label=f'Poisson Fit ($\lambda$={limitedAvg:.2f})')
    plt.xlabel("Number of Mutants per Culture")
    plt.ylabel("Probability Density")
    plt.title(f"Poisson Fit - {title} (Data ≤ 6)")
    plt.legend()
    plt.grid()
    
    plt.show()

# Process both datasets
processData(expt22, "Experiment 22")
processData(expt23, "Experiment 23")
