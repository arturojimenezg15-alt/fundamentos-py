#estructuras de datos de python
#enteros 
number = 10
#print(type(number)) #<class 'int'>

# flotantes
pi = 3.14
#print(type(pi)) #<class 'float'>

# cadenas de texto
greeting = "Hola, Mundo!"
#print(type(greeting)) #<class 'str'>
g
# booleanos
is_active = True
#print(type(is_active)) #<class 'bool'>

# listas
fruits = [
    "manzana", 
    "banana", 
    "cereza"
    ]
# agregar un elemento a la lista
fruits.append("naranja")

# print(fruits) 

# print(fruits[1:])
print(fruits)
fruits[0] = "kiwi"
print(fruits) #['kiwi', 'banana', 'cereza', 'naranja']

# tuplas
nombres = (
      "alice", 
      "job",
      "maria",
      "diana"
      )
print(nombres[0]) #alice

#nombres[0] = "arturo" 

#dicionarios 
persona = {
    "nombre": "Alice", 
    "edad": 30,
    "ciudad": "barcelona"
    
}
print(persona["nombre"]) #Alice
print(persona["edad"]) #30