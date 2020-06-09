#Jeremy Reiser
#CSE4095 Assignment 5
%matplotlib inline
import numpy as np
import seaborn as sb
import matplotlib.pylab as plt
from IPython.display import display,clear_output

N = 10
minDiff = 0.3          #sets the stopping parameter (once diffusion per loop reaches 0.3 micromolar)
coeff = 5
DX = 0.1
DY = 0.1
DT = DX**2/(2*coeff)   #calculates time interval
x = np.zeros((N,N))
x[3,6] = 23
difference = 1
sb.heatmap(x, linewidth=0.5)
plt.show()

while(difference >= minDiff):
    difference = 0                 #resets total diffusion count for this loop
    for i in range(1, N-1):
        for j in range(1, N-1):    #formula for 2D diffusion:
            diffusion=(DT*((x[i+1,j]-2*x[i,j]+x[i-1,j])/DX**2 + (x[i,j+1]-2*x[i,j]+x[i,j-1])/DY**2) + x[i,j])-x[i,j]
            x[i,j] = x[i,j] + diffusion     #adds diffusion to cell
            difference = difference + abs(diffusion)   #tracks diffusion for this loop
    clear_output(wait=True)
    sb.heatmap(x, linewidth=0.5)    #update plot variables
    plt.show()                      #then replot
    