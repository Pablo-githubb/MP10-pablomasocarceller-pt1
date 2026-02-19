from gestio_erp.model.comanda import Comanda

class Clients:
    id_client = None
    nom = ""
    correu = ""
    llista_comandes = list[Comanda]

    def __init__(self, id_client, nom, correu, llista_comandes: list[Comanda]):
        self.id_client = id_client
        self.nom = nom
        self.correu = correu
        self.llista_comandes = llista_comandes
