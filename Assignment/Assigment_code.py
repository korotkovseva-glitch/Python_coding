### Assigment coding for ecnomists, vienna hotels data set###

print ("Hello, world!") # checking that python works correctly

# Libraries import
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Uploading the data set from internal directory
raw_data=pd.read_csv("C:/Users/korot/Desktop/CEU/Coding/Assignment/raw/hotelbookingdata-vienna.csv")
print(raw_data.head())

#Downloading a raw csv. file from OSF via link (fyi, it's a permanent link, so it provided as an alternative option, commented below)
#raw_data=pd.read_csv("https://storage.googleapis.com/cos-osf-prod-files-de-1/06fae0a9021c1d6c1bf50ac4c14f3c6f34cbe3924c1baf1f49f63b8df03a550b?response-content-disposition=attachment%3B%20filename%3D%22hotelbookingdata-vienna.csv%22%3B%20filename%2A%3DUTF-8%27%27hotelbookingdata-vienna.csv&GoogleAccessId=files-de-1%40cos-osf-prod.iam.gserviceaccount.com&Expires=1762164660&Signature=uR9gSIcNDaR9wkDHKa18%2BJTDxpecUrU62pnNdRkR6MMHVSILxv1Yx3EG8XLFq00aHzcRalzsLnhmjV3ACesloqUtu4E42POhofvntkCyojsiC5VBA%2BZgUzxHobcJtKIz2JiQ94%2B90ISIaf%2Fp6ZRZVIQ%2FJwpFAS2Va0k4RA7nU2qfVESpUtVDJppGZvrvkIIl7qgzBB5J70G7YyYDWNlrCq5PVl5mG%2FLWGaE9g2yIAfoAjrJ2xWnGyexXbDazIZ%2FZaGilkpknoPsGvh4InYrqOoASyAvGm38bPHcxYmL2p7UWSXHQSoG5d9nmXf226JfNIyTQzgrHcL3D3Y5E5yjqKA%3D%3D")
#print(raw_data.head()) # checking that the data was uploaded correctly

column_list=raw_data.columns.tolist() # Creating the list of columns for "for" loop
print(column_list) 

for column in column_list: # Checking the raw data by each column
    print(raw_data[column].head()) # first 5
    print(raw_data[column].tail()) # last 5
    print(raw_data[column].describe()) # summary

#print (raw_data.rating_reviewcount)
#print(raw_data['rating_reviewcount'].describe())

print(raw_data["city_actual"].unique()) # checking another uniqe variables (4) instead of Vienna
print (raw_data["city_actual"].value_counts()) # We see that there are an aglomerations in data set. For this exervice, they will be exluded

df_1=raw_data[raw_data["city_actual"].str.lower().str.strip()=="vienna"] # filtering only accomodations in Vienna
print(df_1["city_actual"].value_counts()) 

print (raw_data["center1distance"].value_counts())

df_2=(df_1["center1distance"].str.extract(r'(\d+\.?\d*)')[0].astype(float))
print (df_2["center1distance"].describe())