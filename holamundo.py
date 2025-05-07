# notas = []
# promedio = 0
# cantidad_notas = int(input("Ingrese la cantidad de notas a cargar: "))

# for i in range(cantidad_notas):
#     nota = float(input(f"Ingrese la nota del alumno {i+1}: "))
#     notas.append(nota)
    
# promedio = float(sum(notas)/cantidad_notas)
# print("El promedio de notas es:", promedio)


class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        
    def presentarse(self):
        print(f"Soy un {self.raza} y me llaman {self.nombre}, y tengo {self.edad} años de edad")
    
    def ladrar(self):
        print("LADRO: GuauGuau")
        
perro1 = Perro("Roma","Bulldog Francés", 3)
perro2 = Perro ("Luli","Labrador", 5)

perrosCreados = []

perrosCreados.append(perro1)
perrosCreados.append(perro2)


for perro in perrosCreados:
    perro.presentarse()
    perro.ladrar()
