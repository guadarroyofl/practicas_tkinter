import tkinter as tk

def mostrar_nombre():
    nombre = entrada.get()
    etiqueta.config(text=f"Hola, {nombre} 👋")

ventana = tk.Tk()
ventana.title("Nombre con Botón")
ventana.geometry("300x200")
ventana.configure(bg="lightyellow")

frame = tk.Frame(ventana, bg="white", bd=5)
frame.pack(pady=10)

# Caja de texto donde se escribe el nombre
entrada = tk.Entry(frame, font=("Arial", 12))
entrada.pack(pady=5)

# Etiqueta vacía que luego mostrará el saludo
etiqueta = tk.Label(frame, text="", font=("Arial", 12), bg="white")
etiqueta.pack(pady=5)

# Botón que ejecuta la función
boton = tk.Button(ventana, text="Saludar", command=mostrar_nombre)
boton.pack(pady=10)

ventana.mainloop()

