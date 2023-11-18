from helpers_ferreteria import inputDni, continue_or_exit, show_menu_sales, input_cod_art, input_cant
from ferreteria_Sale import *
from ferreteria_Client import *
from ferreteria_Art import *

def menu_sales():
    opc = True
    while opc == True:
        show_menu_sales()
        opc_Chosen = input("Ingrese la opcion elegida: ")

        #VENTA (FACTURACION)
        while opc_Chosen == "1":
            dni_cli = inputDni("Ingrese el DNI del cliente: ")
            result_cli = Client.query_client(dni_cli)
            if not result_cli:
                print("El cliente no se encuentra registrado.")
            else:
                if result_cli[7] == 0:
                    print("El cliente se encuentra dado de baja.")
                else:
                    cod_art = input_cod_art("Ingrese el codigo del articulo que desea vender: ")
                    result_art = Article.query_art(cod_art)
                    if not result_art:
                        print("El articulo no se encuentra registrado.")
                    else:
                        if result_art[5] == 0:
                            print("El articulo se encuentra dado de baja.")
                        else:
                            if result_art[6] <= 0:
                                print("El articulo se encuentra sin stock en estos momentos.")
                            else:
                                cant = input_cant("Ingrese la cantidad de articulos que desea comprar: ")
                                
