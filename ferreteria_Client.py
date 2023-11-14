import mariadb
from ferreteriaDB import *

""""#Conectar al engine de la base de datos. PROBABLEMENTE ELIMINAR
mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            autocommit=True
        )"""

class Client():
    Database = Database.connect_DB("ferreteria")

    def __init__(self):
        pass

    @classmethod
    def reg_Client(self, dni_cli, nombre_cli, apellido_cli, dir_cli, tel_cli, mail_cli, sit_IVA_cli, alta_cli = True, obs_cli = ""):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = "INSERT INTO clientes (dni_cli, nombre_cli, apellido_cli, dir_cli, tel_cli, mail_cli, sit_IVA_cli, alta_cli, obs_cli) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (dni_cli, nombre_cli, apellido_cli, dir_cli, tel_cli, mail_cli, sit_IVA_cli, alta_cli, obs_cli)
        mycursor.execute(sql, val)
        mydb.commit()

    @classmethod
    def query_client(self, dni_cli):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"SELECT * FROM clientes WHERE dni_cli = {dni_cli}"
        mycursor.execute(sql)
        myresultado = mycursor.fetchone()
        print(myresultado)  # REVISAR ESTE PRINT
        return myresultado

    @classmethod
    def query_dni_name_lastname_alta_obs_client(self, dni_cli):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"SELECT dni_cli, nombre_cli, apellido_cli, alta_cli, obs_cli FROM clientes WHERE dni_cli = {dni_cli}"
        mycursor.execute(sql)
        myresultado = mycursor.fetchone()
        print(myresultado)  # REVISAR ESTE PRINT
        return myresultado

    @classmethod
    def change_alta_client(self, dni_cli, alta_cli):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"UPDATE clientes SET alta_cli = {alta_cli} WHERE dni_cli = {dni_cli}"
        mycursor.execute(sql)
        mydb.commit()

    @classmethod
    def change_alta_obs_client(self, dni_cli, alta_cli, obs_cli):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"UPDATE clientes SET alta_cli = {alta_cli}, obs_cli = '{obs_cli}' WHERE dni_cli = {dni_cli}"
        mycursor.execute(sql)
        mydb.commit()
