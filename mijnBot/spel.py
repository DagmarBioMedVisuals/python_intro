from speler import Speler
from gevecht import Gevecht, Resultaat

class Spel:
    def __init__(self):
        self.spelers = {}
        self.gevechten = {}

    def get_speler(self, speler_id):
        speler = self.spelers.get(speler_id) # if not found, return None

        # speler = self.spelers[speler_id] # if not found, throw an error
        if speler: # als er al een speler bestaat
            return speler # stuur speler info terug
        else: # anders, maak een nieuwe speler
            self.spelers[speler_id] = Speler(speler_id, 0, 2, 10)
            return self.spelers[speler_id]

    def maak_gevecht(self, speler_id):
        gevecht = self.gevechten.get(speler_id) # check of de speler al een gevecht heeft

        if gevecht:
            return "Gevecht is al bezig"
        else:
            speler = self.get_speler(speler_id) # maak een nieuwe speler
            self.gevechten[speler_id] = Gevecht(speler)
            return "Gevecht begonnen!"
    
    def attack(self, speler_id):
        gevecht = self.gevechten.get(speler_id)

        if gevecht is None:
            # start nieuw gevecht
            speler = self.get_speler(speler_id)
            gevecht = Gevecht(speler)
            self.gevechten[speler_id] = gevecht

        # ga door met de aanval
        resultaat = gevecht.speler_attack()

        # 2 mogelijke uitkomsten
        
        if resultaat.resultaat == Resultaat.CONTINUE:
            # 1. het gevecht gaat door (Resultaat.CONTINUES)
            self.gevechten[speler_id] = gevecht
            self.spelers[speler_id] = gevecht.speler
        else: 
            # 2. het gevecht is over (de speler is dood of het monster) (Resultaat.WIN of Resultaat.LOSE)
            del self.gevechten[speler_id] # verwijder item uit gevechten dictionary
        
        return resultaat.tekst