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

