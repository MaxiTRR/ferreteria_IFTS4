from ferreteriaDB import *
from ferreteria_Client import *

#Metodos para setear la base de datos con registros iniciales. COMENTAR Y DESCOMENTAR.
BD = "ferreteria"
clientTable = "clientes"
provTable = "proveedores"
artTable = "articulos"

def setDatabase():
    Database.create_DB(BD)
    Database.create_Table_Clientes(BD, clientTable)
    Database.ceate_Table_Proveedores(BD, provTable)

#setDatabase()

def setClientRegs():
    Client.reg_Client(32548528, "Peter", "Parker", "Telarania 29", 45245887, "spiderParker@web.com", "monotributista", True)

#setClientRegs()