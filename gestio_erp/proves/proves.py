from gestio_erp.controller import comandes_controller, clients_controller, producte_controller
from gestio_erp.model.clients import Clients
from gestio_erp.model.comanda import Comanda
from gestio_erp.model.productes import Productes


def entorn_proves():
    print("COMANDES DELS CLIENTS")

    # Crear clients
    anna = Clients("Anna", "Anna", "ana@gmail.com", [])
    pere = Clients("Pere", "Pere", "pere@gmail.com", [])
    joan = Clients("Joan", "Joan", "joan@gmail.com", [])

    # Crear productes
    bicicleta = Productes("bicicleta", 1)
    casc = Productes("casc", 2)
    guants = Productes("guants", 1)
    maillot = Productes("maillot", 1)
    roda = Productes("roda", 2)
    pantalons = Productes("pantalons", 1)

    # Crear comandes per Anna
    comanda_101 = comandes_controller.crear_comanda(101, "Pendent", anna)
    comandes_controller.afegir_producte(comanda_101, bicicleta, 1)
    comandes_controller.afegir_producte(comanda_101, casc, 2)

    comanda_102 = comandes_controller.crear_comanda(102, "Pendent", anna)
    comandes_controller.afegir_producte(comanda_102, guants, 1)

    # Crear comandes per Pere
    comanda_103 = comandes_controller.crear_comanda(103, "Pendent", pere)
    comandes_controller.afegir_producte(comanda_103, maillot, 1)
    comandes_controller.afegir_producte(comanda_103, roda, 2)

    comanda_104 = comandes_controller.crear_comanda(104, "Pendent", pere)
    comandes_controller.afegir_producte(comanda_104, guants, 2)

    # Llistar comandes per clients
    print(f"Comandes del client {anna}: {len(Comanda.linia)}")
    comandes_controller.llistar_comandes(anna)
    print(f"Comandes del client {pere}: {len(Comanda.linia)}")
    comandes_controller.llistar_comandes(pere)
    comandes_controller.llistar_comandes(joan)

    # Intentar afegir productes per comprovar errors
    comandes_controller.afegir_producte(comanda_101, bicicleta, 1)  # Ja existeix
    patinet = Productes("patinet", 1)
    producte_controller.llistar_productes(patinet)  # No existeix

    print("\nCOMANDES DELS CLIENTS")

    # Modificar quantitats de comanda 101 (Anna)
    comandes_controller.modificar_estat_comanda("Enviada", comanda_101)
    comandes_controller.modificar_quantitat(comanda_101, bicicleta.nom_producte, 2)
    comandes_controller.modificar_quantitat(comanda_101, casc.nom_producte, 4)
    comandes_controller.afegir_producte(comanda_101, pantalons, 1)

    # Llistat de comandes actualitzat per Anna
    print(f"Comandes del client {anna.nom}: {len(anna.llista_comandes)}")
    comandes_controller.llistar_comandes(anna)

    # Modificar quantitats de comanda 103 (Pere)
    comandes_controller.modificar_quantitat(comanda_103, maillot.nom_producte, 1)
    comandes_controller.modificar_quantitat(comanda_103, roda.nom_producte, 2)

    # Modificar quantitats de comanda 104 (Pere)
    comandes_controller.modificar_quantitat(comanda_104, guants.nom_producte, 2)

    # Llistat de comandes actualitzat per Pere
    print(f"Comandes del client {pere.nom}: {len(pere.llista_comandes)}")
    comandes_controller.llistar_comandes(pere)

    # Llistat de comandes per Joan
    comandes_controller.llistar_comandes(joan)