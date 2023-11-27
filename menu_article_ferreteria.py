from helpers_ferreteria import inputDni, input_cod_art, show_menu_articles, continue_or_exit, input_price
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
                    cod_art = input_cod_art("Ingrese el codigo del articulo que desea registrar/dar de alta: ")
                    result_art = Article.query_codArt_alta_article(cod_art)
                    if result_art:
                        print_data_art = Article.query_art(cod_art)

                        print()
                        print("**************************************************************")
                        print("CODIGO: ", print_data_art[0])
                        print("NOMBRE: ", print_data_art[1])
                        print("RUBRO: ", print_data_art[2])
                        print("PRECIO: ", print_data_art[3])
                        print("DNI PROVEEDOR: ", print_data_art[4])
                        print("ESTADO ALTA: ", print_data_art[5])
                        print("**************************************************************")
                        print()

                        if result_art[1] == 1:
                            print("El articulo ya se encuentra dado de alta.")
                        else:
                            print("El articulo se encuentra dado de baja.")
                            op_proceed = True
                            while op_proceed == True:
                                proceed = input("Desea dar de alta nuevamente el articulo? Y/N: ").upper()
                                if proceed == "N":
                                    print("La opcion elegida fue N. No se realizo el alta del articulo.")
                                    op_proceed = False
                                elif proceed == "Y":
                                    Article.change_alta_article(cod_art, 1)
                                    print("El articulo se dio de alta con exito!")
                                    op_proceed = False
                                else:
                                    print("Opcion no valida. Por favor, ingrese Y o N.")
                    else:
                        print("El articulo no se encuentra registrado. Se pueden ingresar sus datos para registrarlo.")
                        operation = 1

                        while operation == 1:
                            ing_art_name = input("Ingrese el nombre del articulo: ")
                            if ing_art_name == "":
                                print("El nombre del articulo no puede ser un campo vacio.")
                            else:
                                operation = 2

                        while operation == 2:
                            ing_art_rubro = input("Ingrese un rubro para el articulo:" )
                            if ing_art_rubro == "":
                                print("El rubro del articulo no puede ser un campo vacio.")
                            else:
                                operation = 3

                        while operation == 3:
                            try:
                                ing_art_price = int(input("Ingrese el precio del articulo: "))
                            except ValueError:
                                print("El campo precio solo acepta valores numericos.")
                            else:
                                operation = 4

                        print()
                        print("**************************************************************")
                        print("CODIGO: ", cod_art)
                        print("NOMBRE: ", ing_art_name)
                        print("RUBRO: ", ing_art_rubro)
                        print("PRECIO: ", ing_art_price)
                        print("DNI PROVEEDOR: ", dni_prov)
                        print("**************************************************************")
                        print()

                        op_proceed = True
                        while op_proceed == True:
                            proceed = input("Desea registrar el articulo? Y/N: ").upper()
                            if proceed == "N":
                                print("La opcion elegida fue N. No se realizo el alta del articulo.")
                                op_proceed = False
                            elif proceed == "Y":
                                Article.reg_Art(cod_art, ing_art_name, ing_art_rubro, ing_art_price, dni_prov)
                                print("El articulo fue registrado con exito!")
                                op_proceed = False
                            else:
                                print("Opcion no valida. Por favor, ingrese Y o N.")

            opc_Chosen = continue_or_exit(opc_Chosen)

        #CONSULTAR DATOS ARTICULOS
        while opc_Chosen == "2":
            cod_art = input_cod_art("Ingrese el codigo del articulo que desea registrar/dar de alta: ")
            result = Article.query_art(cod_art)
            if not result:
                print("El articulo no se encuentra registrado.")  # CAMBIAR
            else:
                print()
                print("**************************************************************")
                print("CODIGO: ", result[0])
                print("NOMBRE: ", result[1])
                print("RUBRO: ", result[2])
                print("PRECIO: ", result[3])
                print("DNI PROVEEDOR: ", result[4])
                print("ESTADO ALTA: ", result[5])
                print("STOCK: ", result[6])
                print("ESTADO TRANSACCION: ", result[7])
                print("**************************************************************")
                print()

            opc_Chosen = continue_or_exit(opc_Chosen)

        #BAJA ARTICULO
        while opc_Chosen == "3":
            cod_art = input_cod_art("Ingrese el codigo del articulo que desea registrar/dar de alta: ")
            result = Article.query_codArt_alta_estadoTrans_article(cod_art)
            if not result:
                print("El articulo no se encuentra registrado.")  # CAMBIAR
            else:
                print_data_art = Article.query_art(cod_art)

                print()
                print("**************************************************************")
                print("CODIGO: ", print_data_art[0])
                print("NOMBRE: ", print_data_art[1])
                print("RUBRO: ", print_data_art[2])
                print("PRECIO: ", print_data_art[3])
                print("DNI PROVEEDOR: ", print_data_art[4])
                print("ESTADO ALTA: ", print_data_art[5])
                print("**************************************************************")
                print()

                if result[1] == 0:
                    print("El articulo ya se encuentra dado de baja.")
                else:
                    if result[2] == 1:
                        print("El articulo se encuentra en una transaccion activa. No podra darse de baja hasta que se finalize la transaccion.")
                    else:
                        print("El articulo se dara de baja.") #CAMBIAR
                        op_proceed = True
                        while op_proceed == True:
                            proceed = input("Desea dar de baja el articulo? Y/N: ").upper()
                            if proceed == "N":
                                print("La opcion elegida fue N. No se realizo el alta del articulo.")
                                op_proceed = False
                            elif proceed == "Y":
                                Article.change_alta_article(cod_art, 0)
                                #Article.query_codArt_alta_estadoTrans_article(cod_art) #CAMBIAR
                                print("El articulo fue dado de baja con exito!")
                                op_proceed = False
                            else:
                                print("Opcion no valida. Por favor, ingrese Y o N.")

            opc_Chosen = continue_or_exit(opc_Chosen)

        #MODIFICAR DATOS ARTICULO (PRECIO)
        while opc_Chosen == "4":
            cod_art = input_cod_art("Ingrese el codigo del articulo que desea modificar: ")
            result = Article.query_codArt_name_price_alta_estadoTrans_article(cod_art)
            if not result:
                print("El articulo no se encuentra registrado.")
            else:

                print()
                print("**************************************************************")
                print("CODIGO: ", result[0])
                print("NOMBRE: ", result[1])
                print("PRECIO: ", result[2])
                print("ESTADO ALTA: ", result[3])
                print("ESTADO TRANSACCION: ", result[4])
                print("**************************************************************")
                print()

                if result[3] == 0:
                    print("El articulo se encuentra dado de baja. No puede modificar sus datos hasta darlo de alta nuevamente.")
                else:
                    if result[4] == 1:
                        print("El articulo se encuentra en una transaccion activa. Debe finalizarla para poder modificar sus datos.")
                    else:
                        ing_new_price = input_price("Ingrese el nuevo precio del articulo (No ingrese datos para dejar como estaba):")
                        if ing_new_price == 0:
                            print("No se han producido cambios en el registro.")
                            #print(result[0] + result[2]) #CAMBIAR
                        else:
                            print()
                            print("**************************************************************")
                            print("PRECIO ORIGINAL: $", result[2])
                            print("PRECIO NUEVO: $", ing_new_price)
                            print()
                            print("**************************************************************")
                            op_proceed = True
                            while op_proceed == True:
                                proceed = input("Desea modificar los datos del articulo? Y/N: ").upper()
                                if proceed == "N":
                                    print("La opcion elegida fue N. No se realizo el alta del articulo.")
                                    op_proceed = False
                                elif proceed == "Y":
                                    Article.chage_price_article(cod_art, ing_new_price)
                                    #Article.query_codArt_name_price_alta_estadoTrans_article(cod_art) #CAMBIAR?
                                    print("Los datos del articulo fueron modificados con exito!")
                                    op_proceed = False
                                else:
                                    print("Opcion no valida. Por favor, ingrese Y o N.")

            opc_Chosen = continue_or_exit(opc_Chosen)

        #ACTUALIZAR STOCK (INGRESO DE REMITO)
        while opc_Chosen == "5":
            cod_art = input_cod_art("Ingrese el codigo del articulo que desea modificar: ")
            result_art = Article.query_cod_nombre_alta_stock_estado_article(cod_art)
            if not result_art:
                print("El articulo se encuentra registrado.")
            else:
                if result_art[2] == 0:
                    print("El articulo se encuentra dado de baja.")
                else:
                    result_trans = Provider.query_trans_for_update_stock(cod_art)
                    if not result_trans:
                        print("No se encontraron transacciones de pedido de este articulo.")
                    else:
                        op_proceed = True
                        while op_proceed == True:
                            proceed = input("Se encontro stock para actualizar. Desea hacerlo? Y/N: ").upper()
                            if proceed == "N":
                                print("La opcion elegida fue N. No se realizo la devolucion.")
                                op_proceed = False
                            elif proceed == "Y":
                                print("Puede actualizar el stock!") #REVISAR
                                new_stock = 0
                                for reg in result_trans:
                                    new_stock = reg[3] + result_art[3]
                                Article.change_stock_article(cod_art, new_stock)
                                Article.change_estadoTrans_article(cod_art, 0)
                                for reg in result_trans:
                                    Provider.change_estado_trans(reg[0], 0)
                                op_proceed = False
                            else:
                                print("Opcion no valida. Por favor, ingrese Y o N.")

            opc_Chosen = continue_or_exit(opc_Chosen)

        #CONSULTA ARTICULOS SIN STOCK
        while opc_Chosen == "6":
            result = Article.query_codArt_nombreArt_alta_stock_article()
            if not result:
                print("No se encontro ningun articulo con 0 stock.")
            else:
                for reg in result:
                    print(reg)

            opc_Chosen = continue_or_exit(opc_Chosen)

        # SALIR MENU PRINCIPAL
        if opc_Chosen == "7":
            opc = False