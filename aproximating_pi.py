import numpy as np
import matplotlib.pyplot as plt
from numpy import random
def calculate_pi: 
    inside=0
    outside=0

    for i in range(n):
        x=random.random()
        y=random.random()
        r=np.sqrt(x**2+y**2)
        
        if r<1:
        inside=inside+1
        plt.plot(x,y,"r")
        elif r>=1:
        outside=outside+1
        plt.plot(x,y,"b")
    plt.show()    
    pi=(4*inside)/(n)
    return pi


