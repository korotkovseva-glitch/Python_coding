print ("hello")
#da-coding-python/ lecture05-graphs-basics/01_plotine_intro

import matplotlib.pyplot as plt

# Functional approach

x=range(0,10)
print (x)
y=[i**2 for i in x]
print (y)

plt.subplot(1,2,1)
plt.plot(x,y,"r--")
plt.title("x-squared")
plt.xlabel("x")
plt.ylabel("y")
plt.legend("x")

plt.subplot(1,2,2)
plt.plot(y,x,"g*-")
plt.title("square toor of x")
plt.show()

# Object-oriented approach

x=range(0,10)
print (x)
y=[i**2 for i in x]
print (y)

#fig = plt.figure()
#axes1=fig.add_axes([0.1,0.1,0.8,0.8])
#axes2=fig.add_axes([0.1,0.4,0.4,0.3])

# Main figure
#axes1.plot(x,y,"r")
#axes1.set_xlabel("x")
#axes1.set_ylabel("y")
#axes1.set_title("Simple x-squared")

# Additional figure
#axes2.plot(y,x,"g")
#axes2.set_xlabel("y")
#axes2.set_ylabel("x")
#axes2.set_title("Square root of x")

import pandas as pd
import numpy as np

#df = pd.read_csv('https://osf.io/4pgrf/download')
df.head()
df.shape
df.columns

df["ticker"].unique()

df["ref.date"]=pd.to_datetime(df["ref.date"])
df["ref.date"].dtype

date=list(df[df.ticker=="MSFT"]["ref.date"])
price=df[df.ticker=="MSFT"]["price.close"].tolist()

date_apple=list(df[df.ticker=="AAPL"]["ref.date"])
price_apple=df[df.ticker=="APPL"]["price.close"].tolist()

fig=plt.figure(figsize=(10,6))
ax = fig.add_axes([0,0,1,1])
ax.plot(date,price,label="MSFT")
ax.plot(date_apple,price_apple,label="AAPL")
ax.set_title("MSFT and APPL closing price")
plt.legend(loc="upper left")
plt.show()