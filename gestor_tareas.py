import tkinter as tk
from tkinter import messagebox

# Función para agregar tarea
def agregar_tarea():
    tarea = entrada.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo está vacío")

# Función para borrar todas las tareas
def borrar_tareas():
    lista_tareas.delete(0, tk.END)

# Función para salir del programa
def salir():
    ventana.quit()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas")

# --- Menú ---
menu_bar = tk.Menu(ventana)
ventana.config(menu=menu_bar)

# Menú Archivo
menu_archivo = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Salir", command=salir)

# Menú Opciones
menu_opciones = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Opciones", menu=menu_opciones)
menu_opciones.add_command(label="Borrar tareas", command=borrar_tareas)

#  --- Frame principal ---
frame = tk.Frame(ventana)
frame.pack(padx=10, pady=10)

# Entry para ingresar tareas
entrada = tk.Entry(frame, width=40)
entrada.pack(side=tk.LEFT, padx=5)

# Botón para agregar tarea
boton_agregar = tk.Button(frame, text="Agregar", command=agregar_tarea)
boton_agregar.pack(side=tk.LEFT)

# Listbox para mostrar tareas
lista_tareas = tk.Listbox(ventana, width=50)
lista_tareas.pack(padx=10, pady=10)

ventana.mainloop()
