import random

def print_hello_world() -> None:
    print("Hello World")

#Generador de password
#Debe permitir cuantos caracteres tiene el password
#Que tenga mayusculas y minusculas por defecto
#Que tenga caracteres especiales optional
#Que tenga numeros optional
def password_generator(numbers: bool, special: bool, lenght: int = 8) -> str:
    """This is a password generator function
    """
    password = "" #This variable will be the result
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "1234567890"
    schars = "!#$%&()"

    if numbers == True:
        chars += num #concatenar +=
    
    if special == True:
        chars = chars + schars #concatenar igual al anterior

    #will iterate as long as lenght
    for _ in range(lenght):
        password += random.choice(chars)

    return password

