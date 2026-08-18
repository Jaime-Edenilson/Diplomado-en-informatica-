import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

usuarios = {
    "admin": "12345",
    "profesor": "abc123",
    "estudiante": "2026"
}

def iniciar_sesion():
    usuario = txt_usuario.get().strip()
    clave = txt_clave.get().strip()

    if usuario in usuarios and usuarios[usuario] == clave:
        messagebox.showinfo("Acceso Concedido", f"¡Bienvenido/a al sistema, {usuario}!")
        ventana.withdraw()
        menu_principal(usuario)
    else:
        messagebox.showerror("Error de Autenticación", "Usuario o contraseña incorrectos.")
        txt_clave.delete(0, 'end')

def menu_principal(nombre):
    menu = ctk.CTkToplevel()
    menu.title("Sistema de Gestión")
    menu.geometry("600x500")
    menu.resizable(False, False)

    def al_cerrar_menu():
        ventana.destroy()

    menu.protocol("WM_DELETE_WINDOW", al_cerrar_menu)

    frame_menu = ctk.CTkFrame(menu, corner_radius=15)
    frame_menu.pack(pady=20, padx=20, fill="both", expand=True)

    ctk.CTkLabel(
        frame_menu, 
        text=f"📌 Panel Principal\nBienvenido, {nombre}", 
        font=("Arial", 22, "bold")
    ).pack(pady=25)

    def abrir_modulo(modulo):
        messagebox.showinfo("Módulo", f"Accediendo al módulo de {modulo}...")

    ctk.CTkButton(
        frame_menu, 
        text="🛒 Módulo de Ventas", 
        width=250, 
        height=38,
        command=lambda: abrir_modulo("Ventas")
    ).pack(pady=10)

    ctk.CTkButton(
        frame_menu, 
        text="📦 Módulo de Inventario", 
        width=250, 
        height=38,
        command=lambda: abrir_modulo("Inventario")
    ).pack(pady=10)

    ctk.CTkButton(
        frame_menu, 
        text="👥 Módulo de Clientes", 
        width=250, 
        height=38,
        command=lambda: abrir_modulo("Clientes")
    ).pack(pady=10)

    def cerrar_sesion():
        menu.destroy()
        txt_usuario.delete(0, 'end')
        txt_clave.delete(0, 'end')
        ventana.deiconify()

    ctk.CTkButton(
        frame_menu, 
        text="🚪 Cerrar Sesión", 
        width=250, 
        height=38,
        fg_color="#D32F2F", 
        hover_color="#9A0007", 
        command=cerrar_sesion
    ).pack(pady=20)

ventana = ctk.CTk()
ventana.title("Sistema - Inicio de Sesión")
ventana.geometry("450x520")
ventana.resizable(False, False)

card_frame = ctk.CTkFrame(ventana, corner_radius=15)
card_frame.pack(pady=25, padx=25, fill="both", expand=True)

ctk.CTkLabel(
    card_frame, 
    text="🔐 INICIAR SESIÓN", 
    font=("Arial", 24, "bold")
).pack(pady=(25, 15))

txt_usuario = ctk.CTkEntry(
    card_frame, 
    width=280, 
    height=40,
    placeholder_text="Nombre de usuario"
)
txt_usuario.pack(pady=12)

txt_clave = ctk.CTkEntry(
    card_frame, 
    width=280, 
    height=40,
    placeholder_text="Contraseña", 
    show="*"
)
txt_clave.pack(pady=12)

btn_ingresar = ctk.CTkButton(
    card_frame, 
    text="Ingresar al Sistema", 
    width=280, 
    height=40,
    font=("Arial", 14, "bold"),
    command=iniciar_sesion
)
btn_ingresar.pack(pady=20)

info_frame = ctk.CTkFrame(card_frame, fg_color="transparent")
info_frame.pack(pady=10)

ctk.CTkLabel(
    info_frame, 
    text="💡 Credenciales de prueba:\nadmin / 12345  •  profesor / abc123  •  estudiante / 2026", 
    font=("Arial", 11),
    text_color="gray"
).pack()

ventana.mainloop()