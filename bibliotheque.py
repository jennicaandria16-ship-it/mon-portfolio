class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

    def afficher_details(self):
       print("Titre :", self.titre)
       print("Auteur :", self.auteur)
       print("Annee:", self.annee)

class Bibliotheque:
    def __init__(self):
        self.livres = [] 


    def ajouter_livre(self, livre):
            self.livres.append(livre)
    
    def afficher_catalogue(self):
         for livre in self.livres:
            livre.afficher_details()

livre1 = Livre("L'Etranger", "Albert Camus" , 1942)
livre2 = Livre("La métamorphose", "Franz Kafka" ,1915)
livre3 = Livre("Matin brun", "Franck Pavloff" , 1998)
    

bibliotheque = Bibliotheque()
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_livre(livre3)
          
bibliotheque.afficher_catalogue()
        