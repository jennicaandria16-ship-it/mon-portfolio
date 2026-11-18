class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

class commande:
    def __init__(self, produit, quantite ):
        self.produit = produit
        self.quantite = quantite

    def calculer_total(self):
         return self.produit.prix * self.quantite

    def afficher_commande(self):
        print("Nom du produit :", self.produit.nom)
        print("Quantite :" ,self.quantite)
        print("Montant total :", self.calculer_total(), "Ar")
        print("Total : ", commande.calculer_total(), "Ar")

produit = Produit("Sac", 50000)
commande = commande(produit, 3)

commande.afficher_commande()

