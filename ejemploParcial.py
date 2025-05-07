class Persona: 
    def  __init__(self, nombre, apellidos, edad): 
        print("ejecutando metodo constructor, asignando valores")
        self.nombre=nombre 
        self.apellidos=apellidos
        self.edad=edad 
        
    def MostrarPersona(self): 
        print ("Nombre: " ,self.nombre) 
        print ("Apellidos: ", self.apellidos) 
        print ("Edad: " ,self.edad) 
 
p1 = Persona("Alfredo","Moreno Muñoz ", 35) 
p1.MostrarPersona()