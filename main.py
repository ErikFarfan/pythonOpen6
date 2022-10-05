class Vehiculo:
    color=None
    ruedas=None
    Puertas=None

    def __init__(self,nombre):
        self.color='Negro'
        self.ruedas=4
        self.puertas=4

class Coche(Vehiculo):

    velocidad=None
    cilindrada=None

    def __init__(self,nombre):
        super().__init__(nombre)
        self.nombre=nombre
        self.velocidad=190
        self.cilindrada=1500

c=Coche('Deportivo')
print('Es un coche tipo:  ',c.nombre)
print('Tiene una cilindrada de:  ',c.cilindrada)
print('color: ',c.color)
print('Velocidad maxima : ',c.velocidad)
print('Cantidad de puertas : ',c.puertas)
print('Cantidad de ruedas: ',c.ruedas)
