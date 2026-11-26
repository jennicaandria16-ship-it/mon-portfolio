class Employe:
    def __init__(self, nom, salaire_base):
        self.nom = nom
        self.salaire_base  = salaire_base
        pass

    def calculer_salaire(self):
        return self.salaire_base

class Developpeur(Employe):
     def __init__(self,nom, salaire_base, prime_technique):
         super().__init__(nom, salaire_base)
         self.prime_technique = prime_technique

     def calculer_salaire(self):
         return  super().calculer_salaire() + self.prime_technique
        
class Commercial(Employe):
    def __init__(self,nom, salaire_base, commission):
        super().__init__(nom, salaire_base)
        self.commission = commission

    def calculer_salaire(self):
        return  super().calculer_salaire() + self.commission


developpeur1 = Developpeur("Luc", 1700000, 200000)
developpeur2 = Developpeur("Jean", 1600000, 250000)

commercial1 = Commercial("Zoe", 500000, 150000)
commercial2 = Commercial("Alie", 500000, 100000)

Employes = [developpeur1, developpeur2, commercial1, commercial2]

for employe in Employes:
    print("Employe: ", employe.nom)
    print("Salaire: ", employe.calculer_salaire(), "Ar")
    print()
    
