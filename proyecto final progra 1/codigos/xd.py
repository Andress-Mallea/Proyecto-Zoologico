from tkinter import *
from tkinter import messagebox

def inicio_sesion(main_menu):
    def hola():
        # Verificar si los campos están llenos
        if driver.get() == '' or server.get() == '':
            messagebox.showinfo("ERROR", "Llena los datos antes de ingresar")   
        else:
            # Almacenar los valores en variables
            valor_driver = driver.get()
            valor_server = server.get()
            valor_database = database.get()

            print(f"Driver: {valor_driver}")
            print(f"Server: {valor_server}")
            print(f"Database: {valor_database}")

            # Si todos los campos están llenos, destruir la ventana actual y la principal
            start_sqls.destroy()
            main_menu.destroy()

    def cerrar():
        start_sqls.destroy()

    # Raíz principal
    start_sqls = Toplevel()
    start_sqls.title("Iniciar sesion en SQLServer")
    start_sqls.iconbitmap("BDICON.ico")
    start_sqls.config(bg="#7BBECB")

    # Imagen
    xd = PhotoImage(file="assets/padoru.png")
    label = Button(start_sqls, image=xd)
    label.place(x=300, y=100)
    label.config(cursor="hand2")

    # Ingresar datos
    titulo = Label(start_sqls, text="SQL SERVER", font=("Comic Sans MS", 10))
    titulo.grid(row=0, column=1, padx=10, pady=10)
    
    global driver  # Hacer driver global para acceder dentro de hola
    driver = Entry(start_sqls)
    driver.grid(row=1, column=1, padx=10, pady=10)
    
    nombre_d = Label(start_sqls, text="Driver", font=("Comic Sans MS", 10))
    nombre_d.grid(row=1, column=0, padx=10, pady=10)
    
    global server  # Hacer server global para acceder dentro de hola
    server = Entry(start_sqls)
    server.grid(row=2, column=1, padx=10, pady=10)
    
    nombre_s = Label(start_sqls, text="Server", font=("Comic Sans MS", 10))
    nombre_s.grid(row=2, column=0, padx=10, pady=10)
    
    global database  # Hacer database global para acceder dentro de hola
    database = Entry(start_sqls)
    database.grid(row=3, column=1, padx=10, pady=10)
    
    nombre_db = Label(start_sqls, text="Data base", font=("Comic Sans MS", 10))
    nombre_db.grid(row=3, column=0, padx=10, pady=10)

    # Botón
    boton = Button(start_sqls, text="Confirmar", command=hola)
    boton.grid(row=4, column=0, padx=10, pady=10)
    
    salir = Button(start_sqls, text="Cerrar", command=cerrar)
    salir.grid(row=4, column=1, padx=10, pady=10)

    # Mainloop
    start_sqls.mainloop()

def otra_ventana():
    # Crear y configurar la primera ventana
    global ventana_principal
    ventana_principal = Tk()
    ventana_principal.title("Otra Ventana")
    ventana_principal.iconbitmap("BDICON.ico")
    ventana_principal.config(bg="#FFDDC1")

    def abrir_inicio_sesion():
        inicio_sesion(ventana_principal)

    # Botón para abrir la ventana de inicio de sesión
    boton_inicio = Button(ventana_principal, text="Abrir inicio de sesión", command=abrir_inicio_sesion)
    boton_inicio.pack(padx=10, pady=10)
    
    ventana_principal.mainloop()

# Ejecutar la primera ventana
otra_ventana()
