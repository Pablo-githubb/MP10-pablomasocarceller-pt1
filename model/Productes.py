class Productes:
    def __init__(self, nom_producte):
        self.nom_producte = nom_producte
        self.llistat_productes = []


    def llistarProductes(self):
        return self.llistat_productes


    def afegirProducte(self, nou_producte):
        self.llistat_productes.append(nou_producte)

