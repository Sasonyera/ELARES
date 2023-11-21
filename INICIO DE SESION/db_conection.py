import pymysql

class DatabaseConnection:
    def __init__(self):
        self.db = None
        self.cursor = None

    def conectar_base_de_datos(self):
        try:
            self.db = pymysql.connect(
                host="localhost",
                user="elares",
                password="jhice1317",
                database="elares",
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.db.cursor()
            return True
        except pymysql.Error as e:
            print(f"Error de conexión a la base de datos: {e}")
            return False

    def get_connection(self):
        return self.db

    def get_cursor(self):
        return self.cursor

    def close_connection(self):
        if self.db:
            self.db.close()