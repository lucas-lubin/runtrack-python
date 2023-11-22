def verifier_signe(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("nul")

verifier_signe(700)
verifier_signe(-10)
verifier_signe(60)
verifier_signe(-1)