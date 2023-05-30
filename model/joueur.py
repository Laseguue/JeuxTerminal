import random

class Joueur:
    def __init__(self, nom="Joueur", player_l=0, potions=0, agilite=0, force=0, chance=0, potion_value=0, atk_value=0):
        self.nom = nom
        self.player_l = player_l
        self.potions = potions
        self.agilite = agilite
        self.force = force
        self.chance = chance
        self.potion_value = potion_value
        self.atk_value = atk_value

    @classmethod
    def generate_carac(cls, min_val, max_val):
        return random.randint(min_val, max_val)

    @classmethod
    def generate_joueur(cls, lvl, player_l, potions, min_val_carac, max_val_carac, min_val_potion, max_val_potion, min_val_atk, max_val_atk):
        return cls(
            player_l = player_l,
            potions = potions,
            agilite = cls.generate_carac(min_val_carac, max_val_carac),
            force = cls.generate_carac(min_val_carac, max_val_carac),
            chance = cls.generate_carac(min_val_carac, max_val_carac),
            potion_value = random.randint(min_val_potion, max_val_potion),
            atk_value = random.randint(min_val_atk, max_val_atk)
        )

    @classmethod
    def joueur_lvl1(cls):
        return cls.generate_joueur(1, 150, 3, 50, 100, 20, 30, 15, 25)

    @classmethod
    def joueur_lvl2(cls):
        return cls.generate_joueur(2, 200, 5, 70, 120, 30, 40, 20, 30)

    @classmethod
    def joueur_lvl3(cls):
        return cls.generate_joueur(3, 250, 7, 80, 140, 40, 50, 25, 35)

    def est_vivant(self):
        return self.player_l > 0

    @staticmethod
    def generate_carac_lvl1():
        return random.randint(50, 100)

    @staticmethod
    def generate_carac_lvl2():
        return random.randint(70, 120)

    @staticmethod
    def generate_carac_lvl3():
        return random.randint(80, 140)

    def joueur_atac(self, monster):
        atk_value = self.atk_value
        if self.force < 50:
            degats = atk_value
        elif self.force >= 50 and self.force < 75:
            degats = atk_value * 1.2
        else:  
            degats = atk_value * 1.4
        monster.monster -= degats
        return degats

    def prendre_potion(self):
        if self.potions > 0:
            if self.chance < 50:
                self.player_l += self.potion_value
            elif self.chance >= 50 and self.chance < 75:
                self.player_l += self.potion_value * 1.2
            else:  
                self.player_l += self.potion_value * 1.4
            self.potions -= 1
        else:  
            piece = random.randint(1, 2)
            if piece == 1 and self.chance < 50:
                self.potions += 1
            elif piece == 1 and self.chance >= 50:
                self.potions += 2

    def fuir(self):
        if self.agilite < 50:
            fuite = random.randint(1, 4)
            if fuite == 1:
                return True
        elif self.agilite >= 50 and self.agilite < 80:
            fuite = random.randint(1,3)
            if fuite == 1:
                return True
        else:  
            fuite = random.randint(1,2)
            if fuite == 1:
                return True
        return False