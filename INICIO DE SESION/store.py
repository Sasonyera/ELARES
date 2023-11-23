import tkinter as tk
from tkinter import messagebox
from db_conection import DatabaseConnection
from login import menu_pantalla

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tienda de Servicios Elares")
        self.geometry("600x400")

        # Configurar fondo verde
        self.configure(bg="green")

        # Conectar a la base de datos
        self.db_conection = DatabaseConnection()
        if self.db_conection.conectar_base_de_datos():
            self.db = self.db_conection.get_connection()
        else:
            messagebox.showerror("Error de conexion", "No se pudo conectar")
            self.destroy()

        # Encabezado
        self.header = tk.Label(self, text="Tienda de Servicios Elares", font=("Helvetica", 24), bg="white")
        self.header.pack(pady=10)

        # Botones de encabezado
        self.provider_button = tk.Button(self, text="Encargar", font=("Helvetica", 12), bg="white")
        self.provider_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10)

        self.register_button = tk.Button(self, text="Registrarse", font=("Helvetica", 8), bg="white", command=self.llamar_login)
        self.register_button.pack(side=tk.RIGHT, anchor=tk.N, padx=0)

        # Área de contenido principal
        self.main_frame = tk.Frame(self, bg="blue")
        self.main_frame.pack(pady=10)

        self.all_products_var = tk.StringVar(self)
        self.all_products_var.set("Todos los Productos")
        categorias = self.obtener_categorias()
        self.all_products_menu = tk.OptionMenu(self.main_frame, self.all_products_var, "Todas los Productos", *categorias, command=self.mostrar_productos)
        self.all_products_menu.pack(side=tk.LEFT, anchor=tk.N, padx=10)

        # Lista de productos
        self.product_listbox = tk.Listbox(self.main_frame, bg="white", selectbackground="blue", selectmode=tk.SINGLE,height=20)
        self.product_listbox.pack(side=tk.LEFT, anchor=tk.N, padx=10)

        # Botón "Comprar"
        self.buy_button = tk.Button(self.main_frame, text="Comprar", font=("Helvetica", 10), command=self.comprar_producto)
        self.buy_button.pack(side=tk.LEFT, anchor=tk.N, padx=10)

        # Pie de página
        self.footer = tk.Label(self, bg="green")
        self.footer.pack(side=tk.BOTTOM, fill=tk.X)

        # Mostrar productos en la interfaz gráfica
        self.mostrar_productos()

    def obtener_productos(self, categoria_seleccionada):
        if categoria_seleccionada == "Todas los Productos":
            query = "SELECT productos.NOMBRE, productos.PRECIO, categorias.NOMBRE AS categoria FROM productos JOIN categorias ON productos.ID_CATEGORIA = categorias.ID_CATEGORIA"
        else:
            query = f"SELECT productos.NOMBRE, productos.PRECIO, categorias.NOMBRE AS categoria FROM productos JOIN categorias ON productos.ID_CATEGORIA = categorias.ID_CATEGORIA WHERE categorias.NOMBRE = '{categoria_seleccionada}'"

        with self.db.cursor() as cursor:
            cursor.execute(query)
            productos = cursor.fetchall()
        return productos

    def obtener_categorias(self):
        query = "SELECT NOMBRE FROM categorias"
        with self.db.cursor() as cursor:
            cursor.execute(query)
            categorias = cursor.fetchall()
            categorias = [categoria["NOMBRE"] for categoria in categorias]
        return categorias

    def mostrar_productos(self, *args):
        # Limpiar la lista de productos antes de mostrar los nuevos
        self.product_listbox.delete(0, tk.END)

        categoria_seleccionada = self.all_products_var.get()
        productos = self.obtener_productos(categoria_seleccionada)

        for producto in productos:
            self.product_listbox.insert(tk.END, f"{producto['NOMBRE']} - ${producto['PRECIO']} ({producto['categoria']})")

    def comprar_producto(self):
        # Obtener el índice seleccionado en la lista
        seleccion = self.product_listbox.curselection()

        if seleccion:
            indice = seleccion[0]
            producto_seleccionado = self.product_listbox.get(indice)

            # Puedes realizar acciones adicionales aquí, como agregar el producto al carrito o realizar un proceso de compra.

            # Ejemplo: Mostrar un mensaje de compra exitosa
            mensaje = f"Producto comprado: {producto_seleccionado}"
            messagebox.showinfo("Compra Exitosa", mensaje)
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un producto antes de comprar.")
    def llamar_login(self):
        menu_pantalla()
        
if __name__ == "__main__":
    app = App()
    app.mainloop()