from helpers_ferreteria import inputDni, continue_or_exit, show_menu_sales, input_cod_art, input_cant, total_sale
from ferreteria_Sale import *
from ferreteria_Client import *
from ferreteria_Art import *
from datetime import datetime

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
                    #PROBABLEMENTE AGREGAR UN WHILE AQUI
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
                                if cant > result_art[6]:
                                    print("La cantidad que desea comprar supera el stock del articulo.")
                                else:
                                    total_pago = 0
                                    total_pago = total_sale(cant, result_art[3])
                                    new_stock = result_art[6] - cant
                                    fecha = datetime.now()
                                    print(f"El monto total a pagar es de ${total_pago}")
                                    print("registro venta")   #REGISTRAR VENTA
                                    Sale.reg_Sale(dni_cli, cod_art, total_pago, cant, fecha)
                                    result_sale = Sale.query_sale()
                                    date = result_sale[5]
                                    print(date.strftime("%c")) #CAMBIAR Y FORMATEAR CON EL RESTO DE LOS INDICES
                                    print("Actualizar stock articulo") #ACTUALIZAR STOCK EN ARTICULOS
                                    Article.change_stock_article(cod_art, new_stock)

            opc_Chosen = continue_or_exit(opc_Chosen)

        while opc_Chosen == "2":
            fecha_hoy = datetime.now()
            fecha_format = fecha_hoy.strftime('%Y-%m-%d')
            print(fecha_hoy.strftime('%Y-%m-%d')) #REVISAR
            result = Sale.query_today_sales(fecha_format)
            if not result:
                print("No se encontro ninguna venta el dia de hoy.")
            else:
                for reg in result:
                    date = reg[5]
                    print(reg) #REVISAR
                    print(date) #REVISAR

            opc_Chosen = continue_or_exit(opc_Chosen)

        if opc_Chosen == "3":
            opc = False


                                
