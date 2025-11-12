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

