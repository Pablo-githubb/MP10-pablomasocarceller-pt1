from model import Comandes


class Clients:
    def __init__(self, id, nom, correu, llistat_comandes):
        self.id = id
        self.nom = nom
        self.correu = correu
        self.llistat_comandes = llistat_comandes

    def __str__(self):
        return f"id: {self.id}, nom: {self.nom}, correu: {self.correu}, comandes: {self.llista_comandes}"
