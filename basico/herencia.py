class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
        print(f'Hola me llamo {self.nombre} y tengo {self.edad}')
    
    def comer(self):
        print(f'Estoy comiendo')

#Para heredar paso la clase como argumento
class Cat(Mascota):
    
    def __init__(self, nombre, edad, color):
        #necesito super().__init__ siempre que estoy heredando una clase
        super().__init__(nombre, edad)
        self.color = color
    
    def habla(self):
        print("Miau!")

class Perro(Mascota):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color
    
    def habla(self):
        print("Gauf chamo!")


m = Mascota("Oreo", 6)
print(m.saludo())
m.comer()

c = Cat("Ruby", 7, "gris")
c.habla()
c.saludo()
c.comer()

p = Perro("Cacho", 2, "blanco")
p.habla()
p.saludo()
