from gestio_erp.model.clients import Clients
from gestio_erp.model.comanda import Comanda, Linia


def crear_client(nou_id: int, nou_nom: str, nou_correu: str, nova_llista: list[Comanda]):
    if not isinstance(nou_id, int):
        raise ValueError(f"El ID: {nou_id} introduït es incorrecte, s'espera un enter.")
    elif not isinstance(nou_nom, str):
        raise ValueError(f"El nom: {nou_nom} es incorrecte, s'espera un string.")
    elif not isinstance(nou_correu, str):
        raise ValueError(f"El correu:  {nou_correu} es incorrecte, s'espera un string.")
    elif not isinstance(nova_llista, list):
        raise ValueError("La llista proporcionada no és vàlida. S'espera una llista de la classe Comanda")
    nou_client = Clients(nou_id, nou_nom, nou_correu, nova_llista)
    return nou_client


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
