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
