# Aplicación de Gestión de Actividades en Tkinter SIN Programación Orientada a Objetos
# Incluye: Login ficticio, gestor de actividades con checkbox, edición y eliminación individual de tareas

import tkinter as tk
from tkinter import messagebox, simpledialog

# --------------- Variables globales ---------------
usuario_valido = "admin"
password_valido = "1234"

# --------------- Ventana Principal ---------------
root = tk.Tk()
root.title("Login")
root.geometry("300x180")
root.configure(bg="#e0e0e0")

# Lista de actividades simuladas si no hay ninguna ingresada
actividades_ficticias = ["Estudiar Python", "Lavar la ropa", "Sacar la basura"]
actividad_vars = []

# --------------- Funciones del Login ---------------
def verificar_login():
    usuario = entry_usuario.get()
    password = entry_password.get()
    if usuario == usuario_valido and password == password_valido:
        login_frame.pack_forget()
        mostrar_principal()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# --------------- Frame Login ---------------
login_frame = tk.Frame(root, bg="#e0e0e0")
login_frame.pack(fill=tk.BOTH, expand=True)

tk.Label(login_frame, text="Usuario:", bg="#e0e0e0").pack(pady=(20, 5))
entry_usuario = tk.Entry(login_frame)
entry_usuario.pack()

tk.Label(login_frame, text="Contraseña:", bg="#e0e0e0").pack(pady=(10, 5))
entry_password = tk.Entry(login_frame, show="*")
entry_password.pack()

tk.Button(login_frame, text="Ingresar", bg="#4CAF50", fg="white", command=verificar_login).pack(pady=15)

# --------------- Ventana Principal Posterior al Login ---------------
def mostrar_principal():
    root.title("Gestor de Actividades")
    root.geometry("600x500")
    root.config(bg="#f5f5f5")

    barra = tk.Menu(root)
    root.config(menu=barra)

    menu_archivo = tk.Menu(barra, tearoff=0)
    barra.add_cascade(label="Archivo", menu=menu_archivo)
    menu_archivo.add_command(label="Salir", command=root.quit)

    menu_actividades = tk.Menu(barra, tearoff=0)
    barra.add_cascade(label="Actividades", menu=menu_actividades)
    menu_actividades.add_command(label="Ver Actividades", command=mostrar_actividades)
    menu_actividades.add_command(label="Agregar Nueva", command=mostrar_entrada_actividad)
    menu_actividades.add_command(label="Borrar Todas", command=borrar_todas_actividades)

    global frame_contenido
    frame_contenido = tk.Frame(root, bg="#f5f5f5")
    frame_contenido.pack(fill=tk.BOTH, expand=True)

    mostrar_inicio()

# --------------- Funciones Compartidas ---------------
def limpiar_contenido():
    for widget in frame_contenido.winfo_children():
        widget.destroy()

def mostrar_inicio():
    limpiar_contenido()
    tk.Label(frame_contenido, text="Bienvenido al Gestor de Actividades",
             font=("Segoe UI", 16), bg="#f5f5f5").pack(pady=20)

    tk.Button(frame_contenido, text="Ver Actividades", command=mostrar_actividades, bg="#2196F3", fg="white").pack(pady=10)
    tk.Button(frame_contenido, text="Agregar Nueva", command=mostrar_entrada_actividad, bg="#4CAF50", fg="white").pack(pady=10)

# --------------- Gestor de Actividades ---------------
def mostrar_entrada_actividad():
    limpiar_contenido()

    entrada = tk.Entry(frame_contenido, width=30, font=("Segoe UI", 12))
    entrada.pack(pady=10)

    def agregar():
        actividad = entrada.get().strip()
        if actividad:
            var = tk.BooleanVar()
            actividad_vars.append([actividad, var])
            entrada.delete(0, tk.END)
            mostrar_actividades()
        else:
            messagebox.showwarning("Vacío", "Ingrese una actividad.")

    tk.Button(frame_contenido, text="Agregar", command=agregar, bg="#4CAF50", fg="white").pack()

def mostrar_actividades():
    limpiar_contenido()
    tk.Label(frame_contenido, text="Lista de Actividades", font=("Segoe UI", 14), bg="#f5f5f5").pack(pady=10)

    lista_frame = tk.Frame(frame_contenido)
    lista_frame.pack()

    canvas = tk.Canvas(lista_frame, height=200, width=400)
    scrollbar = tk.Scrollbar(lista_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    if not actividad_vars:
        for act in actividades_ficticias:
            var = tk.BooleanVar()
            actividad_vars.append([act, var])

    for i, (texto, var) in enumerate(actividad_vars):
        fila = tk.Frame(scrollable_frame)
        fila.pack(anchor='w', pady=2, fill='x')

        cb = tk.Checkbutton(fila, text=texto, variable=var, font=("Segoe UI", 11))
        cb.pack(side="left", padx=5)

        tk.Button(fila, text="Editar", command=lambda idx=i: editar_actividad(idx), bg="#FFC107").pack(side="left", padx=5)
        tk.Button(fila, text="Eliminar", command=lambda idx=i: eliminar_actividad(idx), bg="#F44336", fg="white").pack(side="left", padx=5)

def editar_actividad(indice):
    nueva = simpledialog.askstring("Editar actividad", "Modificar actividad:", initialvalue=actividad_vars[indice][0])
    if nueva:
        actividad_vars[indice][0] = nueva
        mostrar_actividades()

def eliminar_actividad(indice):
    if messagebox.askyesno("Eliminar", "¿Deseas eliminar esta actividad?"):
        del actividad_vars[indice]
        mostrar_actividades()

def borrar_todas_actividades():
    if messagebox.askyesno("Confirmar", "¿Borrar todas las actividades?"):
        actividad_vars.clear()
        mostrar_actividades()

# --------------- Ejecutar App ---------------
root.mainloop()
