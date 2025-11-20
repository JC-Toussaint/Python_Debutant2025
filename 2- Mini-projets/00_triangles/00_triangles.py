# question 1

# question 2
def est_triangle(t):
    cotes = sorted(list(t))
    return cotes[0] + cotes[1] > cotes[2]

# question 3 rectangle et isocele

# question 4

# question 6 perimetre

# test rectangle
t1 = (1,1,5)
t2 = (5,3,4)
print("t1 est rectangle ? =>", est_rectangle(t1))
print("t2 est rectangle ? =>", est_rectangle(t2))

# test isocele
t1 = (1,4,5)
t2 = (5,4,4)
print("t1 est isocele ? =>", est_isocele(t1))
print("t2 est isocele ? =>", est_isocele(t2))

# test equilateral
t1 = (1,4,5)
t2 = (4,4,4)
print("t1 est equilateral ? =>", est_equilateral(t1))
print("t2 est equilateral ? =>", est_equilateral(t2))

print(analyse_triangle((3,4,5))) 

# question 5
print(analyse_triangle((3,4,5))) 
print(analyse_triangle((3,4,3))) 
print(analyse_triangle((3,3,3))) 
print(analyse_triangle((3,3,13))) 
