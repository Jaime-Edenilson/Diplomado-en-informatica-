import tkinter as tk

def mostrar_saludo():
    nombre=caja_nombre.get()
    edad=caja_edad .get()
    mensaje.config(text="Bienvenido, " +nombre+ "! tienes" +edad+ "!")

ventana=tk.Tk()

ventana.title("Ingrese nombre y edad")
ventana.geometry("600x450")

tk.Label(
    ventana,
    text="Ingrese su nombre y ead",
    font=("Algerian", 16)
).pack(pady=10)

caja_nombre=tk.Entry(
    ventana,
    width=40
)
caja_nombre.pack()

caja_edad=tk.Entry(
    ventana,
    width=40
)
caja_edad.pack()

boton=tk.Button(
    ventana, 
    text="mostrar saludo",
    command=mostrar_saludo
)
boton.pack(pady=20)

mensaje=tk.Label(
    ventana,
        text="",
        font=("Algerian", 20),
        fg="#8F53BA"
)
mensaje.pack()

ventana.mainloop()