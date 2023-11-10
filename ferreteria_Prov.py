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

    @classmethod
    def query_dni_and_alta_prov(self, dni_prov):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"SELECT dni_prov, alta_prov FROM proveedores WHERE dni_prov = {dni_prov}"
        mycursor.execute(sql)
        myresultado = mycursor.fetchone()
        print(myresultado) #REVISAR ESTE PRINT
        return myresultado

    @classmethod
    def query_dni_razon_social_tel_alta_prov(self, dni_prov):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"SELECT dni_prov, razon_social, tel_prov, alta_prov FROM proveedores WHERE dni_prov = {dni_prov}"
        mycursor.execute(sql)
        myresultado = mycursor.fetchone()
        print(myresultado)  # REVISAR ESTE PRINT
        return myresultado


    @classmethod
    def change_alta_provider(self, dni_prov, alta_prov):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"UPDATE proveedores SET alta_prov = {alta_prov} WHERE dni_prov = {dni_prov}"
        mycursor.execute(sql)
        mydb.commit()

    @classmethod
    def change_tel_prov(self, dni_prov, tel_prov):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"UPDATE proveedores SET tel_prov = {tel_prov} WHERE dni_prov = {dni_prov}"
        mycursor.execute(sql)
        mydb.commit()