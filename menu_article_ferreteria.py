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
                        if result_art[1] == 1:
                            print("El articulo ya se encuentra dado de alta.")
                        else:
                            print("El articulo se encuentra dado de baja. Se dara de alta.") #CAMBIAR
                            Article.change_alta_article(cod_art, 1)
                    else:
                        print("El articulo no se encuentra registrado. Se pueden ingresar sus datos.") #CAMBIAR
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

                        Article.reg_Art(cod_art, ing_art_name, ing_art_rubro, ing_art_price, dni_prov)

            opc_Chosen = continue_or_exit(opc_Chosen)

        #CONSULTAR DATOS ARTICULOS
        while opc_Chosen == "2":
            cod_art = input_cod_art("Ingrese el codigo del articulo que desea registrar/dar de alta: ")
            result = Article.query_art(cod_art)
            if not result:
                print("El articulo no se encuentra registrado.")  # CAMBIAR
            else:
                print(result[0]) #CAMBIAR

            opc_Chosen = continue_or_exit(opc_Chosen)

        #BAJA ARTICULO
        while opc_Chosen == "3":
            cod_art = input_cod_art("Ingrese el codigo del articulo que desea registrar/dar de alta: ")
            result = Article.query_codArt_alta_estadoTrans_article(cod_art)
            if not result:
                print("El articulo no se encuentra registrado.")  # CAMBIAR
            else:
                if result[1] == 0:
                    print("El articulo ya se encuentra dado de baja.")
                else:
                    if result[2] == 1:
                        print("El articulo se encuentra en una transaccion activa. No podra darse de baja hasta que se finalize la transaccion.")
                    else:
                        print("El articulo se dara de baja.") #CAMBIAR
                        Article.change_alta_article(cod_art, 0)
                        Article.query_codArt_alta_estadoTrans_article(cod_art) #CAMBIAR

            opc_Chosen = continue_or_exit(opc_Chosen)

        #MODIFICAR DATOS ARTICULO (PRECIO)
        while opc_Chosen == "4":
            cod_art = input_cod_art("Ingrese el codigo del articulo que desea modificar: ")
            result = Article.query_codArt_name_price_alta_estadoTrans_article(cod_art)
            if not result:
                print("El articulo se encuentra registrado.")
            else:
                if result[3] == 0:
                    print("El articulo se encuentra dado de baja. No puede modificar sus datos hasta darlo de alta nuevamente.")
                else:
                    if result[4] == 1:
                        print("El articulo se encuentra en una transaccion activa. Debe finalizarla para poder modificar sus datos.")
                    else:
                        ing_new_price = input_price("Ingrese el nuevo precio del articulo (No ingrese datos para dejar como estaba):")
                        if ing_new_price == 0:
                            print("No se han producido cambios en el registro.")
                            print(result[0] + result [2]) #CAMBIAR
                        else:
                            Article.chage_price_article(cod_art, ing_new_price)
                            Article.query_codArt_name_price_alta_estadoTrans_article(cod_art) #CAMBIAR?
                            print("Se han modificado sus datos con exito!") #CAMBIAR

            opc_Chosen = continue_or_exit(opc_Chosen)

        # SALIR MENU PRINCIPAL
        if opc_Chosen == "7":
            opc = False