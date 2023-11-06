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