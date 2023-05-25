class Tireur:
    def __init__(self, nom, vie, force, arme):
        self.nom = nom
        self.vie = vie
        self.force = force
        self.arme = arme
        self.precision = 90

    def attaquer(self):
        print(f"{self.nom} tire avec précision à l'aide de son {self.arme} !")

    def viser(self):
        print(f"{self.nom} vise attentivement pour maximiser sa précision.")

    def recharger(self):
        print(f"{self.nom} recharge son arme pour ne pas manquer de munitions.")

    def esquiver(self):
        print(f"{self.nom} esquive habilement les attaques adverses.")