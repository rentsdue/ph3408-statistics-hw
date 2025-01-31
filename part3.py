# Part 3: For each n, calculate the corresponding standard deviations of the sampled means.
# Plot the standard deviations you get as a function of n from n = 1 to n = 10,000. What
# do you get? How do you interpret the result?

import csv
import numpy as np
import random
import matplotlib.pyplot as plt
import time

# Extract CSV file name
filename = "CLT_data.csv"

# Creating a list of values
values = []

# Reading through the CSV file
with open(filename, 'r') as csvfile:
    # Creating a csv reader object
    csvreader = csv.reader(csvfile)
    
    # Extracting field names through the first row
    fields = next(csvreader)
    
    # Extracting and flattening each data row one by one, converting to float
    for row in csvreader:
        values.extend(float(value) for value in row)


# Snatch random values to plot onto a new PDF (numSamples - number of random samples from the data, numTrials - number of times iterated)
def extractMean(numSamples, numTrials):

    # List of means
    means = []

    # Iterate by the number of trials
    for trial in range(0, numTrials):

        #Snags a random sample
        randomFloats = random.sample(values, numSamples)

        # Calculates the mean of the list
        mean = np.mean(randomFloats)

        # Adds it to the list
        means.append(mean)
    return means

noTrials = 10
sampleSizes = [1, 10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000]


stdList = []

for num in sampleSizes:
    meanList = extractMean(num, noTrials)
    stdDev = np.std(meanList)
    stdList.append(stdDev)

start_time = time.time()
plt.plot(sampleSizes, stdList, label="Standard Deviation of Sampled Means")
plt.title("Standard Deviation vs Sample Size")
plt.xlabel("Sample Size")
plt.ylabel("Standard Deviation")
plt.grid()
plt.legend()
plt.show()
end_time = time.time()
print(f"Plot loaded in {end_time - start_time} seconds.")
