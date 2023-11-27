def tri_bulles(liste):
    n = len(liste)

    
    for i in range(n):
        
        for j in range(0, n-i-1):
         
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]


L = [64, 34, 25, 12, 22, 11, 90]


tri_bulles(L)


print("Liste triée :", L)
