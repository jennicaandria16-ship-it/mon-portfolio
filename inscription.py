class Apprenant:
    def __init__(self, nom, identifiant, module):
        self.nom = nom
        self.identifiant = identifiant
        self.module = module
        self.modules =[]

    def inscrire(self, module):
        self.modules.append(module)

    def afficher_modules(self):
            print("nom :", self.nom)
            print("identifiant :", self.identifiant)
            print("Modules suivis :")
    
            for module in self.modules:
                print("-" , module.titre)

class Module:
    def __init__(self,titre, nombre_heures):
        self.titre = titre
        self.nombre_heures = nombre_heures

 
apprenant1 = Apprenant("Soa", 1093, 1)
apprenant2 = Apprenant("Mia", 1095, 2)

module1 = Module("Python " , 80)
module2 = Module("HTML" , 110)
module3 = Module("Reseau" , 50)


apprenant1.inscrire(module1)
apprenant1.inscrire(module2)
apprenant2.inscrire(module1)
apprenant2.inscrire(module3)


print("   APPRENANT1   ")
apprenant1.afficher_modules()

print("   APPRENANT2   ")
apprenant2.afficher_modules()

