%matplotlib inline
import sys
import numpy as np

import matplotlib.pyplot as plt 
import matplotlib.tri as tri
    
class Fem(object):
    
    def __init__(self, nom):
        self.__x = list()  # list of x 
        self.__y = list()  # list of y
        self.__t = list()  # list of triangle apexes (3 values) => list of lists
        
        try:
            with open(nom, 'r') as f:
        # A COMPLETER
        except FileNotFoundError:
            print('error : mesh file not found')
            sys.exit(1)

    def __surfaces(self):
        """ Returns a list of the surface of each mesh element"""
        x=self.__x
        y=self.__y
        surf= list()
        # A COMPLETER            
        return # A COMPLETER 
    
    def __centers(self):
        """ Returns a list of the tuples (xG, yG) corresponding to the center coordinates of each triangle element"""
        x=self.__x
        y=self.__y
        centers=list()

       # A COMPLETER                 
        return # A COMPLETER 
    
    def num_points(self):
        return len(self.__x)
    
    def surface(self):
        """ Compute the total surface """
        return # A COMPLETER 

    def inertia(self): 
        """ Compute the moment of inertia"""
       # A COMPLETER      
        return # A COMPLETER 
    
    def drawmesh(self): 
        x=self.__x
        y=self.__y
        t=self.__t
        
        triang = tri.Triangulation(x, y, t)
        plt.figure(figsize=(5, 5))
        plt.triplot(triang, lw=0.5, color='black')
        plt.plot(x, y, 'o')
        
        for i, (xi, yi) in enumerate(zip(x,y)):
            plt.text(xi, yi, str(i))
            
        for nt, (xi,yi) in enumerate(self.__centers()):
            plt.text(xi,yi, str(nt), bbox=dict(facecolor='red', alpha=1), size=8)
        
        plt.savefig('snap.png')
        plt.savefig('snap.pdf')
        plt.show()
 
if __name__ == "__main__":
    
    fem=Fem('disk_fine.pro')    
    print(fem.num_points())
    fem.drawmesh()

    %timeit S=fem.surface()
    S=fem.surface()
    print("surface : ", S)
    %timeit I=fem.inertia()
    I=fem.inertia()
    print("Inertial momentum : ", I)