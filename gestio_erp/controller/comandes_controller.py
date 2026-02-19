from gestio_erp.model.clients import Clients
from gestio_erp.model.comanda import Comanda, Linia


def crear_comanda(nova_comanda: Comanda, client: Clients):
    if nova_comanda is None:
        return
    client.llista_comandes.append(nova_comanda)


def llistar_comandes(client: Clients):
    # Gestió d'errors None
    if client is None:
        print(f"Error: Client ({client}) no proporcionat.\n")
        return

    # Gestió d'errors sobre les comandes del client
    if not client.llista_comandes:
        print(f"El client {client.nom} no te cap comanda.\n")
        return

    for comanda in client.llista_comandes:
        print(f"Comanda {comanda.id_comanda} {comanda.estat} : {comanda.linia}")


def modificar_estat_comanda(comanda: Comanda) -> bool:
    # Gestió d'errors None
    if comanda is None:
        return False
    else:
        comanda.estat = "Enviada"
        return True


def afegir_producte(nou_producte, linia: Linia):
    # Gestió d'errors None
    if nou_producte is None:
        raise ValueError(f"El nou producte {nou_producte} no pot ser null")
    linia.producte = nou_producte


def modificar_quantitat(nova_quantiat: int, linia: Linia):
    # Gestió d'errors per quanitat incorrecta
    if not isinstance(nova_quantiat, int):
        raise ValueError("La quantitat introduïda es incorrecta, s'espera un enter.")
    #Gestió d'error per línia None
    if linia is None:
        raise ValueError("La lína no pot ser null")

    linia.quantitat = nova_quantiat
