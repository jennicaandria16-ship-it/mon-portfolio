class Moteur:
    def __init__(self, marque, puissance):
        self.marque = marque
        self.puissance = puissance

    def demarrer(self):
        print("Le moteur démarre")

class Voiture:
    def __init__(self, moteur ):
        self.moteur = moteur

    def demarrer(self):
        self.moteur.demarrer()
        
moteur1 = Moteur( "Toyota", 120)
voiture1 = Voiture(moteur1)
voiture1.demarrer()