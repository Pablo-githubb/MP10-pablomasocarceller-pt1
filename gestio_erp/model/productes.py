class Productes:
    nom_producte = ""
    preu = 0.0
    productes = []

    def __init__(self, nom_producte, preu, productes = None):
        self.nom_producte = nom_producte
        self.preu = preu
        self.productes = productes if productes is not None else []
