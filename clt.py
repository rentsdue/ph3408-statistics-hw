# Extract data from csv file
import csv

# csv file name
filename = "CLT_data.csv"

# Initializing rows
rows = []

# Reading csv file
with open(filename, 'r') as csvfile:
    
    # Creating a csv reader object
    csvreader = csv.reader(csvfile)

    # Extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

