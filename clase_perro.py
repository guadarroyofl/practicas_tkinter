class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def presentarse(self):
        print(f"Soy un {self.raza} y me llaman {self.nombre}, y tengo {self.edad} años de edad.")

    def ladrar(self):
        print("GuauGuau")


# Lista para guardar perros
perrosCreados = []

# Pedir cuántos perros quiere ingresar
cantidad = int(input("¿Cuántos perros querés agregar?: "))

for i in range(cantidad):
    print(f"\n🐾 Ingresando datos del perro {i+1}:")
    nombre = input("Nombre: ")
    raza = input("Raza: ")
    
    while True:
        try:
            edad = int(input("Edad: "))
            break
        except ValueError:
            print("Por favor ingresá un número entero válido para la edad.")
    
    perro = Perro(nombre, raza, edad)
    perrosCreados.append(perro)

# Mostrar presentación de cada perro
print("\n🎉 Perros registrados:")
for perro in perrosCreados:
    perro.presentarse()
    perro.ladrar()
