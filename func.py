
def imprima_nombre():
    name = input("Cual es tu nombre? ")
    print(f"Mi nombre es {name}")


def greater(a, b):
    if a > b:
        return a#f"Argumento a: {a} es mayor que {b}"   
    if b > a:
        return b #f"Argumento b: {b} es mayor que {a}"

#print(greater(4, 6))
#print(greater(10, 7))
#print(greater(8, 2))

def print_age():
    age = int(input("Cual es tu edad? "))
    for n in range(1, age):
        print(n)

print_age()

def suma_int(a, b):
    return a + b







