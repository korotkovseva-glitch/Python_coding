### Assigment coding for ecnomists, vienna hotels data set. Here was used a clean data set of Vienna hotels to demonstrate a summary statistics, graphs an other types of analysis, incl. additional filtering.###

print ("Hello, world!") # checking that python works correctly

# Libraries import
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Uploading the data set from internal directory
clean_data=pd.read_csv("C:/Users/korot/Desktop/CEU/Coding/Assignment/clean/hotelbookingdata-vienna_clean.csv")
print(clean_data.head())