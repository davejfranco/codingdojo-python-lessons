import sys

def divide(a: int, b: int) -> int:
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    except TypeError:
        print("No se puede dividir con tipos diferentes")
    finally:
        print("Continua")

def connect_db(usuario, password):
    usuarios = {
        "dave": "12345",
        "fabian": "54321",
        "valentin": "abcd"
    }
    if usuarios.get(usuario, 0):
        return True
    return False

def login(usuario, password):
    try:
        connect_db(usuario, password)
        return "Login exitoso"
    except Exception:
        print("intente de nuevo")
        usuario = input("Ingrese usuario: ")
        password = input("Ingrese password: ")
        login(usuario, password)


def esviejo(edad: int) -> str:
    if edad < 0:
        raise Exception("Error: edad no puede ser menor a cero")
    return f'Mi edad es {edad}'

print(esviejo(-1))








