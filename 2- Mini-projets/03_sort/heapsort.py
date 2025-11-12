"""
Converted from notebook: heapsort.ipynb
This file was generated automatically. Markdown cells are included as commented blocks.
"""

# ---- Markdown cell 1 ----
# #  Mini-projet : tri rapide d'une liste
# 
# 
# On génère une liste aléatoire $T$  de $N=1000$ entiers que l'on désire
# trier par ordre croissant. 
# 
# * Utiliser la  fonction  du module random __random.randint__ pour générer les nombres.
# Que remarquez-vous quand vous exécutez deux fois cette fonction?
# 
#  Faire la même chose en la précédant de l'instruction 
# __random.seed(12345)__ qui initialise le générateur de nombres aléatoires avec une graine.
# Même question que précédemment.
# 
# ## Tri par bulle :
# * On vous fournit le code de tri par bulle.
# * Pourquoi peut-on supprimer la ligne retournant la liste T dans la fonction `tri_bulle(T)` ?

# ---- Code cell 2 ----
import random

def tri_bulle(T):
    n=len(T)
    while True:
        change=False
        for i in range(n-1):
            j=i+1
            if T[i]>T[j]:
                change=True
                T[i], T[j]= T[j], T[i] # liste
        if change==False:
            break
#   return T

#initialisation du générateur de nombres aléatoires
random.seed(42)

# Nombre d'éléments dans la liste
N = 10
# Limites des nombres aléatoires
lower_bound = 1
upper_bound = 100

# Générer la liste de nombres aléatoires
T = [random.randint(lower_bound, upper_bound) for _ in range(N)]

#T=tri_bulle(T)
tri_bulle(T)
print(T)

# ---- Markdown cell 3 ----
# ## Tri rapide :
# Hoare a inventé en 1962, une méthode de type "diviser pour régner"  permettant de trier un
# tableau en $N \ln N$ opérations. 
# Son algorithme s'écrit :
# 
# ![image.png](attachment:image.png)
# 
# * Implémenter l'algorithme de tri rapide.

# ---- Markdown cell 4 ----
# La boucle conditionnelle __repeat ... until (condition)__ n'existe pas en Python, on vous demande de proposer une implémentation possible. 
# On prend l'exemple d'une boucle incrémentale gérée par une variable $i$ variant
# de 0 à 9 avant l'incrémentation.
# 
# ![image.png](attachment:image.png)
# 
# Cet algorithme peut être traduit en python par:

# ---- Code cell 5 ----
i=0
while True:
	print(i)
	i=i+1
	if i==10:
		break

# ---- Markdown cell 6 ----
# Tester cette implémentation dans un programme à part.

# ---- Code cell 7 ----
def f(N):
    i=0
    while True:
        print(i)
        i=i+1
        if i==N:
            break
f(5)

# ---- Markdown cell 8 ----
# Implémenter l'algorithme suivant sous la forme d'une fonction Python. 
# On rappelle que l'échange des valeurs de deux variables $a \leftrightarrow b$ en python s'écrit :
# $a,\; b=b,\; a$.
# 
# Son appel tri\_rapide(A, 0, len(A)-1) trie le tableau A in-place.

# ---- Code cell 9 ----
# Version 1 : simple traduction de l'algo
import random
def tri_rapide(T, g, d):
    # A COMPLETER
    return T

def partition(T, g, d):
    # A COMPLETER
                  
#initialisation du générateur de nombres aléatoires
random.seed(42)

# Nombre d'éléments dans la liste
N = 10
# Limites des nombres aléatoires
lower_bound = 1
upper_bound = 100

# Générer la liste de nombres aléatoires
T = [random.randint(lower_bound, upper_bound) for _ in range(N)]

print(T)
T=tri_rapide(T, 0, N-1)
print(T) 

# ---- Markdown cell 10 ----
# * Tenir compte que la liste T est en entrée-sortie. On a de la chance que l'algorithme de tri fonctionne encore
# sans faire de copie du tableau passé en entrée. 

# ---- Code cell 11 ----
# Version 2 : T est en entrée-sortie
import random
def tri_rapide(T, g, d):
    # A COMPLETER
#    return T  # NE PAS MODIFIER

def partition(T, g, d):
    # A COMPLETER
        
            
#initialisation du générateur de nombres aléatoires
random.seed(42)

# Nombre d'éléments dans la liste
N = 10
# Limites des nombres aléatoires
lower_bound = 1
upper_bound = 100

# Générer la liste de nombres aléatoires
T = [random.randint(lower_bound, upper_bound) for _ in range(N)]

print(T)
tri_rapide(T, 0, N-1)
print(T) 

# ---- Markdown cell 12 ----
# ## Temps de calcul
# 
# Pour mesurer la complexité d'un algo, on choisit le cas le plus défavorable qui est ici une
# liste ordonnée de manière décroissante.
# La première méthode pour mesure le temps est :

# ---- Code cell 13 ----
from time import process_time

# Start the stopwatch / counter 
t1_start = process_time() 
   
N=1000
T = [_ for _ in range(N, 0, -1)]

tri_bulle(T)
  
# Stop the stopwatch / counter
t1_stop = process_time()
print("Elapsed time (s):", t1_stop-t1_start) 

# ---- Markdown cell 14 ----
# ou encore dans Ipython en utilisant `%timeit`
# devant la fonction à mesurer. Cette commande fait une moyenne statistique sur les temps. 

# ---- Code cell 15 ----
import timeit
import sys 
     
# Set the stack size to 100000 
sys.setrecursionlimit(100000) 

def f(N):
    T = [_ for _ in range(N, 0, -1)]
    tri_bulle(T)
    return T

def g(N):
    T = [_ for _ in range(N, 0, -1)]
    tri_rapide(T, 0, N-1)
    return T

N=1000
# %timeit T=f(N)    # [magic or shell command commented out]
# %timeit T=g(N)    # [magic or shell command commented out]

T=g(N)
print(T)

# ---- Markdown cell 16 ----
# # Fonctions natives de tri d'une liste 
# * Que fait la fonction `sorted` fournie par python et la fonction membre `sort` ?
# * Etudier de même les temps de calcul

# ---- Code cell 17 ----
def h(N):
    T = [_ for _ in range(N, 0, -1)]
    return sorted(T)

N=1000
# %timeit h(N)    # [magic or shell command commented out]
U=h(N)
print(U)

# ---- Code cell 18 ----
help(T.sort)

# ---- Code cell 19 ----
N=1000
T = [_ for _ in range(N, -N-1, -1)]
T.sort(key=lambda x: x*x)   # une fonction lambda est une fonction s'écrivant en une seule ligne.
print(T)

