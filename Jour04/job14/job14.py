def my_long_word(longueur_minimale, phrase):
    mots = []
    mot_actuel = ""
    resultat = ""

    for caractere in phrase:
        if caractere.isalpha():
            mot_actuel += caractere
        elif mot_actuel:
            if len(mot_actuel) > longueur_minimale:
                mots.append(mot_actuel)
            mot_actuel = ""


    if mot_actuel and len(mot_actuel) > longueur_minimale:
        mots.append(mot_actuel)

    
    resultat = " ".join(mots)

    return resultat


longueur_minimale = 3
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"


resultat = my_long_word(longueur_minimale, phrase)
print("Output :", resultat)
