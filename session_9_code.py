#print("Hello world!")
var23_revised = 1
print (var23_revised) # printing the var23_revised variable
# How to name our variables in Python

a = 3
print (type (a))
b = 1.2
print (type (b))
c = 'a'
d = "abc"
print(type(c))
print(type(d))
print (float (a))
print (str (a))
print (int (b))
print (float(int(b)))
# print (int (c))

# fundamental types
# integers, float, boolean, complex numbers
i = True
j = False
print (type(i))
print (type(j))
print (i+j)
print (i*j)
print (int (j))
print (str (i))

# Operators
print (1+2, 1-2, 1*2, 1/2)
print (3.0//2.0)
print (10//6)
print (10//6.0)
print (2**3)
print (2/1)
print (True and False)
print (not False)
print (True or False)
print (False and False)

# for comparison
x = 2
y = 3
z = 3
print (x>y)
print (y==z)
print (y is z)
print (True==1)

#strings
s = "Hello Monty!"
print (s)
print (len(s))
print (s.replace('Monty','Python'))
print (s[0:5])
print (s[-6:])
print (s[:])
print (s[::2])
s2 = "Hello Monty Python!"
print (s2.split(' '))
print (s2.split(' ') [1])
print (s2.split('o'))
print ('Hello \n world!')
print ('Hello \\n world!')
print ('Monty'+'Python')
print (''.join(['Monty','Python']))
print (' '.join(['Monty','Python']))
print ('+'.join(['Monty','Python']))
print ("hello", a)
print ("The outcome of interest is",a)
a = 4
print ("The outcome of interest is",a)
# print ('The first outcome of interest is %.2f', a)

#continiuning
print ('Hello, my name is %s. I am on year MA %f of my MA program.This is Coding for Economists session %d.' % ('Seva',2, 10))
print ('Hello, my name is %s. I am on year MA %s of my MA program.This is Coding for Economists session %d.' % ('Seva','2', 10))

name = 'Seva'
session_number=10
print(f'My name is {name}. Today\'s coding session is {session_number}.')

print ('{} divided by {} is {}.'.format(2000,1500,2000/1500))
print ('{:,d} divided by {:,.0f} is {:.2f}.'.format(2000,1500,2000/1500))

print(type(a))
print(type(a).__name__)