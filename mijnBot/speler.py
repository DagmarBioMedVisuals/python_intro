from random import randrange

class Speler:
    def __init__(self, id, xp=0, attack=1, hp=10):
        self.id = id
        self.xp = xp
        self.attack = attack
        self.max_hp = hp
        self.current_hp = hp
    
    def attack(self):
        return self.attack + randrange(4)

    def take_damage(self, damage):
        self.hp -= damage