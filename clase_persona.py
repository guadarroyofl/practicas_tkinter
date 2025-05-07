class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, carrera):
        super().__init__(nombre, apellido)
        self.edad = edad
        self.carrera = carrera
        
    def mostrar_carrera(self):
        print(f"\nEl alumno {self.nombre} {self.apellido} estudia: {self.carrera}")

e1 = Estudiante("Alfredo", "Gomez", 34, "Contador Público")
e1.mostrar_carrera()
