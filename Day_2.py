import math

# Declaración de variables
nombre = "Hiram"
apellido = "Vazquez"
nombre_completo = nombre + " " + apellido
pais = "MEX"
ciudad = "AGS"
edad = 18
año = 2025
esta_casado = False
es_verdadero = True
luz_encendida = True

# Múltiples variables en una línea
a, b, c = 1, 2, 3

# Verificar tipos de datos
print("Tipos de datos:")
print("nombre:", type(nombre))
print("apellido:", type(apellido))
print("nombre_completo:", type(nombre_completo))
print("país:", type(pais))
print("ciudad:", type(ciudad))
print("edad:", type(edad))
print("año:", type(año))
print("está casado:", type(esta_casado))
print("es verdadero:", type(es_verdadero))
print("luz encendida:", type(luz_encendida))
print("a, b, c:", type(a), type(b), type(c))

# Longitud del nombre
print("\nLongitud del nombre:", len(nombre))

# Comparar longitudes de nombre y apellido
print("¿El nombre es más largo que el apellido?", len(nombre) > len(apellido))

# Operaciones aritméticas
numero_uno = 5
numero_dos = 4

suma = numero_uno + numero_dos
resta = numero_uno - numero_dos
producto = numero_uno * numero_dos
division = numero_uno / numero_dos
residuo = numero_dos % numero_uno
exponente = numero_uno ** numero_dos
division_entera = numero_uno // numero_dos

print("\nResultados aritméticos:")
print("Suma:", suma)
print("Resta:", resta)
print("Producto:", producto)
print("División:", division)
print("Residuo:", residuo)
print("Exponente:", exponente)
print("División entera:", division_entera)

# Cálculos con un círculo
radio = 30
area_circulo = math.pi * radio ** 2
circunferencia = 2 * math.pi * radio

print("\nCálculos del círculo:")
print("Área del círculo:", area_circulo)
print("Circunferencia del círculo:", circunferencia)

# Área del círculo con entrada del usuario
radio_usuario = float(input("\nIngresa el radio: "))
area_usuario = math.pi * radio_usuario ** 2
print("Área con radio del usuario:", area_usuario)

# Recolección de información del usuario
nombre_usuario = input("Ingresa tu nombre: ")
apellido_usuario = input("Ingresa tu apellido: ")
pais_usuario = input("Ingresa tu país: ")
edad_usuario = input("Ingresa tu edad: ")

print("\nInformación del usuario:")
print("Nombre:", nombre_usuario)
print("Apellido:", apellido_usuario)
print("País:", pais_usuario)
print("Edad:", edad_usuario)

# Palabras clave reservadas en Python
print("\nPalabras clave reservadas en Python:")
help('keywords')