import numpy as np

# 3.2 Describe how the average per sample, variance, average per culture, and calculated
# ratio between standard deviation and average are derived from this data set. Write a code
# to reproduce these numbers in Luria and Delbrück’s Table 2, which is shown above, with
# any three columns of data

# 2D Array of Data in Luria-Delbruck Experiment:
experimentalData = [[10, 18, 125, 10, 14, 27, 3, 17, 17], [29, 41, 17, 20, 31, 30, 7, 17], [30, 10, 40, 45, 183, 12, 173, 23, 57, 51], [6, 5, 10, 8, 24, 13, 165, 15, 6, 10], [1, 0, 3, 0, 0, 5, 0, 5, 0, 6, 107, 0, 0, 0, 1, 0, 0, 64, 0, 35], [1, 0, 0, 7, 0, 303, 0, 0, 3, 48, 1, 4], [0, 0, 0, 0, 8, 1, 0, 1, 0, 15, 0, 0, 19, 0, 0, 17, 11, 0, 0], [38, 28, 35, 107, 13]]

# Average per sample:
averageList = []
for array in experimentalData:
    avg = float(np.mean(array))
    averageList.append(avg)

print(averageList)