def tri_a_bulles(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def arrondir_et_trier_liste(liste):
    liste_arrondie = []
    
    for nombre in liste:
        
        nombre_arrondi = int(nombre + 0.5)
        liste_arrondie.append(nombre_arrondi)

    
    tri_a_bulles(liste_arrondie)

    return liste_arrondie


liste_initiale = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]


liste_arrondie_et_triee = arrondir_et_trier_liste(liste_initiale)
print("Liste arrondie et triée :", liste_arrondie_et_triee)
