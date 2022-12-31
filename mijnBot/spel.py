from speler import Speler
from gevecht import Gevecht

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