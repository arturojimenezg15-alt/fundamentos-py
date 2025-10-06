# funciones de python 
def saludar():
    print("hola, bienvenido a python")

#saludar()

#saludos con parametros
def saludar_persona(nombre):
    print(f"Hola, {nombre}. Bienvenido a Python!") 

#saludar_persona("Arturo")

#saludos con parametros y retorno 
def obtener_saludo(nombre):
    return f"Hola, {nombre}. Bienvenido a Python!"

print(obtener_saludo("Arturo")) 

#saludo con nombre y apellido
def obtener_saludo_completo(nombre= "fulano", apellido= "tal"):
    ""

    return f"Hola, {nombre} {apellido}. Bienvenido a Python!"

print(obtener_saludo_completo("Arturo", "Jimenez"))

#print(obtener_saludo_completo(apellido="Jimenez", nombre="Arturo"))

#print(obtener_saludo_completo("Arturo")) 
#print(obtener_saludo_completo(apellido="jimenez"))