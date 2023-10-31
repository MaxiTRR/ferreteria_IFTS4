import mariadb
from ferreteriaDB import *

class Provider():
    Database = Database.connect_DB("ferreteria")

    def __init__(self):
        pass

    @classmethod
    def reg_Prov(self, dni_prov, razon_social, dir_prov, tel_prov, mail_prov, sit_IVA_prov, alta_prov = True):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = "INSERT INTO proveedores (dni_prov, razon_social, dir_prov, tel_prov, mail_prov, sit_IVA_prov, alta_prov) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        val = (dni_prov, razon_social, dir_prov, tel_prov, mail_prov, sit_IVA_prov, alta_prov)
        mycursor.execute(sql, val)
        mydb.commit()