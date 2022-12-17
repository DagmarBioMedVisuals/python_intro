class Speler:
    def __init__(self, id, xp=0, attack=1, hp=10):
        self.id = id
        self.xp = xp
        self.attack = attack
        self.max_hp = hp
        self.current_hp = hp
        