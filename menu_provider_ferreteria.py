from helpers_ferreteria import inputDni, show_menu_providers, continue_or_exit, input_Tel, input_cant, total_sale, input_cod_art
from ferreteria_Prov import *
from ferreteria_Art import *
from datetime import datetime

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

        #BAJA PROVEEDOR
        while opc_Chosen == "3":
            dni_prov = inputDni("Ingrese el dni del proveedor del que desea dar de baja: ")
            result = Provider.query_dni_razonSocial_alta_estadoPedido_prov(dni_prov)
            if not result:
                print("El proveedor no se encuentra registrado.")
            else:
                if result[2] == 0:
                    print("El proveedor ya se encuentra dado de baja.")
                else:
                    if result[3] == 1:
                        print("El proveedor se encuentra en un pedido de stock activo. Debe finalizarlo para poder darlo de baja.") #CAMBIAR
                    else:
                        proceed = input("Desea dar de baja al proveedor? Y/N: ").upper()
                        if proceed == "Y":
                            Provider.change_alta_provider(dni_prov, 0)
                            Provider.query_dni_razonSocial_alta_estadoPedido_prov(dni_prov) #CAMBIAR
                            print("Proveedor dado de baja con exito!") #CAMBIAR
                        else:
                            print("No se realizaron cambios en el estado del proveedor.")

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

        #REALIZAR PEDIDOS STOCK
        while opc_Chosen == "5":
            dni_prov = inputDni("Ingrese el dni del proveedor del que desea dar de baja: ")
            result_prov = Provider.query_dni_razonSocial_alta_estadoPedido_prov(dni_prov)
            if not result_prov:
                print("El proveedor no se encuentra registrado.")
            else:
                if result_prov[2] == 0:
                    print("El proveedor se encuentra dado de baja.")
                else:
                    cod_art = input_cod_art("Ingrese el codigo del articulo que desea vender: ")
                    result_art = Article.query_art(cod_art)
                    if not result_art:
                        print("El articulo no se encuentra registrado.")
                    else:
                        if result_art[5] == 0:
                            print("El articulo se encuentra dado de baja.")
                        else:
                            if result_art[4] != dni_prov:
                                print("El proveedor del articulo no se corresponde con el ingresado anteriormente")
                            else:
                                cant = input_cant("Ingrese la cantidad de articulos que desea pedir: ")
                                total_pago = 0
                                total_pago = total_sale(cant, result_art[3])
                                print(f"El total a pagar es de ${total_pago}")
                                #IMPRIMIR LOS DATOS DEL PEDIDO ACA
                                op_proceed = True
                                while op_proceed == True:
                                    proceed = input("Desea registrar el pedido? Y/N: ").upper()
                                    if proceed == "N":
                                        print("La opcion elegida fue N. No se realizo el pedido.")
                                        op_proceed = False
                                    elif proceed == "Y":
                                        print("registrar pedido") #REVISAR
                                        fecha_trans = datetime.now()
                                        Provider.reg_trans_pedido(dni_prov, cod_art, cant, total_pago, fecha_trans, "pedido stock")
                                        Article.change_estadoTrans_article(cod_art, True)
                                        Provider.query_trans()
                                        #IMPRIMIR LOS RESULTADOS DE LA QUERY. FIJARSE TEMA DE LA FECHA
                                        op_proceed = False
                                    else:
                                        print("Opcion no valida. Por favor, ingrese Y o N.")

            opc_Chosen = continue_or_exit(opc_Chosen)

        #SALIR MENU PRINCIPAL
        if opc_Chosen == "7":
            opc = False

