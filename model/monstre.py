import random

class Monstre:
    def __init__(self, nom="Monstre", monster=0, monster_atk_value=0):
        self.nom = nom
        self.monster = monster
        self.monster_atk_value = monster_atk_value

    @classmethod
    def generate_monstre(cls, monster, min_val_atk, max_val_atk):
        return cls(
            nom = "Monstre",
            monster = monster,
            monster_atk_value = random.randint(min_val_atk, max_val_atk)
        )

    @classmethod
    def monstre_lvl1(cls):
        return cls.generate_monstre(130, 50, 100)

    @classmethod
    def monstre_lvl2(cls):
        return cls.generate_monstre(150, 15, 25)

    @classmethod
    def monstre_lvl3(cls):
        return cls.generate_monstre(170, 15, 25)

    def est_vivant(self):
        return self.monster > 0

    def monster_atac(self, joueur):
        degats = self.monster_atk_value  
        joueur.player_l -= degats  
        return degats