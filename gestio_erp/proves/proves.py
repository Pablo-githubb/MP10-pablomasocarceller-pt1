from gestio_erp.controller import comandes_controller
from gestio_erp.controller.comandes_controller import crear_comanda
from gestio_erp.model.clients import Clients
from gestio_erp.model.productes import Productes


#TODO: Arreglar implementació de proves
def entorn_proves():
    print("COMANDES DELS CLIENTS\n")
    print("Comandes del client: Ana\n")
    crear_comanda()
    comandes_controller.llistar_comandes("")


