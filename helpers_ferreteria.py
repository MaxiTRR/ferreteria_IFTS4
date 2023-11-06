import os

#Funcion para mostrar el menu principal
def show_menu_principal():
    print("""
        *************** MENU PRINCIPAL FERRETERIA ***************

        [1] - Proveedores
        [2] - Clientes
        [3] - Articulos
        [4] - Ventas
        [5] - Salir
        
        *********************************************************
        """)

#Funcion para mostrar el menu de proveedores
def show_menu_providers():
    print("""
            *************** MENU PROVEEDORES - FERRETERIA ***************

            [1] - Registrar/Alta proveedor
            [2] - Baja proveedor
            [3] - Modificar datos proveedor
            [4] - Pedido de stock
            [5] - Devolucion de stock
            [6] - Salir menu principal

            *********************************************************
            """)

#Validacion input del dni del cliente y proveedores
def inputDni(text):
    val = True
    while val == True:
        try:
            dni = int(input(text))
        except ValueError:
            print("El dni solo acepta caracteres numericos")
        else:
            val = False
    return dni