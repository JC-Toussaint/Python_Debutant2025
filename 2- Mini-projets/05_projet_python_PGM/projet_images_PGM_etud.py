"""
Traitement d'images au format PGM
Projet: manipulation d'images en niveaux de gris
"""

import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from PIL import Image
from time import process_time

MAXLVL = 255
MAXTAIL = 256


# Question 1
def fun(x, y):
    # A COMPLETER
    pass


# Question 2
def centering(i, L):
    # A COMPLETER    
    pass


# Question 3
def createImg(fun, NROWS=MAXTAIL, NCOLS=MAXTAIL, NLEVELS=MAXLVL):   
    # A COMPLETER
    pass


# Question 4
def writeImg(img, filename):
    # A COMPLETER
    pass


# Question 5
# PETIT PGM A DEVELOPPER


# Question 6 - CODE FOURNI AUX APPRENANTS
def readImg(filename):
    with open(filename) as f:
        lines = f.readlines()

    # Ignores commented lines
    for l in list(lines):
        if l[0] == '#':
            lines.remove(l)

    # Makes sure it is ASCII format (P2)
    # leading and trailing whitespace removed
    assert lines[0].strip() == 'P2' 

    # Converts data to a list of integers
    data = []
    for line in lines[1:]:
        data.extend([int(c) for c in line.split()])

    return (np.array(data[3:]), (data[1], data[0]), data[2])


# Question 7
# A COMPLETER

# plt.imshow(np.reshape(tup[0], tup[1]), cmap=cm.jet) 
# plt.colorbar()
# plt.show()


# Question 9 - CODE FOURNI AUX APPRENANTS
from time import process_time

# Start the stopwatch / counter 
t1_start = process_time() 

NROWS, NCOLS = 512, 512   
# Z = createImg(fun, NROWS, NCOLS)
  
# Stop the stopwatch / counter
t1_stop = process_time()
print("Elapsed time (s):", t1_stop - t1_start) 


# Question 10
def centering(i, L):
    assert 0 <= i.all() < L, "out of range"
    return (2.0 * i - L) / L
    

def createImgVec(fun, NROWS, NCOLS, NLEVELS=255):    
    # A COMPLETER
    pass


# Question 11 - CODE FOURNI AUX APPRENANTS
from time import process_time

# Start the stopwatch / counter 
t1_start = process_time() 

# A COMPLETER
  
# Stop the stopwatch / counter
t1_stop = process_time()
print("Elapsed time (s):", t1_stop - t1_start) 


# Question 12
def threshold(A, thres):
    # A COMPLETER
    pass


# Question 13
# A COMPLETER


# Question 14
# A COMPLETER


