# 2. Take n = 5 random samples from the data each time, calculate its mean. Repeat this
# process many times to get the PDF of the sampled means. Plot the distribution for n
# = 5. Run the same calculations with n = 10, 100, 1,000, and 10,000 as well. Plot the
# PDF of the sampled mean for each n.

import csv
import numpy as np
import random
import matplotlib.pyplot as plt

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

sampleList = [5, 10, 100, 1000, 10000]

for num in sampleList:
    meanValues = extractMean(num, 1000)
    plt.hist(meanValues, 200, (0, 4), density=True, label=f"Sample size: {num}")
    plt.title(f"Probability Density of Sampled Means (n = {num})")
    plt.xlabel("Sample Mean")
    plt.ylabel("Probability Density")
    plt.grid()
    plt.legend()
    plt.show()

