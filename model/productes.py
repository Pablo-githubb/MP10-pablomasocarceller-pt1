class Productes:
    def __init__(self):
        self.llista_clients = ['Anna', 'Pere', 'Joan']
        self.llista_productes = ['bicileta', 'casc', 'guants', 'maillot,', 'roda']


    def __str__(self):
        return f"{self.llista_clients}\n{self.llista_productes}"

productes = Productes()
print(productes)