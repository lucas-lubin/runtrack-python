def remplacer_element(liste, index):
    
    liste[index] = liste[index - 1] + liste[index + 1]

L = [1, 2, 3, 4, 5]


print("Deuxième valeur de la liste :", L[1])


remplacer_element(L, 3)


print("Tableau après la modification :", L)


print("Dernière valeur de la liste :", L[-1])
