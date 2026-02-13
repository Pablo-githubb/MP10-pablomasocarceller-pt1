def llistarProductes(self):
    return self.llistat_productes


def afegirProducte(self, nou_producte):
    if nou_producte is None:
        return
    self.llistat_productes.append(nou_producte)
