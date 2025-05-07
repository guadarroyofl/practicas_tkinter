import tkinter as tk
from tkinter import messagebox

class GestorTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        self.crear_menu()
        self.crear_widgets()

    def crear_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        menu_archivo = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Salir", command=self.root.quit)

        menu_opciones = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Opciones", menu=menu_opciones)
        menu_opciones.add_command(label="Borrar tareas", command=self.borrar_tareas)

    def crear_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        self.entrada = tk.Entry(frame, width=40)
        self.entrada.pack(side=tk.LEFT, padx=5)

        boton_agregar = tk.Button(frame, text="Agregar", command=self.agregar_tarea)
        boton_agregar.pack(side=tk.LEFT)

        self.lista_tareas = tk.Listbox(self.root, width=50)
        self.lista_tareas.pack(padx=10, pady=10)

    def agregar_tarea(self):
        tarea = self.entrada.get()
        if tarea:
            self.lista_tareas.insert(tk.END, tarea)
            self.entrada.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "El campo está vacío")

    def borrar_tareas(self):
        self.lista_tareas.delete(0, tk.END)

# Crear instancia y correr la app
if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareasApp(root)
    root.mainloop()
