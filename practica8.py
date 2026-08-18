import customtkinter as ctk
from tkinter import messagebox


ventana = ctk.CTk()
ventana.title("Mi ventana")
ventana.geometry("1200x700")
ventana.resizable(False, False)

lbl_titulo = ctk.CTkLabel(
    ventana,
    text="Bienvenido a mi ventana",
    font=("Arial", 20)
)
lbl_titulo.pack(pady=20)

txt_usuario = ctk.CTkEntry(
    ventana,
    placeholder_text="Ingrese su nombre",
    width=300
)
txt_usuario.pack(pady=10)


txt_contraseña = ctk.CTkEntry(
    ventana,
    placeholder_text="Ingrese su contraseña",
    width=300,
    show="*"
)
txt_contraseña.pack(pady=10)

ctk.CTkButton(
    ventana,
    text="Iniciar sesión",
    width=200,
    command=iniciar_sesion
).pack(pady=20)

def iniciar_sesion():
    usuario = txt_usuario.get()
    contraseña = txt_contraseña.get()
    messagebox.showinfo("Inicio de sesión", f"Usuario: {usuario}\nContraseña: {contraseña}")


ventana.mainloop()