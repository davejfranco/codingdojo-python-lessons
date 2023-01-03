"""
Puedo declarar variables con sus tipos pero esto es opcional
"""
name: str = "Dave"
age: int = 35
es_verdad: bool  = False
una_lista: list[str] = ["Hola", "Mundo"]
diccionarios: dict[str, int] = {"Hola": 2}


def sumar(a: int, b: int) -> int:
    """Esta funciona suma dos enteros"""
    return a + b

#Ejecutar la funcion de sumar
suma: int = sumar(2, 5)
print(suma)



