import mariadb
from ferreteriaDB import *

class Article():
    Database = Database.connect_DB("ferreteria")

    def __init__(self):
        pass

    @classmethod
    def reg_Art(self, cod_art, nombre_art, rubro_art, precio_art, dni_prov, alta_art = True, stock_art = 0, estado_trans = False):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = "INSERT INTO articulos (cod_art, nombre_art, rubro_art, precio_art, dni_prov, alta_art, stock_art, estado_trans) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (cod_art, nombre_art, rubro_art, precio_art, dni_prov, alta_art, stock_art, estado_trans)
        mycursor.execute(sql, val)
        mydb.commit()

    @classmethod
    def query_art(self, cod_art):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"SELECT * FROM articulos WHERE cod_art = {cod_art}"
        mycursor.execute(sql)
        myresultado = mycursor.fetchone()
        #print(myresultado)  # REVISAR ESTE PRINT
        return myresultado

    @classmethod
    def query_codArt_alta_article(self, cod_art):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"SELECT cod_art, alta_art  FROM articulos WHERE cod_art = {cod_art}"
        mycursor.execute(sql)
        myresultado = mycursor.fetchone()
        #print(myresultado)  # REVISAR ESTE PRINT
        return myresultado

    @classmethod
    def query_codArt_name_price_alta_estadoTrans_article(self, cod_art):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"SELECT cod_art, nombre_art, precio_art, alta_art, estado_trans FROM articulos WHERE cod_art = {cod_art}"
        mycursor.execute(sql)
        myresultado = mycursor.fetchone()
        print(myresultado)  # REVISAR ESTE PRINT
        return myresultado

    @classmethod
    def query_codArt_alta_estadoTrans_article(self, cod_art):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"SELECT cod_art, alta_art, estado_trans FROM articulos WHERE cod_art = {cod_art}"
        mycursor.execute(sql)
        myresultado = mycursor.fetchone()
        #print(myresultado)  # REVISAR ESTE PRINT
        return myresultado

    @classmethod
    def query_codArt_nombreArt_alta_stock_article(self):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"SELECT cod_art, nombre_art, alta_art, estado_trans FROM articulos WHERE stock_art = 0"
        mycursor.execute(sql)
        myresultado = mycursor.fetchall()
        #print(myresultado)  # REVISAR ESTE PRINT
        return myresultado

    """"@classmethod
    def query_codArt_nombreArt_precioArt_dniProv_alta_stock_estadoTrans_article(self, cod_art):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"SELECT cod_art, nombre_art, precio_art, dni_prov, alta_art, stock_art, estado_trans FROM articulos WHERE cod_art = {cod_art}"
        mycursor.execute(sql)
        myresultado = mycursor.fetchone()
        print(myresultado)  # REVISAR ESTE PRINT
        return myresultado"""

    @classmethod
    def query_cod_nombre_alta_stock_estado_article(self, cod_art):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"SELECT cod_art, nombre_art, alta_art, stock_art, estado_trans FROM articulos WHERE cod_art = {cod_art}"
        mycursor.execute(sql)
        myresultado = mycursor.fetchone()
        # print(myresultado)  # REVISAR ESTE PRINT
        return myresultado

    @classmethod
    def change_alta_article(self, cod_art, alta_art):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"UPDATE articulos SET alta_art = {alta_art} WHERE cod_art = {cod_art}"
        mycursor.execute(sql)
        mydb.commit()

    @classmethod
    def chage_price_article(self, cod_art, precio_art):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"UPDATE articulos SET precio_art = {precio_art} WHERE cod_art = {cod_art}"
        mycursor.execute(sql)
        mydb.commit()

    @classmethod
    def change_stock_article(self, cod_art, new_stock):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"UPDATE articulos SET stock_art = {new_stock} WHERE cod_art = {cod_art}"
        mycursor.execute(sql)
        mydb.commit()

    @classmethod
    def change_estadoTrans_article(self, cod_art, new_estado_trans):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"UPDATE articulos SET estado_trans = {new_estado_trans} WHERE cod_art = {cod_art}"
        mycursor.execute(sql)
        mydb.commit()



