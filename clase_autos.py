class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
    def mostrar_auto(self):
        print(f"\n Tenemos disponible el auto: {self.marca} {self.modelo} del año {self.año}")

Auto1 = Auto("Toyota", "T-Cross", 2023)
Auto2 = Auto("Toyota", "Corolla", 2020)
Auto3 = Auto("Toyota", "Etios", 2021)

autos_creados= []

autos_creados.append(Auto1)
autos_creados.append(Auto2)
autos_creados.append(Auto3)

for Auto in autos_creados:
    Auto.mostrar_auto()

        
        
