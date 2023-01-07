from random import randrange
from datetime import datetime

class Speler:
    def __init__(self, id, xp=0, attack=1, hp=10):
        self.id = id
        self.xp = xp
        self.attack = attack
        self.max_hp = hp
        self._current_hp = hp # '_' geeft aan dat dit een private property is (voor andere mensen)
        self._last_hp_update = datetime.now()
    
    @property 
    ## Behandel deze method alsof het een property is
    def current_hp(self): 
        nu = datetime.now()

        if self._current_hp < self.max_hp:
            gepasseerde_tijd = nu - self._last_hp_update

            # 1 / hp per 10 seconden
            hp_verandering = round(gepasseerde_tijd.total_seconds() * .1)
            self._current_hp += hp_verandering

            if self._current_hp > self.max_hp:
                self._current_hp > self.max_hp


        self._last_hp_update = nu
        return self._current_hp
    
    def val_aan(self):
        return self.attack + randrange(4)

    def ontvang_schade(self, schade):
        self._current_hp -= schade

        # ga niet lager dan 0
        if self._current_hp < 0:
            self._current_hp = 0

        self._last_hp_update = datetime.now()

# De speler geneest tussen gevechten

# 1. Laatste current_hp waarde
# 2. Laatste tijd dat current_hp was gebruikt (hoe lang geleden?)
# 3. Hoe snel verandert current_hp