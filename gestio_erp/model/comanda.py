class Linia:
    producte = None
    quantitat = 1
    total = 0

    def __init__(self, quantitat, producte, total):
        self.quantitat = quantitat
        self.producte = producte
        self.total = total

    def __repr__(self):
        return f"{self.producte}: {self.quantitat}"


class Comanda:
    linia = []
    id_comanda = 0
    estat = "Pendent"

    def __init__(self, id_comanda, linia: list[Linia], estat):
        self.id_comanda = id_comanda
        self.linia = linia
        self.estat = estat
