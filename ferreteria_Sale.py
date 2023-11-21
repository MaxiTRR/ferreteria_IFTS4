import mariadb
from ferreteriaDB import *

class Sale():
    Database = Database.connect_DB("ferreteria")

    def __init__(self):
        pass

    @classmethod
    def reg_Sale(self, dni_cli, cod_art, monto_pago, cant_art, fecha_venta):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"INSERT INTO ventas (dni_cli, cod_art, monto_pago, cant_art, fecha_venta) VALUES(%s, %s, %s, %s, %s)"
        val = (dni_cli, cod_art, monto_pago, cant_art, fecha_venta)
        mycursor.execute(sql, val)
        mydb.commit()

    @classmethod
    def query_sale(self):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"SELECT * FROM ventas ORDER BY id_venta DESC LIMIT 1"
        mycursor.execute(sql)
        myresultado = mycursor.fetchone()
        #print(myresultado)
        return myresultado

    @classmethod
    def query_today_sales(self, time):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = "SELECT * FROM ventas WHERE fecha_venta LIKE '"+time+"%'"
        mycursor.execute(sql)
        myresultado = mycursor.fetchall()
        # print(myresultado)
        return myresultado

        
        