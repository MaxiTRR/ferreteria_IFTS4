from helpers_ferreteria import inputDni, show_menu_providers, continue_or_exit, input_Tel
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
                print("El proveedor no se encuentra registrado. Puede ingresar sus datos.") #CAMBIAR
                operation = 1
                while operation == 1:
                    ing_razon_social = input("Ingrese la razon social del nuevo proveedor: ")
                    if ing_razon_social == "":
                        print("La razon social no puede ser un campo vacio.")
                    else:
                        operation = 2

                while operation == 2:
                    ing_dir_prov = input("Ingrese la direccion completa del nuevo proveedor: ")
                    if ing_dir_prov == "":
                        print("El campo direccion no puede ser un campo vacio.")
                    else:
                        operation = 3

                while operation == 3:
                    try:
                        ing_tel_prov = int(input("Ingrese el telefono del nuevo proveedor: "))
                    except ValueError:
                        print("El campo telefono solo acepta caracteres numericos.")
                    else:
                        operation = 4

                while operation == 4:
                    ing_mail_prov = input("Ingrese el mi=ail del nuevo proveedor: ")
                    if ing_mail_prov == "":
                        print("El campo mail no puede ser un campo vacio.")
                    else:
                        operation = 5

                while operation == 5:
                    ing_iva_prov = input("Ingrese la situacio ante el IVA del nuevo proveedor: ")
                    if ing_iva_prov == "":
                        print("El campo de la situacion ante el IVA no puede ser un campo vacion.")
                    else:
                        operation = 6

                Provider.reg_Prov(dni_prov, ing_razon_social, ing_dir_prov, ing_tel_prov, ing_mail_prov, ing_iva_prov)
                print("Proveedor registrado con exito.") #CAMBIAR
            else:
                if result[1] == 1:
                    print("El proveedor ya se encuentra dado de alta.")
                else:
                    print("El proveedor se encuentra dado de baja, por lo tanto se dara de Alta.") #CAMBIAR
                    Provider.change_alta_provider(dni_prov, 1)

            opc_Chosen = continue_or_exit(opc_Chosen)

        #CONSULTAR DATOS PROVEEDOR
        while opc_Chosen == "2":
            dni_prov = inputDni("Ingrese el dni del proveedor del que desea consultar sus datos: ")
            result = Provider.query_provider(dni_prov)
            if not result:
                print("El proveedor no se encuentra registrado.") #CAMBIAR
            else:
                print(result[0]) #CAMBIAR

            opc_Chosen = continue_or_exit(opc_Chosen)

        #MODIFICAR DATOS PROVEEDOR (TELEFONO)
        while opc_Chosen == "4":
            dni_prov = inputDni("Ingrese el dni del proveedor del que desea modificar sus datos: ")
            result = Provider.query_dni_razon_social_tel_alta_prov(dni_prov)
            if not result:
                print("El proveedor no se encuentra registrado.") #CAMBIAR
            else:
                if result[3] == 0:
                    print("El proveedor se encuentra dado de baja.") #CAMBIAR
                else:
                    tel_prov = input_Tel()
                    if tel_prov == 0:
                        print("No se han producido cambios en el registro.")
                    else:
                        Provider.change_tel_prov(dni_prov, tel_prov)
                        Provider.query_dni_razon_social_tel_alta_prov(dni_prov)

            opc_Chosen = continue_or_exit(opc_Chosen)

        #SALIR MENU PRINCIPAL
        if opc_Chosen == "7":
            opc = False

