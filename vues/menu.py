from model.joueur import Joueur
from model.monstre import Monstre

class MenuGame:

    def afficher_reglement(self):
        print("""  
        
                 ***Regle du jeux***

Vous vous battez contre un monstre. Vous avez trois caractheristiques : ( donnés aleatoirement en debut de partis ) 

    - Agilité : permet de fuir l'enemie plus facilement.
    - Force : permet d'ataquer l'enemie plus fort
    - Chance : permet d'obtenir plus de point de vie avec les potions

    Le but est de mettre l'aversaire en dessous de 1 point de vie si vous le faites vous gagnez, dans le cas contraire vous perdez.
     Conseils : 
     1. établissez une stratégie suivant les caractheristiques de départs 
     2. lorsque vous n'avez plus de potions vous pouvez lancer une piece sur pile ou face et avoir la chance d'en gagner de nouvelles """)   
        print("-" * 50)

    def afficher_menu(self):
        print("Choisissez le niveau de la partie :\n")
        print("1. Niveau 1\n")
        print("2. Niveau 2\n")
        print("3. Niveau 3\n")
        return self.saisir_choix()

    def saisir_choix(self):
        return input("\nVotre choix : ")

    def afficher_joueur(self, joueur):
        print("Joueur :")
        print("Points de vie :", joueur.player_l)
        print("Potions :", joueur.potions)
        print("Agilité :", joueur.agilite)
        print("Force :", joueur.force)
        print("Chance :", joueur.chance)
    
    def afficher_monstre(self, monster):
        print("\nMonstre :")
        print("Points de vie :", monster.monster)

    def choix_invalide(self):
        print("\nChoix invalide. Veuillez réessayer.\n")

    def afficher_options_joueur(self):
        print("\nChoisissez une action :")
        print("1. Attaquer")
        print("2. Boire une potion")
        print("3. Fuir")
        return self.saisir_choix()
    
    def apres_atac(self, attaquant, cible, degats):
        points_de_vie_restants = 0
        if attaquant == "joueur":
            print("\nLe joueur a attaqué le monstre !\n")
        elif attaquant == "monstre":
            print("\nLe monstre a attaqué le joueur !\n")

        if cible == "joueur":
            points_de_vie_restants = cible.player_l
        elif cible == "monstre":
            points_de_vie_restants = cible.monster

        print(f"\nPoints de vie perdus par {cible.nom}: {degats}\n")
    
    def afficher_potion_utilisee(self, points_recuperes):
        print(f"\nLe joueur boit une potion et récupère {points_recuperes} point(s) de vie.\n")
    
    def afficher_echec_fuite(self):
        print("\nVous n'arrivez pas à fuir !\n")
    
    def afficher_reussite_fuite(self):
        print("\nVous avez pris la fuite !\n")
    
    def afficher_resultat(self, joueur):
        if joueur.est_vivant():
            print("\nLe joueur a gagné !\n")
        else:
            print("\nLe monstre a gagné !\n")