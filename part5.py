# 3.4 Replot Luria and Delbrück’s experimental data 22 and 23. The data are in NTULearn ->
# Course -> Content and named LDexpt_22.csv and LDexpt_23.csv, respectively. What is
# the best fit you can get while fitting the data with a Poisson distribution? Below is how Luria
# and Delbrück plot the data and compare it to the theoretical prediction in their original paper.
# In your opinion, does the experimental data follow the expected distribution?
import csv

# Extract CSV file name
filename1 = 'LDexpt22.csv'

# Creating a list of values
values = []

# Reading through the CSV file
with open(filename1, 'r') as csvfile:
    # Creating a csv reader object
    csvreader = csv.reader(csvfile)
    
    # Extracting field names through the first row
    fields = next(csvreader)
    
    # Extracting and flattening each data row one by one, converting to float
    for row in csvreader:
        values.extend(float(value) for value in row)
    
# Mean is the lambda parameter of the Poisson Distribution
mean = np.ave