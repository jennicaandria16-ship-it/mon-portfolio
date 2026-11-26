from abc import ABC, abstractmethod

class Forme(ABC):
    @abstractmethod
    def calculer_surface(self):
         pass
    
class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calculer_surface(self):
        return self.longueur * self.largeur

class Carre(Forme):
    def __init__(self, cote):
        self.cote = cote

    def calculer_surface(self):
        return self.cote * self.cote

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_surface(self):
        return 3.14 *self.rayon*self.rayon

rectangle1 = Rectangle(5,6)
carre1 = Carre(4)
cercle1 = Cercle(5)

Formes = [rectangle1, carre1, cercle1]

for forme in Formes:
    print( forme.calculer_surface())

          
