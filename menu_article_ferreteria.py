from helpers_ferreteria import inputDni, show_menu_articles
from ferreteria_Art import *
from ferreteria_Prov import *

def menu_articles():
    opc = True
    while opc == True:
        show_menu_articles()
        opc_Chosen = input("Ingrese la opcion elegida: ")

        #REGISTRAR/ALTA ARTICULO
        while opc_Chosen == "1":
            dni_prov = inputDni("Ingrese el dni de un proveedor para poder dar de alta un articulo suyo: ")
            result = Provider.query_dni_and_alta_prov(dni_prov)
            if not result:
                print("El proveedor no se encuentra registrado.")
            else:
                if result[1] == 0:
                    print("El proveedor se encuentra dado de baja.")
                else:
                    print("Se puede ingresar los datos del articulo.") #CAMBIAR

