class Module:
    def __init__(self, titre, duree):
        self.titre = titre
        self.duree = duree


class Formation:
    def __init__(self, intitule):
        self.intitule = intitule
        self.liste_de_modules = []

    def ajouter_module(self, module):
        self.liste_de_modules.append(module)
        

class Apprenant:
    def __init__(self, nom):
        self.nom = nom
        self.formations = []

    def s_inscrire(self, formation):
        self.formations.append(formation)

    
    def afficher_parcours(self):
        print(f"Parcours de {self.nom} : ")
        for formation in self.formations:
            print(f"    -{formation.intitule}")
            for module in formation.liste_de_modules:
                print(f"    .{module.titre}  ({module.duree} h)")

module1 = Module("Python", 20)
module2 = Module("HTML", 15)
module3 = Module("CSS", 16)
module4 = Module("Java", 13)

formation1 = Formation("Full Stack 1")
formation2 = Formation("Full Stack 2")

formation1.ajouter_module(module1)
formation1.ajouter_module(module2)
formation1.ajouter_module(module3)


apprenant1 = Apprenant("Soa")
apprenant2 = Apprenant("Mia")


apprenant1.s_inscrire(formation1)
apprenant1.s_inscrire(formation2)
apprenant2.s_inscrire(formation2)

apprenant1.afficher_parcours()
apprenant2.afficher_parcours()
