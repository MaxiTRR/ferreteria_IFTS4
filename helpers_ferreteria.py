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
            [2] - Consultar datos proveedor
            [3] - Baja proveedor
            [4] - Modificar datos proveedor
            [5] - Pedido de stock
            [6] - Devolucion de stock
            [7] - Salir menu principal

            *********************************************************
            """)

#Funcion para mostrar el menu de articulos
def show_menu_articles():
    print("""
            *************** MENU ARTICULOS - FERRETERIA ***************

            [1] - Registrar/Alta articulo
            [2] - Baja articulo
            [3] - Modificar datos de un articulo
            [4] - Ingreso de remito de pedido de stock
            [5] - Listado de articulos sin stock
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

#Validacion input del codigo de articulo
def input_cod_art(text):
    val = True
    while val == True:
        try:
            cod_art = int(input(text))
        except ValueError:
            print("El codigo de articulo solo acepta caracteres numericos.")
        else:
            val = False
    return cod_art

#Validacion input del telefono (proveedor)
def input_Tel():
    tel = 0
    val = True
    while val == True:
        try:
            tel = int(input("Ingrese el telefono nuevo que desea modificar: "))
        except ValueError:
            print("El campo telefono solo acepta caracteres numericos o se ha elegido mantener el campo sin modificacion.")
            return tel
        else:
            val = False
            return tel

#Funcion para seguir agregando opciones o salir al submenu (proveedores)
def continue_or_exit(opt):
    opc_Chosen = opt
    con = input("Desea continuar? Escriba N si desea salir al menu, "
                   "sino presione cualquier tecla: ").upper()
    if con == "N":
        opc_Chosen = "10"
        return opc_Chosen
    return opc_Chosen

#Funcion para limpiar la pantalla de la consola
def limpioPantalla():
    sisOper = os.name
    if sisOper == "posix":   # si fuera UNIX, mac para Apple, java para maquina virtual Java
        os.system("clear")
    elif sisOper == "ce" or sisOper == "nt" or sisOper == "dos":  # windows
        os.system("cls")