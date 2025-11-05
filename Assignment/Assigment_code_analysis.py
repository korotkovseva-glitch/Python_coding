### Assigment coding for ecnomists, vienna hotels data set. Here was used a clean data set of Vienna hotels to demonstrate a summary statistics, graphs an other types of analysis, incl. additional filtering.###

print ("Hello, world!") # checking that python works correctly

# Libraries import
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Uploading the data set from internal directory
clean_data=pd.read_csv("C:/Users/korot/Desktop/CEU/Coding/Assignment/clean/hotelbookingdata-vienna_clean_1.csv")
print(clean_data.head())

pd.set_option('display.max_columns', None) # to see starrating column
print(clean_data.head())

df_0=clean_data.loc[
    (clean_data["accommodationtype"].str.lower().str.strip()=="hotel")&
    ((clean_data["starrating"]>=3)&(clean_data["starrating"]<=4))
].copy() # filtering only hotels accomodation type with 3-4 stars in Vienna

print(df_0["accommodationtype"].value_counts()) # checking that everything works
print(df_0["starrating"].value_counts()) # checking that everything works

