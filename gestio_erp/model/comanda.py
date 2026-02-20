class Linia:
    producte = None
    quantitat = 1
    total = 0

    def __init__(self, producte, quantitat, total):
        self.producte = producte
        self.quantitat = quantitat
        self.total = total

    def __repr__(self):
        return f"{self.producte}: {self.quantitat}"


class Comanda:
    linia = list[Linia]
    id_comanda = 0
    estat = "Pendent"

    def __init__(self, id_comanda, linia: list[Linia], estat):
        self.id_comanda = id_comanda
        self.linia = linia
        self.estat = estat
