class Guerrier:
    def __init__(self, nom, vie, force, arme):
        self.nom = nom
        self.vie = vie
        self.force = force
        self.arme = arme
        self.defense = 5

    def attaquer(self):
        print(f"{self.nom} attaque avec {self.arme} !")

    def defendre(self):
        print(f"{self.nom} se défend et réduit les dégâts.")

    def utiliser_potion(self):
        print(f"{self.nom} utilise une potion pour restaurer sa vie.")

    def fuir(self):
        print(f"{self.nom} fuit le combat.")