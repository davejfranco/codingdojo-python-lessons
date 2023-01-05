import os

#Imprimir directorio actual
print(os.getcwd())
try:
    print(os.environ['HOME'])
except Exception:
    print("No existe variable de entorno")

#print(os.listdir())

#print(os.getresuid())

#print(os.get_exec_path())

#print(os.uname())
if os.path.exists('loop.py'):
    print("Existe")
else:
    print("No existe")



