import numpy as np
from numpy import random
import matplotlib.pyplot as plt

def calculate_pi(n):
    inside=0
    outside=0
    
    for i in range(n):
        x=random.random()
        y=random.random()
        
        r=np.sqrt((x**2)+(y**2))
        
        if r<1:
            inside+=1
            plt.plot(x,y,"ro")
        elif r>=1:
            outside +=1
            plt.plot(x,y,"bo")
            
    plt.show()
    pi= 4*(inside/(n))
    return pi
