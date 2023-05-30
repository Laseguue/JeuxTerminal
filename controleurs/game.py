import sys
from model.joueur import Joueur
from model.monstre import Monstre
from vues.menu import MenuGame

class Game:
    def __init__(self):
        self.joueur = None
        self.monster = None
        self.menu = MenuGame()

    def run(self):
        self.menu.afficher_reglement()
        choix = self.menu.afficher_menu()
        self.setup_partie(choix)
        self.commencer_partie()
        self.menu.afficher_resultat(self.joueur)

    def setup_partie(self, choix):
        if choix == "1":
            self.joueur = Joueur.joueur_lvl1()
            self.monster = Monstre.monstre_lvl1()
        elif choix == "2":
            self.joueur = Joueur.joueur_lvl2()
            self.monster = Monstre.monstre_lvl1()
        elif choix == "3":
            self.joueur = Joueur.joueur_lvl3()
            self.monster = Monstre.monstre_lvl1()
        
        self.menu.afficher_joueur(self.joueur)
        self.menu.afficher_monstre(self.monster)

    def commencer_partie(self):
        while self.joueur.est_vivant() and self.monster.est_vivant():
            self.jouer_tour_joueur()
            if not self.monster.est_vivant():
                break
            self.jouer_tour_monstre()

    def jouer_tour_joueur(self):
        print("Tour du joueur \n")
        choix = self.menu.afficher_options_joueur()
        if choix == "1":
            degats = self.joueur.joueur_atac(self.monster)
            self.menu.apres_atac("joueur", self.monster, degats)
        elif choix == "2":
            self.joueur.prendre_potion()
            self.menu.afficher_potion_utilisee(self.joueur.potion_value)
        elif choix == "3":
            if self.joueur.fuir():
                self.menu.afficher_reussite_fuite()
                sys.exit()

        self.menu.afficher_joueur(self.joueur)
        self.menu.afficher_monstre(self.monster)

    def jouer_tour_monstre(self):
        print("Tour du monstre \n")
        degats = self.monster.monster_atac(self.joueur)
        self.menu.apres_atac("monstre", self.joueur, degats)

        self.menu.afficher_joueur(self.joueur)
        self.menu.afficher_monstre(self.monster)