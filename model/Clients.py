class Clients:

    def __init__(self, id_client, nom, correu):
        self.id_client = id_client
        self.nom = nom
        self.correu = correu
        self.llistat_comandes = []

    def afegirComanda(self, nova_comanda):
        self.llistat_comandes.append(nova_comanda)
        return self.llistat_comandes

    def llistar_comandes(self):
        if not self.llistat_comandes:
            print(f"El client {self.nom} no te cap comanda.\n")
            ##TODO: Acabar d'implementar el resultat
        # else:
        # for comanda in self.llistat_comandes:
        # print(f"Comanda {comanda.id_comanda} {comanda.estat_comanda} : {comanda.llista_comandes[0]}")
