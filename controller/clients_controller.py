def afegirComanda(self, nova_comanda: Comandes):
    if nova_comanda is None:
        return
    self.llista_comandes.append(nova_comanda)
    return self.llista_comandes


def llistar_comandes(self):
    if not self.llistat_comandes:
        print(f"El client {self.nom} no te cap comanda.\n")

    else:
        for comanda in self.llistat_comandes:
            print(f"Comanda {comanda.id_comanda} {comanda.estat_comanda} : {comanda.llista_comandes[0]}")