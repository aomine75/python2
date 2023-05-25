from guerrier import Guerrier
from tireur import Tireur
from constructeur import Constructeur

def main():
   
    guerrier = Guerrier("Guerrier", 100, 10, "Épée")
    tireur = Tireur("Tireur", 80, 8, "Arc")
    constructeur = Constructeur("Constructeur", 120, 6, "Marteau")

    guerrier.attaquer()
    guerrier.defendre()
    guerrier.utiliser_potion()
    guerrier.fuir()

    tireur.attaquer()
    tireur.viser()
    tireur.recharger()
    tireur.esquiver()

    constructeur.attaquer()
    constructeur.réparer()
    constructeur.renforcer()
    constructeur.améliorer()

if __name__ == "__main__":
    main()