import tkinter
from tkinter import * 
from tkinter import messagebox
from PIL import Image,ImageTk
from db_conection import DatabaseConnection

def menu_pantalla():
    # Crear la ventana principal
    global pantalla
    
    pantalla=Toplevel()
    pantalla.geometry("300x380")
    pantalla.title("INICIA SESION")
    pantalla.iconbitmap("C:/Users/Alexis Garcia Rojas/Desktop/Proyecto Elares/ELARES/INICIO DE SESION/imgs/logo2.ico")


    # Abrir y redimensionar la imagen de fondo
    imagen_fondo=Image.open("C:/Users/Alexis Garcia Rojas/Desktop/Proyecto Elares/ELARES/INICIO DE SESION/imgs/Elares-login2.png")
    imagen_fondo = imagen_fondo.resize((300, 380))


    # Crear una PhotoImage para la imagen de fondo
    imagen_fondo=ImageTk.PhotoImage(imagen_fondo)

    # Crear un Canvas para la imagen de fondo
    global canvas
    canvas=Canvas(pantalla,width=300,height=380)
    canvas.pack()
    # Mostrar la imagen de fondo en el Canvas
    canvas.create_image(0, 0, anchor=NW, image=imagen_fondo)

    global usuario_verify
    global contrasena_verify
    usuario_verify=StringVar()
    contrasena_verify=StringVar()

    global usuario_entry
    global contrasena_entry
    
    # Crear etiquetas encima de la imagen de fondo
    label1 = Label(pantalla, text="Correo", font=("calibri", 12), fg="black", bg="white")
    usuario_entry=Entry(pantalla,textvariable=usuario_verify)
    usuario_entry.place(relx=0.6, rely=0.5, anchor='center',width=100)
    label1.place(relx=0.5, rely=0.5, anchor='center')

    label2 = Label(pantalla, text="Contraseña", font=("calibri", 12), fg="black", bg="white",width=11,height=1)
    contrasena_entry=Entry(pantalla,show="*",textvariable=contrasena_verify)
    contrasena_entry.place(relx=0.6, rely=0.6, anchor='center', width=100)
    label2.place(relx=0.6, rely=0.6, anchor='center')
    

    #Crear botones
    Button (pantalla,text="Iniciar Sesion", height=1,width=15,command=validacion_datos).place(relx=0.5, rely=0.7, anchor='center')
    Button (pantalla,text="Registrarse", height=1,width=18, command=registrar_ventana ).place(relx=0.5, rely=0.9, anchor='center')

    pantalla.resizable(width=False,height=False)
    # Iniciar el main
    pantalla.mainloop()

#Funciones - Metodos
#def inicio_sesion():
    

def registrar_ventana():
   # Crear la ventana principal
   
    global pantalla2, canvas
    pantalla2=Toplevel(pantalla)
   
    pantalla2.geometry("300x380")
    pantalla2.title("INICIA SESION")
    pantalla2.iconbitmap("C:/Users/Alexis Garcia Rojas/Desktop/Proyecto Elares/ELARES/INICIO DE SESION/imgs/logo2.ico")


    # Abrir y redimensionar la imagen de fondo
    imagen_fondo_registrar=Image.open("C:/Users/Alexis Garcia Rojas/Desktop/Proyecto Elares/ELARES/INICIO DE SESION/imgs/ElaresREGISTRARSE3.png")
    imagen_fondo_registrar = imagen_fondo_registrar.resize((300, 380))


    # Crear una PhotoImage para la imagen de fondo
    imagen_fondo_registrar=ImageTk.PhotoImage(imagen_fondo_registrar)
    

    # Crear un Canvas para la imagen de fondo
    canvas=Canvas(pantalla2,width=300,height=380)
    canvas.pack()
    # Mostrar la imagen de fondo en el Canvas
    canvas.create_image(0, 0, anchor=NW, image=imagen_fondo_registrar)

    # Crear etiquetas encima de la imagen de fondo
    global correoUsuario_entry, contrasenaUsuario_entry, direccionUsuario_entry,nombreUsuario_entry
    correoUsuario_entry=StringVar()
    contrasenaUsuario_entry=StringVar()
    direccionUsuario_entry=StringVar()
    nombreUsuario_entry=StringVar()


    direccionUsuario_entry=Entry(pantalla2)
    direccionUsuario_entry.place(relx=0.6, rely=0.5, anchor='center',width=100)

    nombreUsuario_entry=Entry(pantalla2)
    nombreUsuario_entry.place(relx=0.6, rely=0.4, anchor='center',width=100)

    correoUsuario_entry=Entry(pantalla2)
    correoUsuario_entry.place(relx=0.6, rely=0.6, anchor='center',width=100)

    contrasenaUsuario_entry=Entry(pantalla2,show="*")
    contrasenaUsuario_entry.place(relx=0.6, rely=0.7, anchor='center',width=100)
    
    Button (pantalla2,text="Registrarse", height=1,width=18, command=insert_datos ).place(relx=0.5, rely=0.9, anchor='center')

    pantalla2.resizable(width=False,height=False)

    pantalla2.mainloop()
def registrar():
    # Cerrar la ventana actual antes de abrir la de registro
    
    registrar_ventana()    
def insert_datos():
    db_conexion=DatabaseConnection()
    if db_conexion.conectar_base_de_datos():
        db= db_conexion.get_connection()
        fcursor = db_conexion.get_cursor()
        sql = "INSERT INTO CLIENTES (NOMBRE, DIRECCION, CORREO, CONTRASENA) VALUES (%s, %s, %s, %s)"
        values = (
            nombreUsuario_entry.get(),
            direccionUsuario_entry.get(),
            correoUsuario_entry.get(),
            contrasenaUsuario_entry.get()
        )

        try:
            fcursor.execute(sql, values)
            db.commit()
            messagebox.showinfo(message="Registro exitoso", title="Aviso")
        except Exception as e:
            db.rollback()
            messagebox.showinfo(message=f"No exitoso: {str(e)}", title="Aviso")
        finally:
            db.close()
def validacion_datos():
    db_conexion=DatabaseConnection()
    

    usuario=usuario_verify.get()
    contrasena=contrasena_verify.get()
    
    if db_conexion.conectar_base_de_datos():
        fcursor = db_conexion.get_cursor()
        fcursor.execute("SELECT contrasena FROM Clientes WHERE correo = %s AND contrasena = %s", (usuario, contrasena))
        if fcursor.fetchall():
            messagebox.showinfo(title="Inicio de sesion correcta", message="Usuario y Contraseña correcta")
        else:
            messagebox.showinfo(title="Inicio de sesion incorrecta", message="Usuario y/o Contraseña incorrecta")
            db_conexion.close()

if __name__ =="__main__":
    menu_pantalla()





    










