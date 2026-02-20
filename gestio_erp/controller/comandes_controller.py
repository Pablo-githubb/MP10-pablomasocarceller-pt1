from gestio_erp.model.clients import Clients
from gestio_erp.model.comanda import Comanda, Linia
from gestio_erp.model.productes import Productes


def crear_comanda(id_comanda: int, estat: str, client: Clients):
    nova_comanda = Comanda(id_comanda, [], estat)
    # Gestó d'errors None
    if nova_comanda is None:
        return None
    client.llista_comandes.append(nova_comanda)
    return nova_comanda


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
        print(f"Comanda {comanda.id_comanda} [{comanda.estat}]: {comanda.linia}")


def modificar_estat_comanda(estat: str, comanda: Comanda) -> bool:
    # Gestió d'errors None
    if comanda is None:
        return False

    # Gestió d'errors per si l'estat s'escriu en majúscules
    if estat.lower() == "enviada":
        comanda.estat = "Enviada"

    return True


def afegir_producte(comanda: Comanda, nou_producte: str, quantitat_producte: int):
    # Gestió d'errors None
    if comanda is None:
        raise ValueError("La comanda no pot ser null")
    if nou_producte is None:
        raise ValueError(f"El nou producte {nou_producte} no pot ser null")

    # Gestió d'error per si el producte ja existeix a la comanda
    for l in comanda.linia:
        if l.producte == nou_producte:
            raise ValueError(f"El producte {nou_producte} ja existeix a la comanda")

    # Creem nova línia i l'afegim
    nova_linia = Linia(producte=nou_producte, quantitat=quantitat_producte, total=quantitat_producte)
    comanda.linia.append(nova_linia)


def modificar_quantitat(comanda: Comanda, nom_producte: str, nova_quantitat: int):
    # Gestió d'errors per quantitat incorrecta
    if not isinstance(nova_quantitat, int):
        raise ValueError("La quantitat introduïda es incorrecta, s'espera un enter.")

    # Gestió d'error per comanda None
    if comanda is None:
        raise ValueError("La comanda no pot ser null")

    # Buscar el producte a la comanda
    producte_trobat = False
    # Gestió d'errors fins que trobe el producte a modificar
    for linia in comanda.linia:
        if linia.producte == nom_producte:
            linia.quantitat = nova_quantitat
            linia.total = nova_quantitat
            producte_trobat = True
            break
    if not producte_trobat:
        raise ValueError(f"El producte {nom_producte} no existeix a la comanda")
