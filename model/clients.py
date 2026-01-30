from model import comandes

class Clients:
   def __init__(self, id, nom, correu):
       self.id = id
       self.nom = nom
       self.correu = correu
       c = comandes(self.num_comandes)
       self.llista_comandes = c

