class Productes:
    nom_producte = ""
    preu = 0.0
    productes = ['bicicleta', 'casc', 'guants', 'maillot', 'roda', 'pantalons']

    def __init__(self, nom_producte, preu, productes):
        self.nom_producte = nom_producte
        self.preu = preu
        self.productes = productes
