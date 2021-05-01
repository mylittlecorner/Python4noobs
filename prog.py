#!/usr/bin/env python3

import matplotlib.pyplot as plt 
import numpy as np
  
# Creating vectors X and Y 
x = np.linspace(-50, 50, 10000)
y1=0*x 
y = x*(1.0/3.0) -1
  
fig = plt.figure(figsize = (10, 10))
# Create the plot
plt.plot(x, y)
plt.plot(x ,y1)
 
idx = np.argwhere(np.diff(np.sign(y - y1))).flatten() 
plt.plot(x[idx],y1[idx], 'ro')
for i in idx:
	plt.annotate(f'{round(x[i],2)},{round(y[i],2)}' ,(round(x[i],2),round(y[i],2)))

idy = np.argwhere(np.diff(np.sign(x - y1))).flatten()
plt.plot(x[idy],y[idy], 'ro')

for i in idy:
	plt.annotate(f'{round(x[i],2)},{round(y[i],2)}' ,(round(x[i],2),round(y[i],2)))
# Show the plot 
plt.grid()
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show() 
