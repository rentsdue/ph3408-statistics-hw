import csv
import numpy as np
import matplotlib.pyplot as plt
import random

# 1. Plot the probability distribution function (PDF) of the given data. Calculate the
# standard deviation of all the data.

# Extract CSV file name
filename = 'CLT_data.csv'

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

# Find standard deviation, mean of the data
# std_dev = np.std(values)
# print(f"Standard Deviation: {std_dev}")

# # Plot probability density graph (Part 1)
# plt.hist(values, 200, (0, 12), density=True, label="Probability Density Graph of Data")
# plt.xlabel("Frequency of Values")
# plt.ylabel("Probability Density")
# plt.grid()
# plt.legend()
# plt.show()

# 2. Take n = 5 random samples from the data each time, calculate its mean. Repeat this
# process many times to get the PDF of the sampled means. Plot the distribution for n
# = 5. Run the same calculations with n = 10, 100, 1,000, and 10,000 as well. Plot the
# PDF of the sampled mean for each n.

# Snatch random values to plot onto a new PDF
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

noOfSamples = 1000 # Number of samples to average
noOfTrials = 1000 # Number of times to iterate
meanValues = extractMean(noOfSamples, noOfTrials)

# plt.hist(meanValues, 200, (0, 4), density=True, label="Probability Density Graph of Sampled Means")
# plt.title("Mean frequencies")
# plt.xlabel("Mean Value")
# plt.ylabel("Probability Density")
# plt.grid()
# plt.legend()
# plt.show()

# Part 3: For each n, calculate the corresponding standard deviations of the sampled means.
# Plot the standard deviations you get as a function of n from n = 1 to n = 10,000. What
# do you get? How do you interpret the result?

noTrials = 500
sampleSizes = range(1, noTrials) 
stdList = []

for num in sampleSizes:
    meanList = extractMean(num, noTrials)
    stdDev = np.std(meanList)
    stdList.append(stdDev)

plt.plot(sampleSizes, stdList, label="Standard Deviation of Sampled Means")
plt.title("Standard Deviation vs Sample Size")
plt.xlabel("Sample Size (i)")
plt.ylabel("Standard Deviation")
plt.grid()
plt.legend()
plt.show()