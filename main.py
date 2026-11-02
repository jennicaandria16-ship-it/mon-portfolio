
class Employe:
    def __init__ (self, nom , age):
        self.nom =nom
        self.age =age

    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans. ")

class Developpeur(Employe):
    def __init__ (self, nom, age, langage):
        super().__init__(nom, age)
        self.langage =langage

    def se_presenter(self):
         super().se_presenter()
         print(f"Mon Langage préféré est {self.langage}" )

developpeur1 = Developpeur("Soa" , 25 , "Python")
developpeur1.se_presenter()





        
    
        
        
