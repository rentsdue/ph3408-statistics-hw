### Assignment 1: Basic Statistics and Introduction to Stochastic Process

---

#### **1. Central Limit Theorem**

1. **Question 1.1**: 
   - Plot the probability distribution function (PDF) of the given data. Calculate the standard deviation of all the data.

2. **Question 1.2**: 
   - Take \( n = 5 \) random samples from the data each time and calculate its mean. Repeat this process many times to get the PDF of the sampled means.
   - Plot the distribution for \( n = 5 \). 
   - Repeat the calculations with \( n = 10, 100, 1,000, \) and \( 10,000 \), and plot the PDF of the sampled mean for each \( n \).

3. **Question 1.3**:
   - For each \( n \), calculate the corresponding standard deviations of the sampled means.
   - Plot the standard deviations as a function of \( n \), ranging from \( n = 1 \) to \( n = 10,000 \).
   - What do you observe? How do you interpret the result?

---

#### **2. Short Essay**

- Write at least 500 words with a minimum of 3 diagrams.
- **Prompt**: Provide three examples explaining how fluorescence is used in biological studies quantitatively and/or qualitatively.

---

#### **3. Luria and Delbrück Experiment**

1. **Question 3.1**:
   - Explain how the mutation rate and the estimated standard deviation of the number of mutants can be obtained.

2. **Question 3.2**:
   - Describe how the average per sample, variance, average per culture, and the ratio between standard deviation and average are derived from this dataset.
   - Write a code to reproduce these numbers from Luria and Delbrück’s Table 2 using any three columns of data.

3. **Question 3.3**:
   - Explain the rationale for experiments 22 and 23 in Luria and Delbrück’s paper (Table 3).

4. **Question 3.4**:
   - Replot Luria and Delbrück’s experimental data for experiments 22 and 23 using the files `LDexpt_22.csv` and `LDexpt_23.csv`.
   - Find the best fit using a Poisson distribution.
   - Does the experimental data follow the expected distribution? Provide your opinion with justification.