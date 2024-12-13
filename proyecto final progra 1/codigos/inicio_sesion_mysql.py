from tkinter import *
from tkinter import messagebox
def inicio_sesion(main_menu):
    def hola():
        if user.get() == '' or password.get() == '':
            messagebox.showinfo("ERROR", "Llena los datos antes de ingresar")   
        else:
            a = user.get()
            b = password.get()
            print(a)
            print(b)
            start_sqls.destroy()
            main_menu.destroy()
    def cerrar():
          start_sqls.destroy()
    def mostrar_password():
      if password.cget('show') == '*':
            password.config(show='')
      else:
            password.config(show='*')
    #raiz principal
    start_sqls = Toplevel()
    start_sqls.title("Iniciar sesion en Mysql")
    start_sqls.iconbitmap("BDICON.ico")
    #main.geometry("1280x720")
    start_sqls.config(bg="#7BBECB")
    
    #imagen
    xd = PhotoImage(file="assets/padoru.png")
    label = Button(start_sqls ,image=xd)
    label.place(x="300",y="100")
    label.config(cursor="hand2")

    #Ingresar datos
    titulo = Label(start_sqls, text="MY SQL", font=("Comic Sans SN", 10))
    titulo.grid(row="0",column="1", padx=10, pady=10)
    global user
    user = Entry(start_sqls)
    user.grid(row="1",column="1", padx=10, pady=10)
    n_user = Label(start_sqls, text="User", font=("Comic Sans SN", 10))
    n_user.grid(row="1",column="0", padx=10, pady=10)
    contrasena = False
    global password
    password = Entry(start_sqls)
    password.grid(row="2",column="1", padx=10, pady=10)
    p = Label(start_sqls, text="Password", font=("Comic Sans SN", 10))
    p.grid(row="2",column="0", padx=10, pady=10)
    eye = PhotoImage(file="assets/eye.png")
    eye_l = Button(start_sqls ,image=eye, command=mostrar_password)
    eye_l.grid(row="2",column="2", padx=0.5, pady=0.5)
    eye_l.config(cursor="hand2")
    if contrasena == True:
            password.config()
    else:
            password.config(show="*")

    #boton
    boton = Button(start_sqls, text="Confirmar", command=hola)
    boton.grid(row="3",column="0", padx=10, pady=10)
    salir = Button(start_sqls, text="Cerrar", command=cerrar)
    salir.grid(row="3",column="1", padx=10, pady=10)
    #main
    start_sqls.mainloop()