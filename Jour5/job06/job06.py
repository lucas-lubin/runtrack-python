def distance_to_toilettes(marches, hauteur_marche):
    nombre_de_jours = 7
    nombre_de_descendre_et_remonter = 2  

    distance_marches = marches * hauteur_marche * nombre_de_descendre_et_remonter / 100  

    distance_semaine = distance_marches * nombre_de_jours

    return distance_semaine


nombre_marches = 50
hauteur_marche = 20  

distance_totale = distance_to_toilettes(nombre_marches, hauteur_marche)

print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_totale:.2f} m par semaine.")
