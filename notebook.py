#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis - Assignment
# 
# ## 🔍 Overview
# This lab is designed to help you practice exploratory data analysis using Python. You will work with some housing data for the state of California. You will use various data visualization and analysis techniques to gain insights and identify patterns in the data, and clean and preprocess the data to make it more suitable for analysis. The lab is divided into the following sections:
# 
# - Data Loading and Preparation
# - Data Visualization
# - Data Cleaning and Preprocessing (using visualizations)
# 
# ## 🎯 Objectives
# This assignment assess your ability to:
# - Load and pre-process data using `pandas`
# - Clean data and preparing it for analysis
# - Use visualization techniques to explore and understand the data
# - Use visualization techniques to identify patterns and relationships in the data
# - Use visualization to derive insights from the data
# - Apply basic statistical analysis to derive insights from the data
# - Communicate your findings through clear and effective data visualizations and summaries

# #### Package Imports
# We will keep coming back to this cell to add "import" statements, and configure libraries as we need

# In[7]:


# Common imports
import numpy as np
import pandas as pd
from scipy.stats import trim_mean

# To plot figures
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix


# Configure pandas to display 500 rows; otherwise it will truncate the output
pd.set_option('display.max_rows', 500)
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)
plt.style.use("bmh")


# ## Housing Data in California

# ### Task 1:  Load the dataset
# The dataset is available in the `data/housing.csv` file. Check the file to determine the delimiter and/or the appropriate pandas method to use to load the data.
# 
# Make sure you name the variable `housing` and that you use the appropriate pandas method to load the data.

# In[10]:


# 💻 Import the dataset in the project (data/housing.csv) into a dataframe called (housing)
housing = pd.read_csv("data/housing.csv")



# ### Task 2: Confirm the data was loaded correctly

# #### 2.1: Get the first 6 records of the dataset

# In[11]:


# 💻 Get the first 6 records of the dataframe
housing.head(6)


# #### 2.2: Get the last 7 records of the dataset

# In[12]:


# 💻 Get the last 7 records of the dataframe
housing.tail(7)


# #### 2.3: Get a random sample of 10 records

# In[13]:


# 💻 Get a random 10 records of the dataframe
housing.sample(10)


# #### 2.4: Get information about the dataset, including the number of rows, number of columns, column names, and data types of each column

# In[14]:


# 💻 Show information about the different data columns (columns, data types, ...etc.)
housing.info()


# > 🚩 This is a good point to commit your code to your repository.

# ### Task 3: Understand the data types
# For each of the 10 columns, Identify the data type: (Numerical-Continuous, Numerical-Discrete, Categorical-Ordinal, Categorical-nominal )
# 
# <details>
# <summary>Click here for the data type diagram</summary>
# 
#   ![Data types](https://miro.medium.com/max/1400/1*kySPZcf83qLOuaqB1vJxlg.jpeg)
# </details>
Longitude:          💻:Numerical-Continuous
Latitude:           💻:Numerical-Continuous
Housing Median Age: 💻:Numerical-Continuous
Total Rooms:        💻:Numerical-discrete
Total Bedrooms:     💻:Numerical-discrete
Population:         💻:Numerical-discrete
Households:         💻:Numerical-discrete
Median Income:      💻:Numerical-Continuous
Median House Value: 💻:Numerical-Continuous
Ocean Proximity:    💻:Categorical-Nominal
# > 🚩 This is a good point to commit your code to your repository.

# ### Task 4: Understand the data
# #### 4.1: Get the summary statistics for the numerical columns

# In[15]:


# 💻 Show the descriptive statistics information about the columns in the data frame
housing.describe()


# #### 4.2: For the categorical columns, get the frequency counts for each category
# 
# <details>
#   <summary>🦉 Hints</summary>
# 
#   - Use the `value_counts()` method on the categorical columns
# </details>

# In[16]:


# 💻 Show the frequency of the values in the ocean_proximity column
housing["ocean_proximity"].value_counts()


# > 🚩 This is a good point to commit your code to your repository.

# ### Task 5: Visualize the data

# #### 5.1: Visualize the distribution of the numerical columns
# In a single figure, plot the histograms for all the numerical columns. Use a bin size of 50 for the histograms

# In[9]:


# 💻 Plot a histogram of all the data features( with a bin size of 50)


# #### 5.2: Visualize the distribution of only one column
# Plot the histogram for the `median_income` column. Use a bin size of 50 for the histogram

# In[10]:


# 💻 plot a histogram of only the median_income


# > 🚩 This is a good point to commit your code to your repository.

# #### 5.3: Visualize the location of the houses using a scatter plot
# In a single figure, plot a scatter plot of the `longitude` and `latitude` columns. 
# 
# 
# Try this twice, once setting the `alpha` parameter to set the transparency of the points to 0.1, and once without setting the `alpha` parameter.

# In[11]:


# 💻 scatter plat without alpha


# In[12]:


# 💻 scatter plat with alpha


# > 🚩 This is a good point to commit your code to your repository.

