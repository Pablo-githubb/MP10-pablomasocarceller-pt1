from model import Comandes


class Clients:
    id_client = None
    nom = ""
    correu = ""
    llista_comandes = list[Comandes]

    def __init__(self, id_client, nom, correu, llista_comandes: list[Comandes]):
        self.id_client = id_client
        self.nom = nom
        self.correu = correu
        self.llista_comandes = llista_comandes
