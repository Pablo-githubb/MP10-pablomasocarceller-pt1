from gestio_erp.controller import comandes_controller, producte_controller, clients_controller
from gestio_erp.model.comanda import Linia
from gestio_erp.model.productes import Productes


def entorn_proves():
    print("COMANDES DELS CLIENTS")

    # Crear clients
    anna = clients_controller.crear_client("Anna", 10, "ana@gmail.com", [])
    pere = clients_controller.crear_client("Pere", 20, "pere@gmail.com", [])
    joan = clients_controller.crear_client("Joan", 30, "joan@gmail.com", [])

    # Crear comandes per Anna
    comanda_101 = comandes_controller.crear_comanda(101, "Pendent", anna)
    comandes_controller.afegir_producte(comanda_101, "bicicleta", 1)
    comandes_controller.afegir_producte(comanda_101, "casc", 2)

    comanda_102 = comandes_controller.crear_comanda(102, "Pendent", anna)
    comandes_controller.afegir_producte(comanda_102, "guants", 1)

    # Crear comandes per Pere
    comanda_103 = comandes_controller.crear_comanda(103, "Pendent", pere)
    comandes_controller.afegir_producte(comanda_103, "maillot", 1)
    comandes_controller.afegir_producte(comanda_103, "roda", 2)

    comanda_104 = comandes_controller.crear_comanda(104, "Pendent", pere)
    comandes_controller.afegir_producte(comanda_104, "guants", 2)

    # Llistar comandes per clients
    print(f"Comandes del client {anna.nom}: {len(anna.llista_comandes)}")
    comandes_controller.llistar_comandes(anna)
    print(f"Comandes del client {pere.nom}: {len(pere.llista_comandes)}")
    comandes_controller.llistar_comandes(pere)
    comandes_controller.llistar_comandes(joan)

    # Intentar afegir productes per comprovar errors
    try:
        comandes_controller.afegir_producte(comanda_101, "bicicleta", 1)  # Ja existeix
    except ValueError as e:
        print(f"Error: {e}")

    try:
        patinet = Linia("patinet", 1, 1)
        producte_controller.llistar_productes(patinet)  # No existeix
    # Tractament de AttributeError i ValueError per si la comanda s'inicialitza en None o amb un altre caràcter
    except (AttributeError, ValueError) as e:
        print(f"Error: {e}\n")

    print("COMANDES DELS CLIENTS")

    # Modificar quantitats de comandes 101 (Anna)
    comandes_controller.modificar_estat_comanda("Enviada", comanda_101)
    comandes_controller.modificar_quantitat(comanda_101, "bicicleta", 2)
    comandes_controller.modificar_quantitat(comanda_101, "casc", 4)
    comandes_controller.afegir_producte(comanda_101, "pantalons", 1)

    # Llistat de comandes actualitzat per Anna
    print(f"Comandes del client {anna.nom}: {len(anna.llista_comandes)}")
    comandes_controller.llistar_comandes(anna)

    # Modificar quantitats de comandes 103 (Pere)
    comandes_controller.modificar_quantitat(comanda_103, "maillot", 1)
    comandes_controller.modificar_quantitat(comanda_103, "roda", 2)

    # Modificar quantitats de comandes 104 (Pere)
    comandes_controller.modificar_quantitat(comanda_104, "guants", 2)

    # Llistat de comandes actualitzat per Pere
    print(f"Comandes del client {pere.nom}: {len(pere.llista_comandes)}")
    comandes_controller.llistar_comandes(pere)

    # Llistat de comandes per Joan
    comandes_controller.llistar_comandes(joan)
