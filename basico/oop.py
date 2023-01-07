
nombre = "dave"

def hola():
    print("Hola mundo!")

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def comer(self):
        pass

    def dormir(self):
        pass

    def ir_al_bano(self):
        pass    

class Auto:  
    #metodo init, lo utilizo siempre que quiero darle atributos a mi clase
    def __init__(self, modelo, marca, color):
        #Atributos de la clase
        self.module = modelo
        self.marca = marca
        self.color = color

        #Puedo crear atributos adicionales
        self.estado = "apagado"


    #Metodos
    def encender(self):
        self.estado = "encendido"
        return self.estado

class Concencionario:

    def __init__(self, nombre, direccion, num_telf):
        self.nombre = nombre
        self.direccion = direccion
        self.num_telf = num_telf

        self.inventario = []
    
    def add_auto(self, auto: Auto):
        self.inventario.append(auto)
    
    def get_inventario(self):
        return self.inventario
    
    def delete_car(self, auto):
        self.inventario.remove(auto)

class Database:

    def __init__(self, ip, usuario, password) -> None:
        self.ip = ip
        self.usuario = usuario
        self.password = password

        self.client = None
    
    def connect(self):
        return self.client
    
    def save(self, data):
        


    


car1 = Auto("Sedan", "Toyota", "Negro")
car2 = Auto("Camioneta", "Ford", "Roja")
car3 = Auto("Coupe", "Porsche", "Amarillo")

tienda = Concencionario("CodingAuto", "Zoom", "958653568")
tienda.add_auto(car1)
tienda.add_auto(car2)
tienda.add_auto(car3)
print(tienda.get_inventario())

tienda.delete_car(car2)
for auto in tienda.get_inventario():
    print(auto.color)







