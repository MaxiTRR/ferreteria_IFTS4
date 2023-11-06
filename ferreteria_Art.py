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