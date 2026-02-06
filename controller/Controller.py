import os
from time import sleep
from model import Clients, Comandes, Productes

def crear_personatge(self):
    os.system("clear")
    index = 0;
    nom = input("Introdueix el nom del personatge: ")
    for race in self.llista_productes:
        print(f"{index}.{race}")
        index += 1
    raca = int(input("Introdueix la raça: "))

    index = 0;
    for territory in self.llista_territori:
        print(f"{index}.{territory}")
        index += 1
    territori = int(input("Introdueix el territori del personatge: "))

    index = 0
    for caracteristica in self.llista_caracteristiques:
        print(f"{index}.{caracteristica}")
        index += 1
    caracteristiques = int(input("Introdueix les característiques del personatge: "))

    personatge = Personatge(nom, self.llista_productes[raca], self.llista_territori[territori],
                            self.llista_caracteristiques[caracteristiques])
    self.llista_clients.append(personatge)
    print("Personatge creat amb èxit.")
    sleep(2)


def modificar_comanda(self, nom=None, raca=None, territori=None, caracteristiques=None):
    if nom:
        self.nom = nom
    if raca:
        self.raca = raca
    if territori:
        self.territori = territori
    if caracteristiques:
        self.caracteristiques = caracteristiques


def __str__(self):
    return f"Nom: {self.nom}, Raça: {self.raca}, Territori: {self.territori}, Característiques: {self.caracteristiques}"





def modificar_personatge(self):
    os.system("clear")
    nom = input("Introdueix el nom del personatge a modificar: ")
    for personatge in self.llista_clients:
        if personatge.nom == nom:
            nou_nom = input("Introdueix el nou nom (deixa en blanc per no modificar): ")
            nova_raca = input("Introdueix la nova raça (deixa en blanc per no modificar): ")
            nou_territori = input("Introdueix el nou territori (deixa en blanc per no modificar): ")
            noves_caracteristiques = input("Introdueix les noves característiques (deixa en blanc per no modificar): ")
            personatge.modificar(nou_nom, nova_raca, nou_territori, noves_caracteristiques)
            print("Personatge modificat amb èxit.")
            sleep(2)
            return
    print("Personatge no trobat.")
    sleep(2)


def eliminar_personatge(self):
    os.system("clear")
    nom = input("Introdueix el nom del personatge a eliminar: ")
    for personatge in self.llista_clients:
        if personatge.nom == nom:
            confirmacio = input(f"Vols eliminar el personatge {nom}? (S/n): ")
            if confirmacio.lower() == "s":
                self.llista_clients.remove(personatge)
                print("Personatge eliminat amb èxit.")
                sleep(2)
            else:
                print("Lletra introduida no corresponent")
                sleep(2)
            return
    print("Personatge no trobat.")
    sleep(2)


def sortir(self):
    print("Sortint de l'aplicació.")
    exit()
