# Problem: To have an initial Python script to play with
# Target Users: Me
# Target System: Windows
# Interface: Command Line
# Functional Requirements: TBD. For now just do some simple stuff
# Testing: 
# Maintainer: Kem White
#


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
print(sys.version)
import random
import math
print("Hello, world?")
print("Hello, World!")
print("Now is the time for all good men to come to the aid of their party.",end='\n')

# Create 2 new lists height and weight
#%%
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
print(height)
print(weight)
print(plt.style.available)
plt.style.use('classic')
#
#  Plot
#
fig, ax = plt.subplots()
ax.plot(height,weight, linewidth=1.0)
plt.grid(True)
plt.show()
#%%
print(height)
print(weight)

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print(np_height)
print(np_weight)

print(np.pi)

myVar = random.gauss(0,1)
print(myVar)
print(random.gauss(0,1))

# Now computer the factorial of a number
n=22
a=math.factorial(n)
print(a)
print(math.factorial(n))

# Now compute the cosine of an angle in degrees.
myAngle = 45.*math.pi/180.0
print('pi= ', math.pi)
print('myAngle = ',myAngle)
myCosine = math.cos(myAngle)
print('myCosine = ',myCosine) 

#
s=pd.Series([1, 3, 5, np.nan, 6, 8])
print(s,end='\n')