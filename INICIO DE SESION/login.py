import tkinter
from tkinter import * 
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql

def menu_pantalla():
    # Crear la ventana principal
    global pantalla
    pantalla=Tk()
    pantalla.geometry("300x380")
    pantalla.title("INICIA SESION")
    pantalla.iconbitmap("C:/Users/Alexis Garcia Rojas/Desktop/Proyecto Elares/INICIO DE SESION/imgs/logo2.ico")


    # Abrir y redimensionar la imagen de fondo
    imagen_fondo=Image.open("C:/Users/Alexis Garcia Rojas/Desktop/Proyecto Elares/INICIO DE SESION/imgs/ELARES1.gif")
    imagen_fondo = imagen_fondo.resize((300, 380))


    # Crear una PhotoImage para la imagen de fondo
    imagen_fondo=ImageTk.PhotoImage(imagen_fondo)

    # Crear un Canvas para la imagen de fondo
    canvas=Canvas(pantalla,width=300,height=380)
    canvas.pack()
    # Mostrar la imagen de fondo en el Canvas
    canvas.create_image(0, 0, anchor=NW, image=imagen_fondo)
    # Crear etiquetas encima de la imagen de fondo
    """label1 = Label(pantalla, text="Usuario", font=("calibri", 15), fg="black", bg="white")
    label1.place(relx=0.5, rely=0.2, anchor='center')

    label2 = Label(pantalla, text="Contraseña", font=("calibri", 15), fg="black", bg="white")
    label2.place(relx=0.5, rely=0.4, anchor='center')"""

    #Crear botones
    Button (text="Iniciar Sesion", height=3,width=30,command=inicio_sesion).place(relx=0.5, rely=0.6, anchor='center')
    Button (text="Registrarse", height=3,width=30 ).place(relx=0.5, rely=0.9, anchor='center')

    # Iniciar el main
    pantalla.mainloop()

#Funciones - Metodos
def inicio_sesion():
    global pantalla1
    pantalla1= Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de Sesion")
    pantalla1.iconbitmap("C:/Users/Alexis Garcia Rojas/Desktop/Proyecto Elares/INICIO DE SESION/imgs/logo2.ico")

    Label(pantalla1,text="Por favor ingrese su usuario y contraseña a continuacion").pack()
    Label(pantalla1,text="").pack()

    global usuario_verify
    global contrasena_verify
    usuario_verify=StringVar()
    contrasena_verify=StringVar()

    global usuario_entry
    global contrasena_entry
    Label(pantalla1,text="Usuario").pack()
    usuario_entry=Entry(pantalla1,textvariable=usuario_verify)
    usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1,text="Contraseña").pack()
    contrasena_entry=Entry(pantalla1,textvariable=contrasena_verify)
    contrasena_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1,text="Iniciar Sesion").pack()

menu_pantalla()





    










