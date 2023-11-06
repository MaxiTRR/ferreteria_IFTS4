import mariadb
from helpers_ferreteria import show_menu_principal

principal_Menu = True

while principal_Menu == True:
    show_menu_principal()

    option = input("Ingrese el número de opción: ")

    if option == "1":
        print("PROVEEDORES")
    if option == "2":
        print("CLIENTES")
    if option == "3":
        print("ARTICULOS")
    if option == "4":
        print("VENTAS")
    if option == "5":
        print("Saludos!")
        principal_Menu = False