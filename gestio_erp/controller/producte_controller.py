from gestio_erp.model.comanda import Linia
from gestio_erp.model.productes import Productes


def crear_producte(nou_producte: str, preu: float, productes: Productes):
    if not isinstance(nou_producte, str):
        raise ValueError("El nou producte es incorrecte, s'espera un string.")
    productes.productes.append(nou_producte, preu)


# Llista els productes existents
def llistar_productes(buscador: Linia):
    producte_trobat = False
    productes = Productes
    for p in productes.productes:
        if buscador.producte == p.nom_producte:  # Busca si el producte que hem escollit existeix dintre de la llista o no. Sino, mostra un missatge d'error
            producte_trobat = True
            break
    if not producte_trobat:
        raise ValueError(f"El producte {buscador.producte} no existeix a la comanda")

    return productes.productes