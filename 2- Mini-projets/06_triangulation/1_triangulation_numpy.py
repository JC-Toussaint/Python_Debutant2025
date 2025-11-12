#%matplotlib inline
import sys
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.tri as tri
    
class Fem(object):
        
    def __init__(self, nom):
        x = list()  # list of x 
        y = list()  # list of y
        t = list()  # list of triangle apexes (3 values)
        
        try:
            with open(nom, 'r') as f:
                NP=int(f.readline())
                for i in range(NP):
                    line = f.readline()
                    [xi, yi] = line.split() # xi and yi of type str
                    x.append(float(xi))
                    y.append(float(yi))
                self.__xy = np.asarray([x,y])
                print(self.__xy.shape)
                print('-----------')
                
                blank_line =  f.readline() # blank line after 1st part

                NE=int(f.readline()) 
                for ne in range(NE):
                    line = f.readline()
                    lst = line.split()
                    ti=[int(e) for e in lst]
                    t.append(ti)
                self.__t = np.asarray(t)
                #print(self.__t)
                #print('-----------')
        except FileNotFoundError:
            print('error : mesh file not found')
            sys.exit(1)
            
    def __surfaces(self):
        """ Returns a ndarray of the surface of each mesh element"""
        xy = self.__xy
        t  = self.__t
        
        # Px are 2 x Nt arrays
        # Pi corresponds to the coordinates of the first apexes of all triangles
        # Pj corresponds to the coordinates of the second apexes of all triangles, etc...
        Pi = xy[:, t[:, 0]]
        Pj = xy[:, t[:, 1]] 
        Pk = xy[:, t[:, 2]]
        
        AB = Pj-Pi
        AC = Pk-Pi
        surf = 0.5 * np.cross(AB.T, AC.T)    # surf is a 1 x Nt array containing the surface of each triangle
        return surf
    
    def __centers(self):
        """ Returns a ndarray with 2 columns corresponding to the center coordinates of each triangle element"""
        # A COMPLETER
        return # A COMPLETER 

    
    def num_points(self):
        # A COMPLETER
        return # A COMPLETER 
    
    def surface(self):
        """ Compute the total surface """
        # A COMPLETER
        return # A COMPLETER 

    def inertia(self): 
        """ Compute the moment of inertia"""
        # A COMPLETER
        return # A COMPLETER 
    
    def drawmesh(self): 
        x=self.__xy[0]
        y=self.__xy[1]
        t=self.__t
        
        triang = tri.Triangulation(x, y, t)
        plt.figure(figsize=(5, 5))
        plt.triplot(triang, lw=0.5, color='black')
        plt.plot(x, y, 'o')
        
        for i, [xi, yi] in enumerate(self.__xy):
            plt.text(xi, yi, str(i))
            
        for nt, [xi,yi] in enumerate(self.__centers()):
            plt.text(xi,yi, str(nt), bbox=dict(facecolor='red', alpha=1), size=8)
        
        plt.savefig('snap.png')
        plt.savefig('snap.pdf')
        plt.show()
 
if __name__ == "__main__":
    
    fem=Fem('disk_fine.pro')    
    print(fem.num_points())
    #fem.drawmesh()

    %timeit S=fem.surface()
    S=fem.surface()
    print("surface : ", S)
    %timeit I=fem.inertia()
    I=fem.inertia()
    print("Inertial momentum : ", I)