import mariadb
from ferreteriaDB import *

class Sale():
    Database = Database.connect_DB("ferreteria")

    def __init__(self):
        pass

    @classmethod
    def ref_Sale(self, id_venta, dni_cli, cod_art, monto_pago, cant_art, fecha_venta):
        mydb = self.Database
        mycursor = mydb.cursor()
        sql = f"INSERT INTO ventas (id_venta, dni_cli, cod_art, monto_pago, cant_art, fecha_venta) VALUES(%s, %s, %s, %s, %s, %s)"
        val = (id_venta, dni_cli, cod_art, monto_pago, cant_art, fecha_venta)
        mycursor.execute(sql, val)
        mydb.commit()