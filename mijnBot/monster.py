from random import randrange

class Monster:
    def __init__(self, xp=0, attack=1, hp=5):
        self.xp = xp
        self.attack = attack
        self.hp = hp
    
    def val_aan(self):
        return self.attack + randrange(2)

    def ontvang_schade(self, schade):
        self.hp -= schade