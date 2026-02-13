from gestio_erp.model.Clients import Clients
from gestio_erp.model.Comanda import Comanda, Linia


def crear_comanda(nova_comanda: Comanda, llista_comandes: Clients):
    if nova_comanda is None:
        return
    llista_comandes.add(nova_comanda)
    return llista_comandes


def modificar_estat_comanda(comanda: Comanda, estat: str) -> bool:
    if comanda is None:
        return False
    else:
        comanda.estat = "Enviada"
        return True


def afegir_producte(nou_producte, linia: Linia):
    if nou_producte is None:
        return
    linia.producte = nou_producte


def llistar_comandes(client: Clients, nom: Clients, c: Comanda):
    if not client:
        print(f"El client {nom} no te cap comanda.\n")

    #else:
    #    for comanda in client:
    #        print(f"Comanda {c.id_comanda} {c.estat} : {client.llista_comandes}")

#TODO: configurar modificar_quantitat
def modificar_quantitat():
