def afficher_tables_multiplication(n):
    for i in range(1, n + 1):
        print("\nTable de multiplication de", i, ":\n")
        for j in range(1, 11):
            resultat = i * j
            print(i, "x", j, "=", resultat)


while True:
    try:
        N = int(input("Veuillez entrer un entier N supérieur à zéro : "))
        if N > 0:
            break
        else:
            print("Veuillez entrer un entier supérieur à zéro.")
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")


afficher_tables_multiplication(N)