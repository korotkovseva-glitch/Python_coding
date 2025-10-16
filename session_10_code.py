### Lists ###
l = [1, 2.2, "apple", True, [1,"green", False]]
type (l)
print (l)
print (l[1])
print (l[0])
print (l[1:3])
print (l[-1])
print (l[-1][1])
l.reverse()
print (l)
l1=['d','s','a','o']
l1.sort()
print(l1)

for element in l:
    print (element)

print (l)

start=10
stop=20
step=2
list(range(start,stop, step))

start=1900
stop=2000
step=10
list(range(start,stop, step))

list(range(10))

list(range(1,11))

l2=[]
l2.append(1)
l2.append('red')
l2.append(False)
print (l2)

l3=l1+l2
print(l3)

#length
print (len(l))
print(len(l[0]))

#removing elements
l.remove("apple")
print (l)

del l[0]
print (l)

#joining elements 
print(''.join(l1))
print(' '.join(l1))
print('-'.join(l1))

### Tuple ###

height_and_weight=(165,60)
print(type(height_and_weight).__name__)

height_and_weight2=165,60
print(height_and_weight2)
print (type(height_and_weight2).__name__)

print(height_and_weight[0])
#height_and_weight[0]=170 // we cannot change tuple
print(height_and_weight)

for parameter in height_and_weight:
    print(parameter)

height, weight = height_and_weight
print (height)
print (weight)

### Dictionary ###
class_size={
    'Macro':34,
    'Micro':30,
    'Metrics':25
    }
print(type(class_size).__name__)
print(class_size['Macro'])
#print(class_size['Coding']) // example when element is not in dictionary
print('Coding' in class_size.keys())
print(class_size.get('Coding',0))
print(class_size.get('Macro',0))
print(class_size.get('Coding',None))
print(class_size.get('Coding',"Error"))

for key, value in class_size.items():
    print('The number of students in the',key,'class is',value,'.')
print (class_size.keys())
print(class_size.values())

for key in class_size.keys():
    print(key)

### Sets ###

ls_a=['a','b','a',3.4,1000]
st_a=set(ls_a)
print(st_a)
#print(st_a[1]) // there are no indexes in set

st_b={'d',1000,'pineapple','a'} 
print(st_a|st_b)
print (st_a&st_b)
print (st_a-st_b)
print (st_b-st_a)
print (st_b-st_b)

### Module ###

import math

print(math.cos(0))
print(math.cos(2*math.pi))

from math import *

print(cos(pi))

#from numpy import ceil, floor
#print(ceil(5.5))
#print(floor(5.5))

#import pandas as pd
#import numpy as np

#np.pi

#data=[1,2,3,4]
#series=pd.Series(data)
#print(data)
#print(series)

#import os
#current_directory=os.getcwd()
#print (current_directory)
#files=os.listdir(current_directory)
#print(files)
#print(type(files))