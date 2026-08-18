# ==========================
# PASO 1 - IMPORTACIONES
# ==========================
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

# ==========================
# CONFIGURACIÓN DE LA VENTANA
# ==========================
ctk.set_appearance_mode("dark")          # Opciones: "dark", "light", "system"
ctk.set_default_color_theme("blue")      # Opciones: "blue", "green", "dark-blue"

# ===================================
# DICCIONARIO CON USUARIOS REGISTRADOS
# ===================================
usuarios = {
    "admin": "12345",
    "profesor": "abc123",
    "estudiante": "2026"
}

# ==============================
# FUNCIÓN PARA INICIAR SESIÓN
# ==============================
def iniciar_sesion():
    usuario = txt_usuario.get()
    clave = txt_clave.get()

    # Validación de campos vacíos
    if not usuario or not clave:
        messagebox.showwarning("Advertencia", "Debe llenar todos los campos")
        return

    if usuario in usuarios and usuarios[usuario] == clave:
        messagebox.showinfo("Acceso", f"Bienvenido {usuario}")
        ventana.destroy()
        menu_principal(usuario)
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# ======================================
# FUNCIÓN PARA ABRIR EL MENÚ PRINCIPAL
# ======================================
def menu_principal(nombre):
    menu = ctk.CTk()
    menu.title("Sistema")
    menu.geometry("600x400")

    ctk.CTkLabel(
        menu,
        text=f"Bienvenido {nombre}",
        font=("Arial", 24, "bold")
    ).pack(pady=40)

    ctk.CTkButton(menu, text="Ventas", width=200).pack(pady=10)
    ctk.CTkButton(menu, text="Inventario", width=200).pack(pady=10)
    ctk.CTkButton(menu, text="Clientes", width=200).pack(pady=10)

    ctk.CTkButton(menu, text="Salir", width=200, command=menu.destroy).pack(pady=20)

    menu.mainloop()

# ===========================
# PASO 2 - CREACIÓN DE LA VENTANA
# ===========================
ventana = ctk.CTk()
ventana.title("Inicio de Sesión")
ventana.geometry("450x450")
ventana.resizable(False, False)

# Fondo atractivo (opcional, coloca tu imagen en la carpeta del proyecto)
try:
    fondo = ctk.CTkImage(Image.open("fondo.jpg"), size=(450, 450))
    ctk.CTkLabel(ventana, image=fondo, text="").place(x=0, y=0)
except:
    pass  # Si no hay imagen, no se muestra el fondo

# ===================
# TÍTULO
# ===================
ctk.CTkLabel(
    ventana,
    text="INICIAR SESIÓN",
    font=("Arial", 28, "bold")
).pack(pady=30)

# ===================
# CAJA DE USUARIO
# ===================
txt_usuario = ctk.CTkEntry(
    ventana,
    width=250,
    placeholder_text="Usuario"
)
txt_usuario.pack(pady=15)

# =======================
# CAJA CONTRASEÑA
# =======================
txt_clave = ctk.CTkEntry(
    ventana,
    width=250,
    placeholder_text="Contraseña",
    show="*"
)
txt_clave.pack(pady=15)

# =======================
# BOTÓN MOSTRAR/OCULTAR CONTRASEÑA
# =======================
def toggle_password():
    if txt_clave.cget("show") == "*":
        txt_clave.configure(show="")
        btn_toggle.configure(text="Ocultar")
    else:
        txt_clave.configure(show="*")
        btn_toggle.configure(text="Mostrar")

btn_toggle = ctk.CTkButton(
    ventana,
    text="Mostrar",
    width=100,
    command=toggle_password
)
btn_toggle.pack(pady=5)

# ======================
# BOTÓN INGRESAR
# ======================
ctk.CTkButton(
    ventana,
    text="Ingresar",
    width=250,
    command=iniciar_sesion
).pack(pady=25)

# ==========================
# INFORMACIÓN DEL EJEMPLO
# ==========================
ctk.CTkLabel(
    ventana,
    text="Usuario: admin\nContraseña: 12345",
    font=("Arial", 12)
).pack(pady=10)

# =====================
# INICIA EL PROGRAMA
# =====================
ventana.mainloop()
