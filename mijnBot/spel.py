from speler import Speler

class Spel:
    def __init__(self):
        self.spelers = {}

    def get_speler(self, speler_id):
        speler = self.spelers.get(speler_id) # if not found, return None

        # speler = self.spelers[speler_id] # if not found, throw an error
        if speler: # als er al een speler bestaat
            return speler # stuur speler info terug
        else: # anders, maak een nieuwe speler
            self.spelers[speler_id] = Speler(speler_id, 0, 2, 10)
            return self.spelers[speler_id]