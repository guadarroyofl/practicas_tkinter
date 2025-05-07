# ===============================================
# Aplicación de Gestión de Actividades en Tkinter SIN POO
# ===============================================
#
# Conceptos clave:
# - Tkinter: librería estándar para crear interfaces gráficas en Python.
# - root: ventana principal de la aplicación (instancia de Tk).
# - Frame: contenedor para organizar otros widgets (botones, entradas, etc).
# - pack(), grid(), place(): métodos de posicionamiento de widgets. Aquí usamos pack principalmente.
# - Entry: campo de texto para que el usuario ingrese información.
# - BooleanVar: variable booleana usada para checkboxes.
# - Menu: barra superior que contiene opciones desplegables.
# - messagebox: muestra mensajes de alerta, error o confirmación.
# - simpledialog: muestra cuadros de entrada simples para editar datos.
#
# Estructura general:
# - Al iniciar se muestra una pantalla de login.
# - Si las credenciales son válidas, se muestra la ventana principal con el gestor de actividades.
# - Desde el menú se pueden ver, agregar, editar o eliminar tareas.
# ===============================================================

import tkinter as tk
from tkinter import messagebox, simpledialog

# --------------- Variables globales ---------------
usuario_valido = "admin"  # usuario permitido
password_valido = "1234"  # contraseña permitida

# Lista de actividades ficticias si no hay ingresadas por el usuario
actividades_ficticias = ["Estudiar Python", "Lavar la ropa", "Sacar la basura"]
actividad_vars = []  # lista que guarda [actividad, estado_checkbox]

# --------------- Crear ventana principal ---------------
root = tk.Tk()  # instancia de la ventana principal
root.title("Login")  # título de la ventana
root.geometry("300x180")  # tamaño inicial
root.configure(bg="#e0e0e0")  # color de fondo

# --------------- Funciones del Login ---------------
def verificar_login():
    # obtiene los valores de los campos de texto
    usuario = entry_usuario.get()
    password = entry_password.get()
    # si coinciden con los datos válidos, carga la ventana principal
    if usuario == usuario_valido and password == password_valido:
        login_frame.pack_forget()  # oculta el frame de login
        mostrar_principal()  # llama a la función que muestra el menú principal
        messagebox.showinfo("EXITOSO","Login success")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")  # muestra error

# --------------- Frame de Login ---------------
login_frame = tk.Frame(root, bg="#e0e0e0")  # contenedor del login
login_frame.pack()  # lo mostramos

# Etiqueta y campo de texto para el usuario
tk.Label(login_frame, text="Usuario:", bg="#e0e0e0").pack(pady=(20, 5))
entry_usuario = tk.Entry(login_frame)
entry_usuario.pack()

# Etiqueta y campo de texto para la contraseña
# el parámetro show="*" oculta los caracteres ingresados
tk.Label(login_frame, text="Contraseña:", bg="#e0e0e0").pack(pady=(10, 5))
entry_password = tk.Entry(login_frame, show="*")
entry_password.pack()

# Botón de ingreso
# llama a la función verificar_login al hacer clic
tk.Button(login_frame, text="Ingresar", bg="#4CAF50", fg="white", command=verificar_login).pack(pady=15)

# --------------- Mostrar la ventana principal ---------------
def mostrar_principal():
    root.title("Gestor de Actividades")  # cambia el título
    root.geometry("600x500")  # nuevo tamaño
    root.config(bg="#f5f5f5")  # color de fondo

    # Barra de menú principal
    barra = tk.Menu(root)
    root.config(menu=barra)

    # Menú Archivo (contiene opción salir)
    menu_archivo = tk.Menu(barra, tearoff=0)
    barra.add_cascade(label="Archivo", menu=menu_archivo)
    menu_archivo.add_command(label="Salir", command=root.quit)

    # Menú Actividades con submenús
    menu_actividades = tk.Menu(barra, tearoff=0)
    barra.add_cascade(label="Actividades", menu=menu_actividades)
    menu_actividades.add_command(label="Ver Actividades", command=mostrar_actividades)
    menu_actividades.add_command(label="Agregar Nueva", command=mostrar_entrada_actividad)
    menu_actividades.add_command(label="Borrar Todas", command=borrar_todas_actividades)

    # Creamos un frame contenedor para la zona central
    global frame_contenido
    frame_contenido = tk.Frame(root, bg="#f5f5f5")
    frame_contenido.pack(fill=tk.BOTH, expand=True)

    mostrar_inicio()  # muestra mensaje de bienvenida y botones

