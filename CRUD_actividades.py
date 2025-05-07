import tkinter as tk
from tkinter import messagebox, simpledialog

class GestorActividades:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Actividades")

        # Estilo general
        self.root.configure(bg="#f0f0f0")
        self.root.geometry("500x400")

        self.crear_menu()
        self.crear_widgets()

    def crear_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # Menú Archivo
        archivo_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
        archivo_menu.add_command(label="Salir", command=self.root.quit)

        # Menú Edición
        edicion_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Opciones", menu=edicion_menu)
        edicion_menu.add_command(label="Borrar todas", command=self.borrar_todo)

    def crear_widgets(self):
        # Frame superior: entrada y botón agregar (pack)
        frame_superior = tk.Frame(self.root, bg="#f0f0f0")
        frame_superior.pack(pady=10)

        self.entrada = tk.Entry(frame_superior, width=30, font=("Segoe UI", 12))
        self.entrada.pack(side=tk.LEFT, padx=5)

        boton_agregar = tk.Button(frame_superior, text="Agregar", bg="#4CAF50", fg="white",
                                  font=("Segoe UI", 10), command=self.agregar)
        boton_agregar.pack(side=tk.LEFT, padx=5)

        # Frame medio: listbox con scrollbar (grid)
        frame_medio = tk.Frame(self.root, bg="#f0f0f0")
        frame_medio.pack(pady=5)

        self.lista = tk.Listbox(frame_medio, width=40, height=10, font=("Segoe UI", 11), selectbackground="#D1EAF5")
        self.lista.grid(row=0, column=0)

        scrollbar = tk.Scrollbar(frame_medio, orient=tk.VERTICAL, command=self.lista.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.lista.config(yscrollcommand=scrollbar.set)

        # Frame inferior: botones de edición (pack)
        frame_botones = tk.Frame(self.root, bg="#f0f0f0")
        frame_botones.pack(pady=10)

        boton_editar = tk.Button(frame_botones, text="Editar", bg="#2196F3", fg="white",
                                 font=("Segoe UI", 10), command=self.editar)
        boton_editar.pack(side=tk.LEFT, padx=10)

        boton_eliminar = tk.Button(frame_botones, text="Eliminar", bg="#f44336", fg="white",
                                   font=("Segoe UI", 10), command=self.eliminar)
        boton_eliminar.pack(side=tk.LEFT, padx=10)

    # CRUD: Crear
    def agregar(self):
        actividad = self.entrada.get().strip()
        if actividad:
            self.lista.insert(tk.END, actividad)
            self.entrada.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor, escribe una actividad.")

    # CRUD: Editar
    def editar(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showinfo("Selecciona una actividad", "Selecciona una actividad para editar.")
            return

        indice = seleccion[0]
        valor_original = self.lista.get(indice)

        nuevo_valor = simpledialog.askstring("Editar actividad", "Modifica la actividad:", initialvalue=valor_original)
        if nuevo_valor:
            self.lista.delete(indice)
            self.lista.insert(indice, nuevo_valor)

    # CRUD: Eliminar
    def eliminar(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showinfo("Selecciona una actividad", "Selecciona una actividad para eliminar.")
            return

        confirmacion = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de eliminar esta actividad?")
        if confirmacion:
            self.lista.delete(seleccion[0])

    # CRUD: Borrar todo
    def borrar_todo(self):
        confirmacion = messagebox.askyesno("Borrar todo", "¿Estás seguro de borrar todas las actividades?")
        if confirmacion:
            self.lista.delete(0, tk.END)

# Ejecutar app
if __name__ == "__main__":
    root = tk.Tk()
    app = GestorActividades(root)
    root.mainloop()
