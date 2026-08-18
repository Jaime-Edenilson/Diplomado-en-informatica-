import tkinter as tk
ventana=tk.Tk()

ventana.title("Mi ventana")
ventana.geometry("400x300")

boton=tk.Button(ventana, text="presiona")
boton.pack(pady=20)




ventana.mainloop()
