import mariadb

mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
#            password="RootPassword123!",    # no le puse pass a mi base por el momento
            autocommit=True
        )

class Database():
    def __init__(self):
        pass

    @classmethod
    def create_DB(self, name_DB):
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS " + f"{name_DB}")
        mycursor.execute("SHOW DATABASES")
        for x in mycursor:
            print(x)

    @classmethod
    def connect_DB(self, name_DB):
        return mariadb.connect(
            host="127.0.0.1",
            user="root",
            # password="RootPassword123!",    # no le puse pass a mi base por el momento
            database=name_DB
        )

    @classmethod
    def create_Table_Clientes(self, name_DB, name_Table):
        mydb = self.connect_DB(name_DB)
        mycursor = mydb.cursor()
        mycursor.execute(
            "CREATE TABLE " + f"{name_Table}" + "(dni_cli INT PRIMARY KEY,nombre_cli VARCHAR(255),apellido_cli VARCHAR(255), dir_cli VARCHAR(255),"
                                               "tel_cli VARCHAR(255), mail_cli VARCHAR(255),sit_IVA_cli VARCHAR(255), alta_cli BOOL)")
        mycursor.execute("SHOW TABLES")
        for ind in mycursor:
            print(ind)

    @classmethod
    def create_Table_Proveedores(self, name_DB, name_Table):
        mydb = self.connect_DB(name_DB)
        mycursor = mydb.cursor()
        mycursor.execute(f"CREATE TABLE {name_Table}(dni_prov INT PRIMARY KEY, razon_social VARCHAR(255), dir_prov VARCHAR(255),"
                         f"tel_prov INT, mail_prov VARCHAR(255), sit_IVA_prov VARCHAR(255), alta_prov BOOL)")
        mycursor.execute("SHOW TABLES")
        for ind in mycursor:
            print(ind)

    @classmethod
    def create_Table_Articulos(self, name_DB, name_Table):
        mydb = self.connect_DB(name_DB)
        mycursor = mydb.cursor()
        mycursor.execute(f"CREATE TABLE {name_Table}(cod_art INT PRIMARY KEY, nombre_art VARCHAR(255), rubro_art VARCHAR(255), precio_art INT,"
                         f" stock_art INT, dni_prov INT, alta_art BOOL)")
        mycursor.execute("SHOW TABLES")
        for ind in mycursor:
            print(ind)

    @classmethod
    def create_Table_Ventas(self, name_DB, name_Table):
        mydb = self.connect_DB(name_DB)
        mycursor = mydb.cursor()
        mycursor.execute(f"CREATE TABLE {name_Table}(ID_Venta INT PRIMARY KEY, dni_cli INT, cod_art INT, monto_pago INT, cant_art INT, fecha_venta DATE)")
        mycursor.execute("SHOW TABLES")
        for ind in mycursor:
            print(ind)