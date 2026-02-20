class Productes:
    nom_producte = ""
    preu = 0.0
    productes = []

    def __init__(self, nom_producte, preu):
        self.nom_producte = nom_producte
        self.preu = preu
        Productes.productes.append(self)