# 💯✨ For 3 Extra Credit points; Use the Plotly express to plot the scatter plot on a map of california
# 
# (📜 Check out the examples on their docs)[https://plotly.com/python/scatter-plots-on-maps/]

# In[13]:


# 💻💯✨ Plot the data on a map of California


# > 🚩 This is a good point to commit your code to your repository.

# ### Task 6: Explore the data and find correlations

# #### 6.1: Generate a correlation matrix for the numerical columns

# In[14]:


# 💻 Get the correlation matrix of the housing data


# #### 6.2: Get the Correlation data fro the `median_house_age` column
# sort the results in descending order

# In[15]:


# 💻 Get the correlation data for just the median_house_age


# #### 6.2: Visualize the correlation matrix using a heatmap
# - use the coolwarm color map
# - show the numbers on the heatmap
# 

# In[16]:


# 💻 Plot the correlation matrix as a heatmap


# #### 6.3: Visualize the correlations between some of the features using a scatter matrix
# - Plot a scatter matrix for the `total_rooms`, `median_house_age`, `median_income`, and `median_house_value` columns

# In[17]:


# 💻 using Pandas Scatter Matrix Plotting, Plot the scatter matrix for (median_house_value, median_income, total_rooms, housing_median_age)


# #### 6.4: Visualize the correlations between 2 features using a scatter plot
# - use an `alpha` value of 0.1

# In[18]:


# 💻 Plot the scatter plot for just (median_income and median_house_value)


# #### 6.5: ❓ What do you notice about the chart? what could that mean?
# What could the lines of values at the top of the chart mean here?
💻:
# > 🚩 This is a good point to commit your code to your repository.

# ### Task 7: Data Cleaning - Duplicate Data

# #### 7.1: Find duplicate data

# In[19]:


# 💻 Identify the duplicate data in the dataset


# ### Task 8: Data Cleaning - Missing Data

# #### 8.1: Find missing data

# In[20]:


# 💻 Identify the missing data in the dataset


# #### 8.2: show a sample of 5 records of the rows with missing data
# Notice there are 2 keywords here: `sample` and (rows with missing data)
# 
# <details>
#   <summary>🦉 Hints:</summary>
# 
#   * You'll do pandas filtering here
#   * You'll need to use the `isna()` or `isnull()` method on the 1 feature with missing data. to find the rows with missing data
#   * you'll need to use the `sample()` method to get a sample of 5 records of the results
# </details>

# In[21]:


# 💻 use Pandas Filtering to show all the records with missing `total_bedrooms` field


# #### 8.3: Calculate the central tendency values of the missing data feature
# * Calculate the mean, median, trimmed mean

# In[22]:


# 💻 get the mean, median and trimmed mean of the total_bedrooms column
total_bedrooms_median = 0
total_berooms_mean = 0
total_bedrooms_trimmed_mean = 0

print(f"Median: {total_bedrooms_median}")
print(f"Mean: {total_berooms_mean}")
print(f"Trimmed Mean: {total_bedrooms_trimmed_mean}")


# #### 8.4: Visualize the distribution of the missing data feature
# * Plot a histogram of the missing data feature (total_bedrooms)

# In[23]:


# 💻 Plot the histogram of the total_bedrooms column


# #### 8.5: Choose one of the central tendency values and use it to fill in the missing data
# * Justify your choice
# * Don't use the `inplace` parameter, instead, create a new dataframe with the updated values. (this is a bit challenging)
# * show the first 5 records of the new dataframe to confirm we got the full dataframe
# 
# [📜 You should find a good example here](https://www.sharpsightlabs.com/blog/pandas-fillna/#example-2)

# In[24]:


# 💻 Fill the missing values in the total_bedrooms column with an appropriate value, then show the first 5 records of the new dataframe


# ❓ Why did you choose this value?
💻
# #### 8.6: Confirm that there are no more missing values in the new dataframe
# * make sure the dataframe contains all features, not just the `total_bedrooms` feature

# In[25]:


# 💻 Confirm the new dataframe has no missing values


# #### 8.7: Dropping the missing data
# assume we didn't want to impute the missing data, and instead, we wanted to drop the rows with missing data.
# * don't use the `inplace` parameter, instead, create a new dataframe with the updated values.

# In[26]:


# 💻 drop the missing rows of the total_bedroom and save it to a new dataframe


# #### 8.8: Confirm that there are no more missing values in the new dataframe
# * make sure the dataframe contains all features, not just the `total_bedrooms` feature

# In[27]:


# 💻 Confirm the new dataframe has no missing values


# > 🚩 This is a good point to commit your code to your repository.

# ## Wrap up
# Remember to update the self reflection and self evaluations on the `README` file.

# Make sure you run the following cell; this converts this Jupyter notebook to a Python script. and will make the process of reviewing your code on GitHub easier

# In[28]:


# 🦉: The following command converts this Jupyter notebook to a Python script.
get_ipython().system('jupyter nbconvert --to python notebook.ipynb')


# > 🚩 **Make sure** you save the notebook and make one final commit here
