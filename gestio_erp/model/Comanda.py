class Linia:
    quantitat = 1
    producte = None
    total = 0

    def __init__(self, quantitat, producte, total):
        self.quantitat = quantitat
        self.producte = producte
        self.total = total


class Comanda:
    linia = []
    id_comanda = 0
    estat = "Pendent"

    def __init__(self, id_comanda, linia: list[Linia], estat):
        self.id_comanda = id_comanda
        self.linia = linia
        self.estat = estat
