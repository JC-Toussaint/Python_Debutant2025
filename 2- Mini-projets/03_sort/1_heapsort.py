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

