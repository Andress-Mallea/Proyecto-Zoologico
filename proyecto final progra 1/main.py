from tkinter import *

#raiz principal
main = Tk()
main.title("Base de datos god")
main.iconbitmap("BDICON.ico")
main.geometry("1280x720")
main.config(bg="#7BBECB")

#fondo rojo
elframe = Frame()
elframe.pack(fill="both", expand="false")
elframe.config(bg="red")
elframe.config(width="650", height="650")

#imagen
xd = PhotoImage(file="padoru.png")
label = Label(image=xd)
label.place(x="100",y="100")
label.config(cursor="hand2")

#Ingresar datos
i = Entry(elframe)
i.place(x=800,y=200)
main.mainloop()