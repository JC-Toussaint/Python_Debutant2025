# ---- Markdown cell 1 ----
# # Miniprojet "Triangles" - Version objet
# On s’intéresse dans ce miniprojet à déterminer les propriétés de triangles, mais en utilisant une approche objet.
# 
# Comme dans le premier miniprojet, les triangles seront définis par la longueur de leurs côtés et on supposera que ces longueurs sont des valeurs entières.
# 
# Les trois entiers décrivant le triangle ainsi que les différentes fonctions associées seront assemblés dans un objet `Triangle`.

# ---- Markdown cell 2 ----
# 1- Créez la classe Triangle ainsi que la fonction \__init__ permettant d'instancier des `Triangle`s. 
# 
# - les longueurs des cotés seront nommées a,b et c.
# - Faites en sorte que a soit forcément le plus grand coté et c le plus petit, quelque soient les paramètres entrés par l'utilisateur
# - testez votre classe en instanciant quelques `Triangle`s.

# ---- Code cell 3 ----
# question 1


t1 = Triangle (2,4,3)
print(t1.a, t1.b, t1.c)

# ---- Code cell 4 ----
help(sorted)

# ---- Markdown cell 5 ----
# 2- On vous rappelle le code de la fonction ‘est_triangle(t)’ de la version initiale du projet.
# 
# - Adaptez cette fonctionnalité pour en faire une méthode de votre classe `Triangle`.
# - Intégrez cette fonction à l'initialisation. L'objectif est qu'il soit impossible de créer une objet `Triangle` qui n'ait pas les propriétés d'un triangle.

# ---- Code cell 6 ----
# question 2

## version initiale de la fonction est_triangle
# def est_triangle(t):
#     cotes = sorted(list(t))
#     return cotes[0] + cotes[1] > cotes[2]

t1 = Triangle (2,4,3)
print(t1.a, t1.b, t1.c)
t1 = Triangle (2,6,3)
print(t1.a, t1.b, t1.c)

# ---- Markdown cell 7 ----
# 3- Recopiez votre classe Triangle et ajoutez-y les méthodes suivantes, qui permettent de vérifier les propriétés du triangle, en tant que méthode de la classe `Triangle`. Ces fonctions retourneront un booléen.
# 
# - 'est_rectangle()' permettant de vérifier si un triangle est un triangle rectangle
# - 'est_isocèle()' pour vérifier si le triangle est isocèle
# - 'est_equilateral()' pour vérifier si le triangle est équilatéral

# ---- Code cell 8 ----
# question 3


t1 = Triangle (2,4,3)
print(t1.est_rectangle(), t1.est_isocele(), t1.est_equilateral())
t1 = Triangle (5,4,3)
print(t1.est_rectangle(), t1.est_isocele(), t1.est_equilateral())
t1 = Triangle (2,6,6)
print(t1.est_rectangle(), t1.est_isocele(), t1.est_equilateral())
t1 = Triangle (4,4,4)
print(t1.est_rectangle(), t1.est_isocele(), t1.est_equilateral())

# ---- Markdown cell 9 ----
# 4- On veut à présent écrire une méthode donnant toutes les informations sur le triangle. 
# - La fonction retournera une chaine de caractères. (la fonction en elle-même n'imprime rien dans la console)
# - la chaine de caractère retournée sera de la forme 'Triangle dont les cotés sont de dimensions (8,6,6). Ce triangle est isocèle et équilatéral.'
# - la méthode sera nommée \__str__. Cherchez par vous-même ou auprès de l'enseignant la raison de ce choix de nom de méthode.

# ---- Code cell 10 ----

# ---- Markdown cell 11 ----
# 5- Testez la méthode produite à la question précédente sur quelques exemples

# ---- Code cell 12 ----
# question 5
t1 = Triangle (2,4,3)
print(t1)
t1 = Triangle (5,4,3)
print(t1)
t1 = Triangle (2,6,6)
print(t1)
t1 = Triangle (4,4,4)
print(t1)

# ---- Markdown cell 13 ----
# 6- Ecrivez les méthodes perimetre() et surface() qui retournent respectivement le périmètre et la surface du triangle.
# 
# Note : la surface d’un triangle peut se calculer selon : $S=\sqrt{d(d-a)(d-b)(d-c)}$, où a,b,c sont les cotés du triangle et d est le demi-périmètre.

# ---- Code cell 14 ----
# question 6
from math import sqrt

    
t1 = Triangle (2,4,3)
print(t1.surface())    

# ---- Markdown cell 15 ----
# 7- On souhaite pour finir protéger les propriétés (a,b,c) du triangle.
# 
# En effet, il est pour l'instant possible de créer un triangle puis de modifier l'un des cotés, ce qui rend ce triangle potentiellement erroné (par exemple, le calcul de la surface peut devenir invalide (racine d'un nombre négatif)). De plus, si l'utilisateur modifie l'un des cotés, l'ordre a>b>c ne sera plus assuré. De ce fait les méthodes telles que 'est_rectangle' ne fonctionneront plus correctement.
# 
# Pour remédier à ces problèmes, on peut remplacer a, b et c par des `@property`. Reprenez le code de votre classe Triangle et modifiez le pour sécuriser l'accès aux paramètres des cotés

# ---- Code cell 16 ----
# question 7 : exemple de code qui va poser problème

## exemple 1 : apres modification, le triangle devrait être rectangle
t1 = Triangle (3,4,1)
print(t1)
t1.c = 5
print(t1)
print('-'*40)

## exemple 2 : la modification "a=1" devrait être interdite car cela rend le triangle invalide
t1 = Triangle (2,4,5)
print(t1.surface())
t1.a = 1
print(t1)
print(t1.surface())

# ---- Code cell 17 ----
# question 7 : classe sécurisée
from math import sqrt

# ---- Code cell 18 ----
# question 7 : vérification classe sécurisée

## exemple 1 : apres modification, le triangle devrait être rectangle
t1 = Triangle (3,4,1)
print(t1)
t1.c = 5
print(t1)
print('-'*40)

## exemple 2 : la modification "a=1" devrait être interdite car cela rend le triangle invalide
t1 = Triangle (2,4,5)
print(t1.surface())
t1.a = 1
print(t1)
print(t1.surface())

