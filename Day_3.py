import math

# 1. Declara tu edad como variable entera
edad = 25

# 2. Declara tu altura como variable flotante
altura = 1.75

# 3. Declara una variable que almacene un número complejo
numero_complejo = 2 + 3j

# 4. Área de un triángulo con entrada del usuario
base = float(input("Ingresa la base del triángulo: "))
altura_triangulo = float(input("Ingresa la altura del triángulo: "))
area_triangulo = 0.5 * base * altura_triangulo
print("El área del triángulo es:", area_triangulo)

# 5. Perímetro de un triángulo
a = float(input("Ingresa el lado a: "))
b = float(input("Ingresa el lado b: "))
c = float(input("Ingresa el lado c: "))
perimetro_triangulo = a + b + c
print("El perímetro del triángulo es:", perimetro_triangulo)

# 6. Área y perímetro de un rectángulo
longitud = float(input("Ingresa la longitud del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))
area_rectangulo = longitud * ancho
perimetro_rectangulo = 2 * (longitud + ancho)
print("Área del rectángulo:", area_rectangulo)
print("Perímetro del rectángulo:", perimetro_rectangulo)

# 7. Área y circunferencia de un círculo
radio = float(input("Ingresa el radio del círculo: "))
area_circulo = 3.14 * radio ** 2
circunferencia = 2 * 3.14 * radio
print("Área del círculo:", area_circulo)
print("Circunferencia del círculo:", circunferencia)

# 8. Pendiente, intersección x e intersección y de y = 2x - 2
m = 2
y_interseccion = -2
x_interseccion = y_interseccion / m
print("Pendiente:", m)
print("Intersección en x:", x_interseccion)
print("Intersección en y:", y_interseccion)

# 9. Pendiente y distancia euclidiana entre (2,2) y (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1)
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Pendiente entre los puntos:", pendiente)
print("Distancia euclidiana:", distancia)

# 10. Comparar las pendientes
print("¿Las pendientes son iguales?", m == pendiente)

# 11. y = x^2 + 6x + 9. ¿Para qué valor de x, y = 0?
for x in range(-10, 11):
    y = x**2 + 6*x + 9
    if y == 0:
        print("y es 0 cuando x =", x)

# 12. Longitud de 'python' y 'dragon' con comparación falsa
print("¿Longitud de 'python' igual a la de 'dragon'?", len("python") == len("dragon"))

# 13. Usar operador and para verificar si 'on' está en ambas palabras
print("'on' está en 'python' y 'dragon'?", "on" in "python" and "on" in "dragon")

# 14. Verificar si 'jargon' está en la oración
frase = "I hope this course is not full of jargon."
print("¿'jargon' está en la frase?", "jargon" in frase)

# 15. Afirmación falsa: 'on' no está en 'dragon' ni en 'python'
print("¿'on' no está en 'dragon' y 'python'?", "on" not in "dragon" and "on" not in "python")

# 16. Longitud de 'python' y convertir a float y string
longitud_python = len("python")
print("Como float:", float(longitud_python))
print("Como string:", str(longitud_python))

# 17. Verificar si un número es par
numero = int(input("Ingresa un número para saber si es par: "))
print("¿Es par?", numero % 2 == 0)

# 18. ¿Floor division de 7 entre 3 es igual a int(2.7)?
print("¿7 // 3 == int(2.7)?", 7 // 3 == int(2.7))

# 19. ¿type('10') == type(10)?
print("¿El tipo de '10' es igual al de 10?", type('10') == type(10))

# 20. ¿int('9.8') == 10?
try:
    print("¿int('9.8') == 10?", int('9.8') == 10)  # Esto genera error
except ValueError:
    print("int('9.8') genera un error porque '9.8' no es un entero válido.")

# 21. Cálculo de salario semanal
horas = float(input("Ingresa las horas trabajadas: "))
tarifa = float(input("Ingresa la tarifa por hora: "))
ganancia = horas * tarifa
print("Tus ganancias semanales son:", ganancia)

# 22. Calcular segundos vividos
anios = int(input("Ingresa cuántos años has vivido: "))
segundos = anios * 365 * 24 * 60 * 60
print("Has vivido aproximadamente", segundos, "segundos.")

# 23. Imprimir tabla
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
#operadores