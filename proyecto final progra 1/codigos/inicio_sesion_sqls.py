from tkinter import *
from tkinter import messagebox
def inicio_sesion(main_menu):
    def hola():
        if driver.get() == '' or server.get() == '':
            messagebox.showinfo("ERROR", "Llena los datos antes de ingresar")   
        else:
            a = driver.get()
            b = server.get()
            print(a)
            print(b)
            start_sqls.destroy()
            main_menu.destroy()
    def cerrar():
        start_sqls.destroy()
    #raiz principal
    start_sqls = Toplevel()
    start_sqls.title("Iniciar sesion en SQLServer")
    start_sqls.iconbitmap("BDICON.ico")
    start_sqls.config(bg="#7BBECB")
    
    #imagen
    xd = PhotoImage(file="assets/padoru.png")
    label = Button(start_sqls ,image=xd)
    label.place(x="300",y="100")
    label.config(cursor="hand2")

    #Ingresar datos
    titulo = Label(start_sqls, text="SQL SERVER", font=("Comic Sans SN", 10))
    titulo.grid(row="0",column="1", padx=10, pady=10)
    global driver
    driver = Entry(start_sqls)
    driver.grid(row="1",column="1", padx=10, pady=10)
    nombre_d = Label(start_sqls, text="Driver", font=("Comic Sans SN", 10))
    nombre_d.grid(row="1",column="0", padx=10, pady=10)
    global server
    server = Entry(start_sqls)
    server.grid(row="2",column="1", padx=10, pady=10)
    nombre_s = Label(start_sqls, text="Server", font=("Comic Sans SN", 10))
    nombre_s.grid(row="2",column="0", padx=10, pady=10)

    #boton
    boton = Button(start_sqls, text="Confirmar", command=hola)
    boton.grid(row="3",column="0", padx=10, pady=10)
    salir = Button(start_sqls, text="Cerrar", command=cerrar)
    salir.grid(row="3",column="1", padx=10, pady=10)
    #main
    start_sqls.mainloop()