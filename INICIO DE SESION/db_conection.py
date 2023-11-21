import pymysql

class DatabaseConnection:
    def conectar_base_de_datos():
        try:
            db = pymysql.connect(
                host="localhost",
                user="elares",
                password="jhice1317",
                database="elares",
                cursorclass=pymysql.cursors.DictCursor
            )
            return True
        except pymysql.Error as e:
            print(f"Error de conexión a la base de datos: {e}")
            return False
