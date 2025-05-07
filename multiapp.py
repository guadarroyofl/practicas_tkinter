import tkinter as tk
from tkinter import messagebox, simpledialog


# ---------------------- Login ----------------------
class LoginVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x180")
        self.root.configure(bg="#e0e0e0")

        self.usuario_valido = "admin"
        self.password_valido = "1234"

        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self.root, text="Usuario:", bg="#e0e0e0").pack(pady=(20, 5))
        self.usuario_entry = tk.Entry(self.root)
        self.usuario_entry.pack()

        tk.Label(self.root, text="Contraseña:", bg="#e0e0e0").pack(pady=(10, 5))
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Ingresar", bg="#4CAF50", fg="white", command=self.verificar).pack(pady=15)

    def verificar(self):
        if self.usuario_entry.get() == self.usuario_valido and self.password_entry.get() == self.password_valido:
            self.root.destroy()
            main_root = tk.Tk()
            AppPrincipal(main_root)
            main_root.mainloop()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")


# ---------------------- App Principal ----------------------
class AppPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación Multiuso")
        self.root.geometry("600x450")
        self.root.configure(bg="#f5f5f5")

        self.crear_menu()

        # Frame contenedor
        self.frame_contenido = tk.Frame(self.root, bg="#f5f5f5")
        self.frame_contenido.pack(fill=tk.BOTH, expand=True)

        self.mostrar_inicio()

    def crear_menu(self):
        barra = tk.Menu(self.root)
        self.root.config(menu=barra)

        menu_archivo = tk.Menu(barra, tearoff=0)
        barra.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Salir", command=self.root.quit)

        menu_actividades = tk.Menu(barra, tearoff=0)
        barra.add_cascade(label="Actividades", menu=menu_actividades)
        menu_actividades.add_command(label="Gestor de Actividades", command=self.mostrar_actividades)

        menu_calculadora = tk.Menu(barra, tearoff=0)
        barra.add_cascade(label="Calculadora", menu=menu_calculadora)
        menu_calculadora.add_command(label="Suma", command=lambda: self.mostrar_calculadora("suma"))
        menu_calculadora.add_command(label="Resta", command=lambda: self.mostrar_calculadora("resta"))
        menu_calculadora.add_command(label="Multiplicación", command=lambda: self.mostrar_calculadora("multiplicacion"))
        menu_calculadora.add_command(label="División", command=lambda: self.mostrar_calculadora("division"))

    def limpiar_contenido(self):
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

    def mostrar_inicio(self):
        self.limpiar_contenido()
        tk.Label(self.frame_contenido, text="Bienvenido a la Aplicación Multiuso",
                 font=("Segoe UI", 16), bg="#f5f5f5").pack(pady=100)

    # ------------------ Gestor de Actividades ------------------
    def mostrar_actividades(self):
        self.limpiar_contenido()

        frame_superior = tk.Frame(self.frame_contenido, bg="#f5f5f5")
        frame_superior.pack(pady=10)

        entrada = tk.Entry(frame_superior, width=30, font=("Segoe UI", 12))
        entrada.pack(side=tk.LEFT, padx=5)

        def agregar():
            actividad = entrada.get().strip()
            if actividad:
                lista.insert(tk.END, actividad)
                entrada.delete(0, tk.END)
            else:
                messagebox.showwarning("Vacío", "Ingrese una actividad.")

        tk.Button(frame_superior, text="Agregar", bg="#4CAF50", fg="white",
                  command=agregar).pack(side=tk.LEFT, padx=5)

        frame_medio = tk.Frame(self.frame_contenido)
        frame_medio.pack()

        lista = tk.Listbox(frame_medio, width=40, height=10, font=("Segoe UI", 11))
        lista.grid(row=0, column=0)

        scrollbar = tk.Scrollbar(frame_medio, command=lista.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        lista.config(yscrollcommand=scrollbar.set)

        frame_botones = tk.Frame(self.frame_contenido, bg="#f5f5f5")
        frame_botones.pack(pady=10)

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

        tk.Button(frame_botones, text="Editar", bg="#2196F3", fg="white", command=editar).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botones, text="Eliminar", bg="#f44336", fg="white", command=eliminar).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botones, text="Borrar Todo", bg="#9E9E9E", fg="white", command=borrar_todo).pack(side=tk.LEFT, padx=10)

    # ------------------ Calculadora ------------------
    def mostrar_calculadora(self, operacion):
        self.limpiar_contenido()

        tk.Label(self.frame_contenido, text=f"Calculadora - {operacion.title()}",
                 font=("Segoe UI", 14), bg="#f5f5f5").pack(pady=10)

        entrada_frame = tk.Frame(self.frame_contenido, bg="#f5f5f5")
        entrada_frame.pack(pady=10)

        entry1 = tk.Entry(entrada_frame, width=10)
        entry2 = tk.Entry(entrada_frame, width=10)
        entry1.grid(row=0, column=0, padx=5)
        entry2.grid(row=0, column=1, padx=5)

        resultado_label = tk.Label(self.frame_contenido, text="", font=("Segoe UI", 12), bg="#f5f5f5")
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

        tk.Button(self.frame_contenido, text="Calcular", bg="#4CAF50", fg="white", command=calcular).pack()

# ---------------------- Main ----------------------
if __name__ == "__main__":
    login_root = tk.Tk()
    app_login = LoginVentana(login_root)
    login_root.mainloop()
