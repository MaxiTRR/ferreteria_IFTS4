from ferreteriaDB import *
from ferreteria_Client import *
from ferreteria_Prov import *
from ferreteria_Art import *

#Metodos para setear la base de datos con registros iniciales. COMENTAR Y DESCOMENTAR.
BD = "ferreteria"
clientTable = "clientes"
provTable = "proveedores"
artTable = "articulos"

def set_Database():
    #Database.create_DB(BD)
    #Database.create_Table_Clientes(BD, clientTable)
    #Database.create_Table_Proveedores(BD, provTable)
    Database.create_Table_Articulos(BD, artTable)

#set_Database()

def set_Client_Regs():
    Client.reg_Client(32548528, "Peter", "Parker", "Telarania 29", 45245887, "spiderParker@web.com", "monotributista", True)

#set_Client_Regs()

def set_Prov_Regs():
    Provider.reg_Prov(69542178, "Black & Decker", "Ramon Falcon 345, Flores, CABA", 42896524, "black@decker.com", "inscripto", True)

#set_Prov_Regs()

def set_Art_Reg():
    Article.reg_Art(3100, "Pinza De Punta","herramienta manual", 7.791, 42896524, True,0, False)

#set_Art_Reg()
