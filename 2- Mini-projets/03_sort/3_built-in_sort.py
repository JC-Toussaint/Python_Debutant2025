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

