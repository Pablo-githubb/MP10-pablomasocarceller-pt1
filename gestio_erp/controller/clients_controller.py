from gestio_erp.model.clients import Clients
from gestio_erp.model.comanda import Comanda, Linia


def crear_client(nom: str, id_client,  correu: str, llista: list[Comanda]):
    if not isinstance(id_client, int):
        raise ValueError(f"El ID: {id_client} introduït es incorrecte, s'espera un enter.")
    elif not isinstance(nom, str):
        raise ValueError(f"El nom: {nom} es incorrecte, s'espera un string.")
    elif not isinstance(correu, str):
        raise ValueError(f"El correu:  {correu} es incorrecte, s'espera un string.")
    elif not isinstance(llista, list):
        raise ValueError("La llista proporcionada no és vàlida. S'espera una llista de la classe Comanda")
    nou_client = Clients(id_client, nom, correu, llista)
    return nou_client

#No s'ha fet servir
def afegir_comanda(id_comanda: int, linia: list[Linia], estat: str):
    if not isinstance(linia, list):
        raise ValueError("La línia proporcionada no és vàlida. S'espera una llista d'objectes Linia.")
    elif not isinstance(id_comanda, int):
        raise ValueError(f"El id introduït: {id_comanda}, no es vàlid")
    elif not isinstance(estat, str):
        raise ValueError(f"L'estat es incorrecte")
    nova_comanda = Comanda(id_comanda, linia, estat)
    return nova_comanda


def total_comanda(total: Linia):
    return total.total
