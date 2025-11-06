### Assigment coding for ecnomists, vienna hotels data set. Here was used a raw data set of Vienna hotels for filtering purposes to recevie a clean file.###

print ("Hello, world!") # checking that python works correctly

# Libraries import
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Uploading the data set from internal directory
raw_data=pd.read_csv("C:/Users/korot/Desktop/CEU/Coding/Python_coding/Assignment/Raw_data/hotelbookingdata-vienna.csv")
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

df_0=raw_data.loc[raw_data["city_actual"].str.lower().str.strip()=="vienna"].copy() # filtering only accomodations in Vienna
print(df_0["city_actual"].value_counts()) # checking that everything works

print (raw_data["center1distance"].value_counts()) # checking the situation with miles as a text

miles_to_clean=["center1distance","center2distance"]

for col in miles_to_clean:
    miles=(df_0[col].astype(str)
           .str.extract(r'(\d+\.?\d*)')[0]
           .str.replace(',', '.', regex=False)
           .str.strip()
           ) # removing the miles as a text in two collumns
    df_0.loc[:,col]=pd.to_numeric(miles,errors="coerce") #rewriting the changes of the data set

print(df_0[miles_to_clean].head(10))  # checking that everything works
print(df_0[miles_to_clean].describe()) # checking that everything works
print(df_0) # checking that everything works
print (df_0["city_actual"].value_counts()) # checking that everything works

print(df_0["neighbourhood"].value_counts()) #checking the neigbourhood. But after comparison with the clean version in OSF it was maded decision to stay it as it is (e.g. "17.  Hernals", or "Vienna")

df_0["accommodationtype"]=( #cleaning accomodationtype column. we need only type of accomodation without "Accomodationtype@" text
    df_0["accommodationtype"]
    .astype(str)
    .str.split("@")
    .str[-1]
    .str.strip()
)

print (df_0) #checking if everything works
print(df_0["accommodationtype"].value_counts()) #checking updates in exact column


df_0["guestreviewsrating"]=( #cleaning accomodationtype column. we need only reviews rating without "/5" text
    df_0["guestreviewsrating"]
    .astype(str)
    .str.split(" /")
    .str[0]
    .str.strip()
)

print (df_0) #checking if everything works
print(df_0["guestreviewsrating"].value_counts()) #checking updates in exact column

for col in df_0.columns: 
    print(f"{col}:{df_0[col].dtype}") #checking the type of columns
 
print(df_0["center1distance"].dtype) # noticing that center1distance and center2distance have object type

df_0[miles_to_clean] = df_0[miles_to_clean].astype('Float64') #converting to float64 type

print(df_0['center1distance'].isna().sum()) #checking missing values, if any

print(df_0["center1distance"].dtype) #checking converting has been done succesfully
print(df_0["center2distance"].dtype) #checking converting has been done succesfully

filt_coll = [ #filtering columns, it will be saved only important ones
    "rating_reviewcount",
    "center1distance",
    "center1label",
    "center2distance",
    "center2label",
    "neighbourhood",
    "price",
    "starrating",
    "accommodationtype",
    "guestreviewsrating",
    "hotel_id",
]

df_clean=df_0[filt_coll].copy() #saving filtering results
print (df_clean)

df_clean.to_csv("C:/Users/korot/Desktop/CEU/Coding/Python_coding/Assignment/Clean_data/hotelbookingdata-vienna_clean.csv",index=False)