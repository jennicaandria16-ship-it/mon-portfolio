class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

    def afficher_details():
       print("Titre :", self.titre)
       print("Auteur :", self.auteur)
       print("Annee:", self.annee)


class Bibliothèque:
    def __init__(self):
        self.livres = [livre1, livre2, livre3] 

    def ajouter_livre(self, livre):
        self.livre

    def afficher_catalogue(self):
        for livre in self.livres:
            livre.afficher_details()

    

    livre1 = Livre("L'Etranger", "Albert Camus" , 1942)
    livre2 = Livre("La métamorphose", "Franz Kafka" ,1915)
    livre3 = Livre("Matin brun", "Franck Pavloff" , 1998)

    bibliothèque = Bibliothèque()

    bibliothèque.ajouter_livre(livre1)
    bibliothèque.ajouter_livre(livre2)
    bibliothèque.ajouter_livre(livre3)
          
    bibliothèque.afficher_catalogue()
        