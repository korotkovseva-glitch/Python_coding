print ("Hello world!")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ps = pd.Series(["a",2,np.pi,36])
print (ps)
type(ps)
print(ps.values)
print (ps.index)

print(ps[1:3])

#.loc and .iloc

ps1=pd.Series(
    data=[
        "Introdusction to Micro",
        "Game Theory",
        "Advanced Micro"
    ],
    index=[
        "Bachelor",
        "Master",
        "Phd"
    ]
)
print (ps1)

print(ps1.loc[["Bachelor","Phd"]])
print(ps1.loc["Bachelor":"Phd"])
print (ps1.iloc[[0,2]])
print (ps1.iloc[1:2])

dc_uni_graduation={
    2022: 100,
    2023: 120,
    2024: 90
}
ps_uni_graduation=pd.Series(dc_uni_graduation)
print(ps_uni_graduation)
print (ps_uni_graduation.index)
print (ps_uni_graduation.values)
print(type(ps_uni_graduation))

dc_uni_enrolment={
    2022: 150,
    2023: 80,
    2024: 120
}
ps_uni_enrolment=pd.Series(dc_uni_enrolment)
print(ps_uni_enrolment)

df_uni=pd.concat([ps_uni_enrolment,ps_uni_graduation],axis=1)
df_uni.columns=["enrolment","graduation"]
print(df_uni)
type(df_uni)

print(df_uni.iloc[1:3])
print(df_uni.iloc[-1])
print(df_uni.iloc[-1,0])
print(df_uni.loc[[2023,2024]])
print(df_uni.loc[2023:2024])

print(df_uni[(df_uni.graduation>100) | (df_uni.enrolment<100)]) # add more rules

#ps1[ps.values.isin("Phd")]

print(df_uni.reset_index(drop=False, inplace=True))
print(df_uni.rename({"index":"year"},axis="columns",inplace=True))
print(df_uni[df_uni.year.isin([2022,2024])])
print(~df_uni[df_uni.year.isin([2022,2024])])

df_uni2=[]
df_uni2.append([2022,150,100])
df_uni2.append([2023,80,120])
df_uni2.append([2024,120,90])
print(df_uni2)

df_uni2=pd.DataFrame(data=df_uni2,
                     columns=[
                         "year",
                         "enrolement",
                         "graduation"]
                         )

df_uni2=df_uni2[["year","graduation","enrolement"]]
print(df_uni2)

print(df_uni2.info())
print(df_uni2.shape)
print(type(df_uni2.shape))
rows,columns=df_uni2.shape
print(rows)
print(columns)

raw_data=pd.read_csv("https://osf.io/yzntm/download")
print(raw_data.head())

raw_data["nnights"]=1
print(raw_data.head())

df=raw_data.assign(nnights=0)
print(df)
del raw_data

print(df[["accommodationtype","price"]])
print(df.filter(["accommodationtype","price"]))
print(df.filter(regex="rating"))

# Cleaning

print(df["accommodationtype"].str.split("@"))
print(df["accommodationtype"].str.split("@").str[1])
print(df["accommodationtype"].str.split("@").str[1].str.strip())
df['acc_type']=df["accommodationtype"].str.split("@").str[1].str.strip()
print(df['acc_type'])

print(df["guestreviewsrating"].value_counts(dropna=False))
df["ratings"]=df["guestreviewsrating"].str.split('/').str[0].str.strip()
df["guestreviewsrating"].dtypes
df["ratings"]=df["ratings"].astype(float)
df["ratings"].dtypes
df["ratings"].value_counts()

#Renaming variables
df=df.rename(columns={"rating_reviewcount":"rating_count",
                      "rating2_ta":"ratinga"})
df.filter(regex="rating")

#Filtering observations
df.shape
df.loc[df["acc_type"]=="Hotel"]
#df["acc_type"].loc[df["acc_type"]=="Hotel"].value_counts()
print(df["ratings"].isnull().sum())
df=df.loc[df["ratings"].notnull()]
#df=df.loc[~df["ratings"].isnull()] # same output for line 136
df=df.dropna(subset=["ratings"])
df.shape

#Correction wrongly documented observations
df["starrating"].value_counts(dropna=False)
df["starrating"]=np.where(df["starrating"]==0,None,df["starrating"])
df["starrating"].value_counts(dropna=False)

# Removing duplicates
print(df.duplicated().sum())
df=df.drop_duplicates()
df.shape

important_vatiables=[
    "s_city",
    "hotel_id",
    "addresscountryname",
    "year",
    "month"
]
df=df.drop_duplicates(subset=important_vatiables)
df.shape

#Descriptive statistics (lecture07-data-exploration on GitHub)
df.describe()

#Saving output
#import os
#os.mkdir("output")
df.to_csv("hotels_data_clean.csv",index=False)
