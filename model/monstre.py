import random

class Monstre:
    def __init__(self, nom="Monstre", monster=0, monster_atk_value=0):
        self.nom = nom
        self.monster = monster
        self.monster_atk_value = monster_atk_value

    @classmethod
    def monstre_lvl1(cls):
        return cls(
            nom = "Monstre",
            monster = 130,
            monster_atk_value = random.randint(50, 100)
        )

    @classmethod
    def monstre_lvl2(cls):
        return cls(
            nom = "Monstre",
            monster = 150,
            monster_atk_value = random.randint(15, 25)
        )

    @classmethod
    def monstre_lvl3(cls):
        return cls(
            nom = "Monstre",
            monster = 170,
            monster_atk_value = random.randint(15, 25)
        )

    def est_vivant(self):
        return self.monster > 0

    def monster_atac(self, joueur):
        degats = self.monster_atk_value  
        joueur.player_l -= degats  
        return degats