from gestio_erp.model.productes import Productes


def crear_producte(nou_producte: str, preu: float, productes: Productes):
    if not isinstance(nou_producte, str):
        raise ValueError("El nou producte es incorrecte, s'espera un string.")
    productes.productes.append(nou_producte, preu)


def llistar_productes(productes: Productes):
    return productes.productes
