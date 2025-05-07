# Aplicación Multiuso en Tkinter SIN Programación Orientada a Objetos
# Incluye: Login ficticio, gestor de actividades, calculadora básica

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
    root.geometry("600x450")
    root.config(bg="#f5f5f5")

    # Menú principal
    barra = tk.Menu(root)
    root.config(menu=barra)

    menu_archivo = tk.Menu(barra, tearoff=0)
    barra.add_cascade(label="Archivo", menu=menu_archivo)
    menu_archivo.add_command(label="Salir", command=root.quit)

    menu_actividades = tk.Menu(barra, tearoff=0)
    barra.add_cascade(label="Actividades", menu=menu_actividades)
    menu_actividades.add_command(label="Gestor de Actividades", command=mostrar_actividades)

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
             font=("Segoe UI", 16), bg="#f5f5f5").pack(pady=100)

# --------------- Gestor de Actividades ---------------
def mostrar_actividades():
    limpiar_contenido()

    entrada = tk.Entry(frame_contenido, width=30, font=("Segoe UI", 12))
    entrada.pack(pady=10)

    def agregar():
        actividad = entrada.get().strip()
        if actividad:
            lista.insert(tk.END, actividad)
            entrada.delete(0, tk.END)
        else:
            messagebox.showwarning("Vacío", "Ingrese una actividad.")

    tk.Button(frame_contenido, text="Agregar", command=agregar, bg="#4CAF50", fg="white").pack()

    lista_frame = tk.Frame(frame_contenido)
    lista_frame.pack(pady=10)

    global lista
    lista = tk.Listbox(lista_frame, width=40, height=10, font=("Segoe UI", 11))
    lista.grid(row=0, column=0)

    scrollbar = tk.Scrollbar(lista_frame, command=lista.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')
    lista.config(yscrollcommand=scrollbar.set)

    botones = tk.Frame(frame_contenido, bg="#f5f5f5")
    botones.pack(pady=10)

    def editar():
        seleccion = lista.curselection()
        if not seleccion:
            return
        indice = seleccion[0]
        original = lista.get(indice)
        nuevo = simpledialog.askstring("Editar", "Editar actividad:", initialvalue=original)
        if nuevo:
            lista.delete(indice)
            lista.insert(indice, nuevo)

    def eliminar():
        seleccion = lista.curselection()
        if seleccion:
            lista.delete(seleccion[0])

    def borrar_todo():
        if messagebox.askyesno("Borrar Todo", "¿Estás seguro?"):
            lista.delete(0, tk.END)

    tk.Button(botones, text="Editar", bg="#2196F3", fg="white", command=editar).pack(side=tk.LEFT, padx=5)
    tk.Button(botones, text="Eliminar", bg="#f44336", fg="white", command=eliminar).pack(side=tk.LEFT, padx=5)
    tk.Button(botones, text="Borrar Todo", bg="#9E9E9E", fg="white", command=borrar_todo).pack(side=tk.LEFT, padx=5)

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
