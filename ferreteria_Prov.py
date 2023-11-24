import mariadb
from ferreteriaDB import *

class Provider():
    Database = Database.connect_DB("ferreteria")

    def __init__(self):
        pass

    @classmethod
    def reg_Prov(self, dni_prov, razon_social, dir_prov, tel_prov, mail_prov, sit_IVA_prov, alta_prov = True, estado_pedido = False, obs_prov = ""):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = "INSERT INTO proveedores (dni_prov, razon_social, dir_prov, tel_prov, mail_prov, sit_IVA_prov, alta_prov, estado_pedido, obs_prov) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (dni_prov, razon_social, dir_prov, tel_prov, mail_prov, sit_IVA_prov, alta_prov, estado_pedido, obs_prov)
        mycursor.execute(sql, val)
        mydb.commit()

    @classmethod
    def reg_trans_pedido(self, dni_prov_trans, cod_art_trans, cant_art_trans, precio_trans, fecha_trans,
                         tipo_trans, obs_trans=None, estado_trans=True):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = "INSERT INTO transacciones_prov (dni_prov_trans, cod_art_trans, cant_art_trans, precio_trans, fecha_trans, tipo_trans, " \
              "obs_trans, estado_trans) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (dni_prov_trans, cod_art_trans, cant_art_trans, precio_trans, fecha_trans, tipo_trans, obs_trans, estado_trans)
        mycursor.execute(sql, val)
        mydb.commit()

    @classmethod
    def query_provider(self, dni_prov):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"SELECT * FROM proveedores WHERE dni_prov = {dni_prov}"
        mycursor.execute(sql)
        myresultado = mycursor.fetchone()
        print(myresultado)  # REVISAR ESTE PRINT
        return myresultado

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
    def query_dni_razonSocial_alta_estadoPedido_prov(self, dni_prov):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"SELECT dni_prov, razon_social, alta_prov, estado_pedido FROM proveedores WHERE dni_prov = {dni_prov}"
        mycursor.execute(sql)
        myresultado = mycursor.fetchone()
        print(myresultado)  # REVISAR ESTE PRINT
        return myresultado

    @classmethod
    def query_trans(self):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"SELECT * FROM transacciones_prov ORDER BY id_trans DESC LIMIT 1"
        mycursor.execute(sql)
        myresultado = mycursor.fetchone()
        print(myresultado) #REVISAR
        return myresultado

    @classmethod
    def query_trans_for_update_stock(self, cod_art):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"SELECT * FROM transacciones_prov WHERE (cod_art_trans = {cod_art} AND tipo_trans = 'pedido stock' AND estado_trans = 1)"
        mycursor.execute(sql)
        myresultado = mycursor.fetchall()
        if myresultado:
            for row in myresultado:
                print(row)  # REVISAR
        else:
            print("No se encontraron registros.")
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

    @classmethod
    def change_estado_trans(self, id_trans, new_estado):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"UPDATE transacciones_prov SET estado_trans = {new_estado} WHERE id_trans = {id_trans}"
        mycursor.execute(sql)
        mydb.commit()

