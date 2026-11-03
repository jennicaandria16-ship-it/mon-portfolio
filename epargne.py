class CompteBancaire:
    def __init__ (self, nom, solde ):
        self.nom =nom
        self.solde =solde

    def afficher_solde(self) :
        print("nom :", self.nom)
        print("solde  :", self.solde ,"Ar")

class CompteEpargne(CompteBancaire):
    def __init__(self, nom, solde, taux_interet):
        super().__init__(nom, solde)
        self.taux_interet =taux_interet

    def afficher_solde(self):
         super().afficher_solde()
         print("taux_interet :", self.taux_interet, "%")


Compte1 =CompteEpargne("Miora", "500000", "5" )
Compte1.afficher_solde()


    