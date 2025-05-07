import tkinter as tk
from tkinter import messagebox, simpledialog

usuario_valido = "profe"
contraseña_valida = "1234"
actividades_vars = []

# Ventana principal
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("700x500")
ventana.configure(bg="alice blue")

login_frame = tk.Frame(ventana, bg="LightBlue2", width=300, height=200)
login_frame.pack(pady=40)
login_frame.pack_propagate(False)

tk.Label(login_frame, text="Usuario", fg="black", bg="alice blue",
         font=("Georgia", 12, "bold")).pack(pady=(20, 10))
entry_usuario = tk.Entry(login_frame)
entry_usuario.pack()

tk.Label(login_frame, text="Contraseña", fg="black", bg="alice blue",
         font=("Georgia", 12, "bold")).pack(pady=(20, 10))
entry_contraseña = tk.Entry(login_frame, show="*")
entry_contraseña.pack()

def verificar_login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    if usuario == usuario_valido and contraseña == contraseña_valida:
        login_frame.pack_forget()
        mostrar_principal()
        messagebox.showinfo("EXITOSO", "Inicio de sesión permitido")
    else:
        messagebox.showerror("ERROR", "Usuario o Contraseña incorrectos")

tk.Button(login_frame, text="Ingresar", bg="white", fg="black",
          font=("Georgia", 10), command=verificar_login).pack(pady=15)

# Ventana principal dsp del login 

def mostrar_principal():
    ventana.title("Lista de Actividades")
    ventana.geometry("600x500")
    ventana.config(bg="lavender", relief="sunken")

    barra = tk.Menu(ventana)
    ventana.config(menu=barra)

    menu_archivo = tk.Menu(barra, tearoff=0)
    barra.add_cascade(label="Archivo", menu=menu_archivo)
    menu_archivo.add_command(label="Salir", command=ventana.quit)

    menu_actividades = tk.Menu(barra, tearoff=0)
    barra.add_cascade(label="Actividades Pendientes", menu=menu_actividades)
    menu_actividades.add_command(label="Ver Pendientes", command=mostrar_actividades)
    menu_actividades.add_command(label="Agregar Nueva", command=mostrar_entrada_actividad)
    menu_actividades.add_command(label="Borrar Todas", command=borrar_todas_actividades)

    global frame_contenido
    frame_contenido = tk.Frame(ventana, bg="CadetBlue3")
    frame_contenido.pack(fill=tk.BOTH, expand=True)

    mostrar_inicio()

def limpiar_contenido():
    for widget in frame_contenido.winfo_children():
        widget.destroy()

def mostrar_inicio():
    limpiar_contenido()
    tk.Label(frame_contenido, text="Bienvenido", font=("Georgia", 16, "bold"), bg="CadetBlue3").pack(pady=20)
    tk.Button(frame_contenido, text="Ver Pendientes", bg="alice blue", fg="black",
              font=("Georgia", 14, "bold"), command=mostrar_actividades).pack(pady=10)
    tk.Button(frame_contenido, text="Agregar Nueva", bg="alice blue", fg="black",
              font=("Georgia", 14, "bold"), command=mostrar_entrada_actividad).pack(pady=10)

def mostrar_entrada_actividad():
    limpiar_contenido()

    entrada = tk.Entry(frame_contenido, width=30, font=("Georgia", 12))
    entrada.pack(pady=10)

    def agregar():
        actividad = entrada.get().strip()
        if actividad:
            var = tk.BooleanVar()
            actividades_vars.append([actividad, var])
            entrada.delete(0, tk.END)
            mostrar_actividades()
        else:
            messagebox.showwarning("Vacío", "Ingrese una actividad.")

    tk.Button(frame_contenido, text="Agregar", bg="alice blue", fg="black",
              font=("Georgia", 14, "bold"), command=agregar).pack(pady=10)

def mostrar_actividades():
    limpiar_contenido()

    tk.Label(frame_contenido, text="Lista de Actividades", font=("Georgia", 14, "bold", "underline"),
             bg="alice blue").pack(pady=10)

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

    if not actividades_vars:
        tk.Label(scrollable_frame, text="No hay actividades registradas", font=("Georgia", 12)).pack(pady=10)
        return

    for i, (texto, var) in enumerate(actividades_vars):
        fila = tk.Frame(scrollable_frame)
        fila.pack(anchor="w", pady=2, fill="x")

        cb = tk.Checkbutton(fila, text=texto, variable=var, font=("Georgia", 10))
        cb.pack(side="left", padx=5)

        tk.Button(fila, text="Editar", command=lambda idx=i: editar_actividad(idx),
                  bg="LightBlue4", fg="black").pack(side="left", padx=5)
        tk.Button(fila, text="Eliminar", command=lambda idx=i: eliminar_actividad(idx),
                  bg="LightBlue4", fg="black").pack(side="left", padx=5)

def editar_actividad(indice):
    nueva = simpledialog.askstring("Editar actividad", "Modificar", initialvalue=actividades_vars[indice][0])
    if nueva:
        actividades_vars[indice][0] = nueva
        mostrar_actividades()

def eliminar_actividad(indice):
    if messagebox.askyesno("Eliminar", "¿Deseas eliminar esta actividad?"):
        del actividades_vars[indice]
        mostrar_actividades()

def borrar_todas_actividades():
    if messagebox.askyesno("Confirmar", "¿Borrar todas las actividades?"):
        actividades_vars.clear()
        mostrar_actividades()

ventana.mainloop()