# --------------- Funciones compartidas ---------------
def limpiar_contenido():
    # elimina todos los widgets del frame principal
    for widget in frame_contenido.winfo_children():
        widget.destroy()

def mostrar_inicio():
    limpiar_contenido()
    # mensaje de bienvenida
    tk.Label(frame_contenido, text="Bienvenido al Gestor de Actividades",
             font=("Segoe UI", 16), bg="#f5f5f5").pack(pady=20)
    # botones de acceso rápido
    tk.Button(frame_contenido, text="Ver Actividades", command=mostrar_actividades, bg="#2196F3", fg="white").pack(pady=10)
    tk.Button(frame_contenido, text="Agregar Nueva", command=mostrar_entrada_actividad, bg="#4CAF50", fg="white").pack(pady=10)

# --------------- Agregar nueva actividad ---------------
def mostrar_entrada_actividad():
    limpiar_contenido()

    entrada = tk.Entry(frame_contenido, width=30, font=("Segoe UI", 12))  # campo de texto
    entrada.pack(pady=10)

    def agregar():
        actividad = entrada.get().strip()
        if actividad:
            var = tk.BooleanVar()  # crea una variable booleana para el checkbox
            actividad_vars.append([actividad, var])  # agrega la actividad a la lista
            entrada.delete(0, tk.END)  # limpia el campo
            mostrar_actividades()  # recarga la vista de actividades
        else:
            messagebox.showwarning("Vacío", "Ingrese una actividad.")  # advertencia

    tk.Button(frame_contenido, text="Agregar", command=agregar, bg="#4CAF50", fg="white").pack()

# --------------- Ver actividades existentes ---------------
def mostrar_actividades():
    limpiar_contenido()

    tk.Label(frame_contenido, text="Lista de Actividades", font=("Segoe UI", 14), bg="#f5f5f5").pack(pady=10)

    lista_frame = tk.Frame(frame_contenido)  # contenedor para la lista y scrollbar
    lista_frame.pack()

    canvas = tk.Canvas(lista_frame, height=200, width=400)  # área de scroll
    scrollbar = tk.Scrollbar(lista_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)  # frame dentro del canvas

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # si no hay actividades ingresadas, usamos las ficticias
    if not actividad_vars:
        for act in actividades_ficticias:
            var = tk.BooleanVar()
            actividad_vars.append([act, var])

    # mostramos cada actividad como checkbox con botones
    for i, (texto, var) in enumerate(actividad_vars):
        fila = tk.Frame(scrollable_frame)
        fila.pack(anchor='w', pady=2, fill='x')

        cb = tk.Checkbutton(fila, text=texto, variable=var, font=("Segoe UI", 11))
        cb.pack(side="left", padx=5)

        # botón para editar
        tk.Button(fila, text="Editar", command=lambda idx=i: editar_actividad(idx), bg="#FFC107").pack(side="left", padx=5)
        # botón para eliminar
        tk.Button(fila, text="Eliminar", command=lambda idx=i: eliminar_actividad(idx), bg="#F44336", fg="white").pack(side="left", padx=5)

# --------------- Editar o eliminar individualmente ---------------
def editar_actividad(indice):
    # muestra un cuadro de entrada con el texto actual
    nueva = simpledialog.askstring("Editar actividad", "Modificar actividad:", initialvalue=actividad_vars[indice][0])
    if nueva:
        actividad_vars[indice][0] = nueva  # actualiza el texto
        mostrar_actividades()

def eliminar_actividad(indice):
    if messagebox.askyesno("Eliminar", "¿Deseas eliminar esta actividad?"):
        del actividad_vars[indice]  # borra la actividad de la lista
        mostrar_actividades()

# --------------- Borrar todas las actividades ---------------
def borrar_todas_actividades():
    if messagebox.askyesno("Confirmar", "¿Borrar todas las actividades?"):
        actividad_vars.clear()  # borra toda la lista
        mostrar_actividades()

# --------------- Iniciar la aplicación ---------------
root.mainloop()  # inicia el bucle principal de la app
