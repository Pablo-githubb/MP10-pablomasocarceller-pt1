from model.Clients import Clients
from model.Productes import Productes


def entorn_proves():
    productes = Productes()
    print(productes)

    clients = Clients(1, "Pablo", "pablomaso@iesebre.com")
    print(clients)

if __name__ == "__main__":
    entorn_proves()