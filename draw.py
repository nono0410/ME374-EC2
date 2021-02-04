# Graphical simulation for extra credit 2

import math as m
import numpy as np
from scipy.optimize import fsolve
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import closer
plt.style.use('seaborn-pastel')
ref = -1 # Ref leave outside

# Driving crank (L1)
def draw(L0,L1,L2,L3):
    
    # Beta,theta angle definition
    def eq(beta,theta):
        return ((-1*L3*m.cos(beta) + L0 -L1*m.cos(theta))**2 + (-1*L1*m.sin(theta)+L3*m.sin(beta))**2)**0.5 - L2

    # Given angle(i) and previous angle(ref) --> Returns cooresponding B,C,and beta
    def BC(i,ref):

        theta = m.radians(i)

        b__inti = fsolve(eq,ref,theta) # Initialize a rough solution
        beta = (b__inti[0])

        for n in range(360): # Finds closer beta
            test = fsolve(eq,m.radians(n),theta) # Result in radians
            beta = closer.closer(ref,beta,test[0])
            #print(m.degrees(ref),m.degrees(beta),m.degrees(test))
            
        B = L1*m.cos(theta) , L1*m.sin(theta)
        C = -1*L3*m.cos(beta) + L0 , L3*m.sin(beta)
        length = ((-1*L3*m.cos(beta) + L0 -L1*m.cos(theta))**2 + (-1*L1*m.sin(theta)+L3*m.sin(beta))**2)**0.5
        #print(m.degrees(theta),m.degrees(beta),m.degrees(ref))

        return B,C,beta # Return B,C, and beta (radians)

    # Plot and animate results with matplotlib
    fig = plt.figure()
    ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
    line, = ax.plot([], [], lw=3)
    line1, = ax.plot([], [], lw=3)
    line2, = ax.plot([], [], lw=3)

    def init():
        line.set_data([], [])
        line1.set_data([], [])
        line2.set_data([], [])
        return line,line1,line2

    def animate(i):
        i = 2*i # Speed up
        global ref
        B,C,ref = BC(i,ref) #i in range of 0 to 360

        line.set_data([0,B[0]],[0,B[1]])
        line1.set_data([L0,C[0]],[0,C[1]])
        line2.set_data([B[0],C[0]],[B[1],C[1]]) # BC link
        return line,line1,line2

    anim = FuncAnimation(fig, animate, init_func=init,frames=360, interval=1, blit=True)
    plt.show()
