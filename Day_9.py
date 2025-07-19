#Nivel 1
# 1. Edad para conducir
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Ya tienes edad suficiente para aprender a conducir.")
else:
    print(f"Necesitas esperar {18 - edad} años para aprender a conducir.")

# 2. Comparación de edades
mi_edad = 25
tu_edad = int(input("Ingresa tu edad: "))
diferencia = abs(mi_edad - tu_edad)

if tu_edad > mi_edad:
    print(f"Eres {diferencia} año{'s' if diferencia > 1 else ''} mayor que yo.")
elif tu_edad < mi_edad:
    print(f"Soy {diferencia} año{'s' if diferencia > 1 else ''} mayor que tú.")
else:
    print("Tenemos la misma edad.")

# 3. Comparación de dos números
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")

#Nivel 2
# 1. Calificación por puntuación
score = int(input("Ingresa tu calificación (0-100): "))

if 80 <= score <= 100:
    print("A")
elif 70 <= score < 80:
    print("B")
elif 60 <= score < 70:
    print("C")
elif 50 <= score < 60:
    print("D")
elif 0 <= score < 50:
    print("F")
else:
    print("Puntuación no válida.")

# 2. Determinar estación del año
mes = input("Ingresa el mes: ").capitalize()

if mes in ['September', 'October', 'November']:
    print("Es otoño 🍂")
elif mes in ['December', 'January', 'February']:
    print("Es invierno ❄️")
elif mes in ['March', 'April', 'May']:
    print("Es primavera 🌸")
elif mes in ['June', 'July', 'August']:
    print("Es verano ☀️")
else:
    print("Mes no reconocido.")

# 3. Verificar fruta en la lista
fruits = ['banana', 'orange', 'mango', 'lemon']
nueva_fruta = input("Ingresa una fruta: ").lower()

if nueva_fruta in fruits:
    print("Esa fruta ya está en la lista.")
else:
    fruits.append(nueva_fruta)
    print("Lista actualizada:", fruits)

#Nivel 3
# Diccionario base
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Verificar si tiene 'skills' y mostrar la del medio
if 'skills' in person:
    skills = person['skills']
    medio = len(skills) // 2
    print("Habilidad del medio:", skills[medio])

# 2. Verificar si sabe Python
if 'skills' in person:
    print("¿Tiene Python?", 'Python' in person['skills'])

# 3. Clasificación por habilidades
skills = person['skills']
if set(skills) == {'JavaScript', 'React'}:
    print("Es desarrollador front end.")
elif {'Node', 'MongoDB', 'Python'}.issubset(skills):
    print("Es desarrollador backend.")
elif {'React', 'Node', 'MongoDB'}.issubset(skills):
    print("Es desarrollador fullstack.")
else:
    print("Título desconocido.")

# 4. Si está casado y vive en Finlandia, mostrar mensaje
if person['is_marred'] and person['country'] == 'Finland':
    nombre = person['first_name'] + ' ' + person['last_name']
    print(f"{nombre} vive en Finlandia. Está casado.")