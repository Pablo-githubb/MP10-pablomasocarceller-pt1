from model import Productes


class Linia:
    quantitat = 1
    producte = None
    total = 0

    def __init__(self, quantitat, productes, total):
        self.quantitat = quantitat
        self.productes = productes
        self.total = total

    def get_a(self):
        return self.__a

    def set_a(self, a):
        self.__a = a


class Comandes:
    linia = []
    id_comanda = 0
    isEnviada = False

    def __init__(self, id_comanda, linia: list[Linia], isEnviada):
        self.id_comanda = id_comanda
        self.linia = linia
        self.isEnviada = isEnviada
