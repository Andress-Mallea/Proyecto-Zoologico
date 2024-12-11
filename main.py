from tkinter import *

#raiz principal
main = Tk()
main.title("Base de datos god")
main.iconbitmap("BDICON.ico")
#main.geometry("1280x720")
main.config(bg="#7BBECB")

#fondo rojo
elframe = Frame()
elframe.pack(fill="both", expand="true")
elframe.config(bg="red")
elframe.config(width="650", height="650")

#imagen
xd = PhotoImage(file="padoru.png")
label = Label(image=xd)
label.place(x="300",y="100")
label.config(cursor="hand2")

#Ingresar datos
titulo = Label(elframe, text="BASE DE DATOS", font=("Comic Sans SN", 10))
titulo.grid(row="0",column="1", padx=10, pady=10)
driver = Entry(elframe)
driver.grid(row="1",column="1", padx=10, pady=10)
nombre_d = Label(elframe, text="Driver: ", font=("Comic Sans SN", 10))
nombre_d.grid(row="1",column="0", padx=10, pady=10)
server = Entry(elframe)
server.grid(row="2",column="1", padx=10, pady=10)
nombre_s = Label(elframe, text="server: ", font=("Comic Sans SN", 10))
nombre_s.grid(row="2",column="0", padx=10, pady=10)
database = Entry(elframe)
database.grid(row="3",column="1", padx=10, pady=10)
nombre_db = Label(elframe, text="Data base: ", font=("Comic Sans SN", 10))
nombre_db.grid(row="3",column="0", padx=10, pady=10)

#main
main.mainloop()