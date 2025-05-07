class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        
    def hablar(self):
        print(f"Hola, soy un {self.raza}, me dicen {self.nombre} y tengo {self.edad} años")
        print("GuauGuauGuau")
        
class Gato(Perro):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza)
    
    def hablar(self):
        print(f"Hola, soy un {self.raza}, me dicen {self.nombre} y tengo {self.edad} años")
        print("Miau")
        
p1 = Perro("Roma", 6, "Bulldog Frances")
p2 = Perro("Luli", 14, "Labrador")

g1 = Gato("Luz", 4, "Burmés")
g2 = Gato("Sol", 8, "Siamés")

Perros_Creados = [p1, p2]
Gatos_Creados = [g1, g2]

for perro in Perros_Creados:
    perro.hablar() 
print("\n")
for gato in Gatos_Creados:
    gato.hablar()   
print("\n")
        