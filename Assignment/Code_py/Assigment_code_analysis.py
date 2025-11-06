### Assigment coding for ecnomists, vienna hotels data set. Here was used a clean data set of Vienna hotels to demonstrate a summary statistics, graphs an other types of analysis, incl. additional filtering.###

print ("Hello, world!") # checking that python works correctly

# Libraries import
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Uploading the data set from internal directory
clean_data=pd.read_csv("C:/Users/korot/Desktop/CEU/Coding/Python_coding/Assignment/Clean_data/hotelbookingdata-vienna_clean.csv")
print(clean_data.head())

pd.set_option('display.max_columns', None) # to see starrating column
print(clean_data.head())

df_0=clean_data.loc[
    (clean_data["accommodationtype"].str.lower().str.strip()=="hotel")&
    ((clean_data["starrating"]>=3)&(clean_data["starrating"]<=4))&
    (clean_data["price"]<1000) #cleaning anomaly hotels with high price
].copy() # filtering only hotels accomodation type with 3-4 stars in Vienna

print(df_0["accommodationtype"].value_counts()) # checking that everything works
print(df_0["starrating"].value_counts()) # checking that everything works


#Summary statistic of  hotels by distance from city centre, price, and guest review rating depending on stars
summary_stat=(
    df_0
        .groupby("starrating")[["center1distance","price","guestreviewsrating"]]
        .agg(["count","mean","std","min","max"])
        .round(1)
        .T
)

print(summary_stat) 

# Summary statistic results are provided below

#starrating                  3.0    3.5    4.0
#center1distance    count   83.0   14.0  112.0
#                   mean     1.8    1.7    1.3
#                   std      1.3    0.9    1.1
#                   min      0.2    0.3    0.0
#                   max      6.6    3.7    4.8
#price              count   83.0   14.0  112.0
#                   mean    91.8  104.1  125.1
#                   std     39.8   21.1   42.1
#                   min     50.0   75.0   60.0
#                   max    383.0  145.0  242.0
#guestreviewsrating count   83.0   14.0  112.0
#                   mean     3.8    4.4    4.2
#                   std      0.5    0.2    0.3
#                   min      2.2    3.9    3.5
#                   max      4.5    4.5    4.8


# Graphs

import matplotlib.pyplot as plt

distance=list(df_0[df_0.starrating==3]["center1distance"])
price=df_0[df_0.starrating==3]["price"].tolist()

# Histogram review of 3 star hotels by distance and price 

plt.figure(figsize=(10,6)) 
plt.hist(distance,bins=20, color="r",edgecolor="black")
plt.title("Distribution of 3 star hotels by distance from center")
plt.xlabel("Distance from center (miles)")
plt.ylabel("Number of hotels")
plt.show()

plt.figure(figsize=(10,6)) 
plt.hist(price,bins=20, color="r",edgecolor="black")
plt.title("Distribution of 3 star hotels by price")
plt.xlabel("price, EUR per night")
plt.ylabel("Number of hotels")
plt.show()

# Scatter plot review of 3 star hotels by distance and price + defining correlation and regression coefficients between price and distance for 3 star hotels  

x=df_0["center1distance"].astype(float).to_numpy()
y=df_0["price"].astype(float).to_numpy()

plt.figure(figsize=(10,6)) 
plt.scatter(x,y,c=pd.cut(x,bins=10,labels=False),cmap="plasma",alpha=0.9)
s,i=np.polyfit(x,y,1)
corr=np.corrcoef(x,y)[0,1]
r2=corr**2
plt.plot(x,s*x+i,color="black",linewidth=1,label=f"y ={s:.2f}x+{i:.2f}\nCorr={corr:.2f},Rsqr={r2:.2f}")
plt.colorbar(label="Distance bin")
plt.title("Price vs. Distance, 3 Star Hotels")
plt.xlabel("Distance (miles)")
plt.ylabel("Price (EUR)")
plt.legend()
plt.tight_layout()
plt.show()