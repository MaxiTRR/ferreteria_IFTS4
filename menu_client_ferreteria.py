from helpers_ferreteria import show_menu_clients, inputDni, continue_or_exit, show_menu_Iva
from ferreteria_Client import *

def menu_clients():
    opc = True
    while opc == True:
        show_menu_clients()
        opc_Chosen = input("Ingrese la opcion elegida: ")

        #REGISTRAR/ALTA CLIENTE
        while opc_Chosen == "1":
            dni_cli = inputDni("Ingrese el DNI del cliente que desea registrar: ")
            result = Client.query_client(dni_cli)
            if result:
                if result[7] == 1:
                    print("El cliente ya se encuentra dado de alta.")
                else:
                    print("El cliente se encuentra dado de baja. Dar de alta?") #CAMBIAR
                    proceed = input("Desea dar de alta al cliente nuevamente? Y/N: ").upper()
                    if proceed != "Y":
                        print("No se realizaron cambios en el estado del cliente.")
                    else:
                        Client.change_alta_client(dni_cli, 1)
                        Client.query_client(dni_cli)
            else:
                print("El cliente no se encuentra registrado. Puede ingresar sus datos para registrarlo.")
                operation = 1
                while operation == 1:
                    ing_name = input("Ingrese el nombre del cliente: ")
                    if ing_name == "":
                        print("El campo nombre no puede quedar vacio.")
                    else:
                        operation = 2

                while operation == 2:
                    ing_last_name = input("Ingrese el apellido del cliente: ")
                    if ing_last_name == "":
                        print("El campo apellido no puede quedar vacio.")
                    else:
                        operation = 3

                while operation == 3:
                    ing_dir = input("Ingrese la direccion del cliente: ")
                    if ing_dir == "":
                        print("El campo direccion no puede quedar vacio.")
                    else:
                        operation = 4

                while operation == 4:
                    try:
                        ing_tel = int(input("Ingrese el telefono del cliente: "))
                    except ValueError:
                        print("El campo telefono solo acepta caracteres numericos")
                    else:
                        operation = 5

                while operation == 5:
                    ing_mail = input("Ingrese el mail del cliente: ")
                    if ing_mail == "":
                        print("El campo mail no puede quedar vacio.")
                    else:
                        operation = 6

                while operation == 6:
                    ing_IVA = input("Ingrese la situacion ante el IVA del cliente: ")
                    if ing_IVA == "":
                        print("El campo de situacion ante el IVA no puede quedar vacio.")
                    else:
                        operation = 7

                Client.reg_Client(dni_cli, ing_name, ing_last_name, ing_dir, ing_tel, ing_mail, ing_IVA)
                Client.query_client(dni_cli) #CAMBIAR

            opc_Chosen = continue_or_exit(opc_Chosen)

        #CONSULTAR DATOS CLIENTE
        while opc_Chosen == "2":
            dni_cli = inputDni("Ingrese el DNI del cliente que desea registrar: ")
            result = Client.query_client(dni_cli)
            if not result:
                print("El cliente no se encuentra registrado.")
            else:
                Client.query_client(dni_cli)  # CAMBIAR

            opc_Chosen = continue_or_exit(opc_Chosen)

        #BAJA CLIENTE
        while opc_Chosen == "3":
            dni_cli = inputDni("Ingrese el DNI del cliente que desea registrar: ")
            result_1 = Client.query_dni_name_lastname_alta_obs_client(dni_cli)
            if not result_1:
                print("El cliente no se encuentra registrado.")
            else:
                if result_1[3] == 0:
                    print("El cliente ya se encuentra dado de baja.")
                else:
                    proceed = input("Desea dar de baja al cliente? Y/N: ").upper()
                    if proceed != "Y":
                        print("No se realizaron cambios en el estado del cliente.")
                    else:
                        obs = input("Desea agregar alguna observacion?: ")
                        if obs == "":
                            obs = result_1[4]
                            Client.change_alta_obs_client(dni_cli, 0, obs)
                        else:
                            Client.change_alta_obs_client(dni_cli, 0, obs)

            opc_Chosen = continue_or_exit(opc_Chosen)
            
        #MODIFICAR DATOS CLIENTES
        while opc_Chosen == "4":
            dni_cli = inputDni("Ingrese el DNI del cliente que desea modificar: ")
            result = Client.query_dni_nombre_apellido_IVA_alta_alta_client(dni_cli)
            if not result:
                print("El cliente no se encuentra registrado.")
            else:
                if result[4] == 0:
                    print("El cliente se encuentra dado de baja.")
                else:
                    show_menu_Iva()
                    iva = input("Ingrese la nueva situacion ante el IVA del cliente: ")
                    if iva == "":
                        print("No se produjeron modificaciones en el registro")
                        iva = result[3]
                    elif iva == "1":
                        iva = "Responsable Inscripto"
                    elif iva == "2":
                        iva = "Sujeto Excento"
                    elif iva == "3":
                        iva = "Autonomo"
                    elif iva == "4":
                        iva = "Monotributista"
                    else:
                        print("No se ingreso una opcion valida, por lo tanto no se realizaran cambios en el registro.")
                        iva = result[3]
                    Client.change_iva_client(dni_cli, iva)
                    Client.query_client(dni_cli)

            opc_Chosen = continue_or_exit(opc_Chosen)

        # SALIR MENU PRINCIPAL
        if opc_Chosen == "5":
            opc = False