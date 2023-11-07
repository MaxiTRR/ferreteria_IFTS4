from helpers_ferreteria import inputDni, input_cod_art, show_menu_articles
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

