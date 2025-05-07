from tkinter import*

# Funcion 1
total_gastos=0
def calculadoraDeGastos():
    global total_gastos
    texto=gastos.get()
    lista=texto.split()
    numeros=list(map(float,lista))
    total_gastos=sum(numeros)
    resultadoGastos.config(text=f"gasto Total: ${total_gastos}")
   
# //funcion 2 
total_ingresos=0
def calculadoraDeIngresos():
    global total_ingresos
    texto2=ingresos.get()
    lista2=texto2.split()
    numeros2=list(map(float,lista2))
    total_ingresos=sum(numeros2)
    resultadoIngresos.config(text=f"gasto Total: ${total_ingresos}")
    
# funcion 3
def calculadoraReRestante():
    cantidadrestante=total_ingresos - total_gastos
    restante.config(text=f"Dinero restante: ${cantidadrestante}")
    

practica=Tk()
#ventana 
practica.title("Ventana de practica")
# practica.iconbitmap("ordenador-portatil.ico")
practica.resizable(1,1)
practica.geometry("650x400")
#marco
marco=Frame()
marco.config(width=600,height=350, bg="#C4A1CD")
marco.pack_propagate(False)
marco.pack()
#Gastos
gastos=Entry(marco)
gastos.pack()
#boton
calcularGastos=Button(marco, text="Calcular gastos", font=("Arial",13),command=calculadoraDeGastos)
calcularGastos.pack()
#label
resultadoGastos=Label(marco,width=25)
resultadoGastos.pack()
#Ingresos
ingresos=Entry(marco)
ingresos.pack()
#boton de ingresos
calcularIngresos=Button(marco, text="Calcular ingresos", font=("arial",13),command=calculadoraDeIngresos)
calcularIngresos.pack()
#label de ingresos
resultadoIngresos=Label(marco, width=25)
resultadoIngresos.pack()
#boton restante
calcularRestante=Button(marco, text="Calcular dinero restante", font=("arial",13), command=calculadoraReRestante)
calcularRestante.pack()
#label restante
restante=Label(marco, width=25)
restante.pack()

practica.mainloop()