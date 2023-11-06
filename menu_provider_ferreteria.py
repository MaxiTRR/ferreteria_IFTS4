from helpers_ferreteria import inputDni, show_menu_providers
from ferreteria_Prov import *

def menu_providers():
    opc = True
    while opc == True:
        show_menu_providers()
        opc_Chosen = input("Ingrese la opcion elegida: ")

        #REGISTRAR/ALTA PROVEEDOR
        while opc_Chosen == "1":
            dni_prov = inputDni("Ingrese el dni del proveedor que deser registrar o dar de alta: ")
            result = Provider.query_dni_and_alta_prov(dni_prov)
            if not result:
                print("El proveedor no se encuentra registrado. Puede ingresar sus datos.")
            else:
                if result[1] == 1:
                    print("El proveedor ya se encuentra dado de alta.")
                else:
                    print("El proveedor se encuentra dado de baja, por lo tanto se dara de Alta.")



