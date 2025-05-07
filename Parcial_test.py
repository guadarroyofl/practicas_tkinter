# Aplicación Multiuso en Tkinter SIN Programación Orientada a Objetos
# Incluye: Login ficticio, gestor de actividades con checkbox, calculadora básica, menú interactivo

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
        login_frame.pack_forget()  # Oculta el login
        mostrar_principal()       # Muestra el panel principal
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# --------------- Frame Login ---------------
login_frame = tk.Frame(root, bg="#e0e0e0")
login_frame.pack(fill=tk.BOTH, expand=True)

# Etiqueta y campo de usuario
tk.Label(login_frame, text="Usuario:", bg="#e0e0e0").pack(pady=(20, 5))
entry_usuario = tk.Entry(login_frame)
entry_usuario.pack()

# Etiqueta y campo de contraseña
tk.Label(login_frame, text="Contraseña:", bg="#e0e0e0").pack(pady=(10, 5))
entry_password = tk.Entry(login_frame, show="*")
entry_password.pack()

# Botón ingresar
tk.Button(login_frame, text="Ingresar", bg="#4CAF50", fg="white", command=verificar_login).pack(pady=15)

# --------------- Ventana Principal Posterior al Login ---------------
def mostrar_principal():
    root.title("Aplicación Multiuso")
    root.geometry("600x500")
    root.config(bg="#f5f5f5")

    # Menú principal
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

    menu_calculadora = tk.Menu(barra, tearoff=0)
    barra.add_cascade(label="Calculadora", menu=menu_calculadora)
    menu_calculadora.add_command(label="Suma", command=lambda: mostrar_calculadora("suma"))
    menu_calculadora.add_command(label="Resta", command=lambda: mostrar_calculadora("resta"))
    menu_calculadora.add_command(label="Multiplicacion", command=lambda: mostrar_calculadora("multiplicacion"))
    menu_calculadora.add_command(label="Division", command=lambda: mostrar_calculadora("division"))

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
    tk.Label(frame_contenido, text="Bienvenido a la Aplicación Multiuso",
             font=("Segoe UI", 16), bg="#f5f5f5").pack(pady=20)

    # Botones directos de navegación
    tk.Button(frame_contenido, text="Gestor de Actividades", command=mostrar_actividades, bg="#2196F3", fg="white").pack(pady=10)
    tk.Button(frame_contenido, text="Calculadora", command=lambda: mostrar_calculadora("suma"), bg="#4CAF50", fg="white").pack(pady=10)

# --------------- Gestor de Actividades ---------------
def mostrar_entrada_actividad():
    limpiar_contenido()

    entrada = tk.Entry(frame_contenido, width=30, font=("Segoe UI", 12))
    entrada.pack(pady=10)

    def agregar():
        actividad = entrada.get().strip()
        if actividad:
            var = tk.BooleanVar()
            actividad_vars.append((actividad, var))
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

    scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Mostrar actividades
    if not actividad_vars:
        for act in actividades_ficticias:
            var = tk.BooleanVar()
            actividad_vars.append((act, var))

    for texto, var in actividad_vars:
        cb = tk.Checkbutton(scrollable_frame, text=texto, variable=var, font=("Segoe UI", 11))
        cb.pack(anchor='w')

def borrar_todas_actividades():
    if messagebox.askyesno("Confirmar", "¿Borrar todas las actividades?"):
        actividad_vars.clear()
        mostrar_actividades()

# --------------- Calculadora ---------------
def mostrar_calculadora(operacion):
    limpiar_contenido()

    tk.Label(frame_contenido, text=f"Calculadora - {operacion.title()}",
             font=("Segoe UI", 14), bg="#f5f5f5").pack(pady=10)

    entrada_frame = tk.Frame(frame_contenido, bg="#f5f5f5")
    entrada_frame.pack(pady=10)

    entry1 = tk.Entry(entrada_frame, width=10)
    entry2 = tk.Entry(entrada_frame, width=10)
    entry1.grid(row=0, column=0, padx=5)
    entry2.grid(row=0, column=1, padx=5)

    resultado_label = tk.Label(frame_contenido, text="", font=("Segoe UI", 12), bg="#f5f5f5")
    resultado_label.pack(pady=10)

    def calcular():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            if operacion == "suma":
                resultado = num1 + num2
            elif operacion == "resta":
                resultado = num1 - num2
            elif operacion == "multiplicacion":
                resultado = num1 * num2
            elif operacion == "division":
                if num2 == 0:
                    raise ZeroDivisionError
                resultado = num1 / num2
            resultado_label.config(text=f"Resultado: {resultado}")
        except ValueError:
            resultado_label.config(text="Error: Ingresa números válidos")
        except ZeroDivisionError:
            resultado_label.config(text="Error: División por cero")

    tk.Button(frame_contenido, text="Calcular", bg="#4CAF50", fg="white", command=calcular).pack()

# --------------- Ejecutar App ---------------
root.mainloop()
