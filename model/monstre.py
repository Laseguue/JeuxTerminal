import random

class Monstre:
    def __init__(self):
        self.nom = "Monstre"
        self.monster = 0
        self.monster_atk_value = 0

    def monstre_lvl1(self):
        self.monster = 130
        self.monster_atk_value = random.randint(50, 100)
        return self

    def monstre_lvl2(self):
        self.monster = 130
        self.monster_atk_value = random.randint(15, 25)
        return self

    def monstre_lvl3(self):
        self.monster = 130
        self.monster_atk_value = random.randint(15, 25)
        return self

    def est_vivant(self):
        return self.monster > 0

    def monster_atac(self, joueur):
        degats = self.monster_atk_value  
        joueur.player_l -= degats  
        return degats