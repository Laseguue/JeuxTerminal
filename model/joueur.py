import random

class Joueur:
    def __init__(self):
        self.nom = "Joueur"
        self.player_l = 0
        self.potions = 0
        self.agilite = 0
        self.force = 0
        self.chance = 0
        self.potion_value = 0
        self.atk_value = 0


    def joueur_lvl1(self):
        self.player_l = 150
        self.potions = 3
        self.agilite = self.generate_carac_lvl1()
        self.force = self.generate_carac_lvl1()
        self.chance = self.generate_carac_lvl1()
        self.potion_value = random.randint(20, 30)
        self.atk_value = random.randint(15, 25)
        return self

    def joueur_lvl2(self):
        self.player_l = 200
        self.potions = 5
        self.agilite = self.generate_carac_lvl2()
        self.force = self.generate_carac_lvl2()
        self.chance = self.generate_carac_lvl2()
        self.potion_value = random.randint(30, 40)
        self.atk_value = random.randint(20, 30)
        return self

    def joueur_lvl3(self):
        self.player_l = 250
        self.potions = 7
        self.agilite = self.generate_carac_lvl3()
        self.force = self.generate_carac_lvl3()
        self.chance = self.generate_carac_lvl3()
        self.potion_value = random.randint(40, 50)
        self.atk_value = random.randint(25, 35)
        return self

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