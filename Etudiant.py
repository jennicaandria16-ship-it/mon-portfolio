class Formation:
    def __init__(self , intitule, duree):
        self.intitule = intitule
        self.duree = duree

class Etudiant:
    def __init__(self, nom, formation):
        self.nom = nom
        self.formation = formation 

    def afficher_information(self):
        print("Nom : " , self.nom)
        print("Formation :", self.formation.intitule)

formation = Formation("Developpement web" , 5 )

etudiant1 = Etudiant("Soa" ,formation)
etudiant2 = Etudiant("Niry" ,formation)

etudiant1.afficher_information()
etudiant2.afficher_information()


