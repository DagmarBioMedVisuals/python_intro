from speler import Speler
from monster import Monster
from enum import Enum

class Resultaat(Enum):
    CONTINUE=1
    WIN=2
    LOSE=3

class AanvalResultaat:
    def __init__(self, resultaat: Resultaat, tekst: str):
        self.resultaat = resultaat
        self.tekst = tekst

class Gevecht:
    def __init__(self, speler: Speler):
        self.monster = Monster()
        self.speler = speler

    def speler_attack(self):
        # speler valt aan
        schade = self.speler.attack()
        self.monster.ontvang_schade(schade)
        
        # check of monster nog leeft (hp > 0)
        if(self.monster.hp > 0):
            # als het nog leeft, ontvangt het schade en valt het aan
            monster_schade = self.monster.attack()
            self.speler.ontvang_schade(monster_schade)
            # check dan of de speler nog leeft en hoeveel schade ontvangt
            if(self.speler.hp > 0):
                #continue
                return AanvalResultaat(Resultaat.CONTINUE, f"Speler viel aan voor {schade}. Monster viel aan voor {monster_schade}. (-_-)")
            else:
                # speler verliest
                return AanvalResultaat(Resultaat.LOSE, f"Speler viel aan voor {schade}. Monster viel aan voor {monster_schade}. De speler is dood. ಠ_ಠ")
        else:
            return AanvalResultaat(Resultaat.WIN, f"Speler viel aan voor {schade}. Het monster is verslagen. o(*°▽°*)o")
        