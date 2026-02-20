from gestio_erp.model.clients import Clients
from gestio_erp.model.comanda import Comanda, Linia


def crear_comanda(id_comanda: int, estat: str, client: Clients):
    nova_comanda = Comanda(id_comanda, [], estat)
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
        print(f"Comanda {comanda.id_comanda} [{comanda.estat}]: {comanda.linia}\n")


def modificar_estat_comanda(estat: str, comanda: Comanda) -> bool:
    # Gestió d'errors None
    if comanda is None:
        return False

    # Gestió d'errors per si l'estat s'escriu en majúscules
    if estat.lower() == "enviada":
        comanda.estat = "Enviada"

    return True


def afegir_producte(comanda : Comanda, nou_producte, quantitat_producte : int):
    # Gestió d'errors None
    if nou_producte is None:
        raise ValueError(f"El nou producte {nou_producte} no pot ser null")

    # Gestió d'error per si el producte ja existeix a la comanda
    for l in comanda.linia:
        if l.producte == nou_producte:
            raise ValueError(f"El producte {nou_producte} ja existeix a la comanda")

    # Creem nova línia i l'afegim
    nova_linia = Linia(producte=nou_producte, quantitat=quantitat_producte, total=quantitat_producte)
    comanda.linia.append(nova_linia)


def modificar_quantitat(id_comanda : Comanda, producte : Linia, nova_quantiat: int):
    # Gestió d'errors per quanitat incorrecta
    if not isinstance(nova_quantiat, int):
        raise ValueError("La quantitat introduïda es incorrecta, s'espera un enter.")
    # Gestió d'error per línia None
    if producte is None:
        raise ValueError("El producte no pot ser null")
    producte.quantitat = nova_quantiat
    producte.total = nova_quantiat
