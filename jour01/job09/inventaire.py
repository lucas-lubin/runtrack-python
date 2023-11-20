nom_produit = "Wopper"
prix_unitaire = 10.0
quantite_en_stock = 900


print("Informations du produit :")
print("Nom du produit :", nom_produit)
print("Prix unitaire :", prix_unitaire)
print("Quantité en stock :", quantite_en_stock)


quantite_achetee = int(input("Entrez la quantité de produits que tu souhaites acheter : "))
quantite_en_stock += quantite_achetee


prix_unitaire *= 1.1


print("\nInformations du produit après mise à jour :")
print("Nom du produit :", nom_produit)
print("Nouveau prix unitaire (après inflation de 10%) :", prix_unitaire)
print("Nouvelle quantité en stock :", quantite_en_stock)