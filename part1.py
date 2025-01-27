import csv
import numpy as np
import matplotlib.pyplot as plt

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
std_dev = np.std(values)
print(f"Standard Deviation: {std_dev}")

# Plot probability density graph
plt.hist(values, 200, (0, 12), density=True, label="Probability Density of Data")
plt.title("Probability Density Graph of CSV File Data")
plt.xlabel("Data Values")
plt.ylabel("Probability Density")
plt.text(0.1, 0.9, f"Standard Deviation: {std_dev:.2f}", transform=plt.gca().transAxes, fontsize=10, color='red') # Standard deviation of the data
plt.grid()
plt.legend()
plt.show()

