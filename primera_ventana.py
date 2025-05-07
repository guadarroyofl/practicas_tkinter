import time
import tkinter as tk
ventana = tk.Tk()

ventana.title("Reloj")

ventana.geometry("400x200")
ventana.configure(bg= "pale violet red")

frame1 = tk.Frame(ventana)
frame1.configure(width=200, height=100, bg="DeepPink4", bd= 5)
frame1.pack()

etiqueta = tk.Label(frame1, text="", font=("Arial", 30), bg="DeepPink4", fg="white")
etiqueta.pack()

def actualizar_hora():
    hora_actual = time.strftime("%H : %M : %S")
    etiqueta.config(text=hora_actual)
    ventana.after(1000, actualizar_hora)

actualizar_hora()

ventana.mainloop()