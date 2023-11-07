import mariadb
from helpers_ferreteria import show_menu_principal
from menu_provider_ferreteria import *
from menu_article_ferreteria import *

principal_Menu = True

while principal_Menu == True:
    show_menu_principal()

    option = input("Ingrese el número de opción: ")

    if option == "1":
        menu_providers()
    if option == "2":
        print("CLIENTES")
    if option == "3":
        menu_articles()
    if option == "4":
        print("VENTAS")
    if option == "5":
        print("Saludos!")
        principal_Menu = False