#Nivel 1
# 1. Iterar de 0 a 10 con for loop
for i in range(11):
    print(i)

print("------")

# 2. Iterar de 0 a 10 con while loop
i = 0
while i <= 10:
    print(i)
    i += 1

print("------")

# 3. Iterar de 10 a 0 con for loop
for i in range(10, -1, -1):
    print(i)

print("------")

# 4. Iterar de 10 a 0 con while loop
i = 10
while i >= 0:
    print(i)
    i -= 1

print("------")

# 5. Triángulo con 7 líneas usando print()
for i in range(1, 8):
    print('#' * i)

print("------")

# 6. Cuadrado de # con loops anidados (8x8)
for _ in range(8):
    print('# ' * 8)

print("------")

# 7. Patrón de multiplicación
for i in range(11):
    print(f"{i} x {i} = {i*i}")

print("------")

# 8. Iterar lista y mostrar elementos
lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in lista:
    print(item)

print("------")

# 9. Imprimir solo números pares de 0 a 100
for num in range(0, 101, 2):
    print(num)

print("------")

# 10. Imprimir solo números impares de 0 a 100
for num in range(1, 101, 2):
    print(num)

#Nivel 2
# 1. Suma de todos los números de 0 a 100
suma_total = 0
for num in range(101):
    suma_total += num
print("La suma de todos los números es:", suma_total)

print("------")

# 2. Suma de pares e impares separados
suma_pares = 0
suma_impares = 0
for num in range(101):
    if num % 2 == 0:
        suma_pares += num
    else:
        suma_impares += num
print(f"La suma de todos los pares es {suma_pares}. La suma de todos los impares es {suma_impares}.")

#Nivel 3
# 1. Países con "land" en su nombre
countries = [
    'Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland',
    'Ireland', 'Poland', 'Netherlands', 'England', 'Scotland'
]
countries_with_land = [country for country in countries if 'land' in country.lower()]
print("Países con 'land':", countries_with_land)

print("------")

# 2. Invertir lista de frutas usando loop
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])
print("Frutas invertidas:", reversed_fruits)

print("------")

# 3. Trabajar con datos de países y lenguas
# Aquí simulo que cargamos datos (ya que no hay acceso directo a archivos en esta sesión)

countries_data = [
    {'name': 'China', 'population': 1409517397, 'languages': ['Chinese']},
    {'name': 'India', 'population': 1339180127, 'languages': ['Hindi', 'English']},
    {'name': 'USA', 'population': 324459463, 'languages': ['English']},
    {'name': 'Indonesia', 'population': 263991379, 'languages': ['Indonesian']},
    {'name': 'Brazil', 'population': 209288278, 'languages': ['Portuguese']},
    # ... más países
]

# Total de idiomas únicos
all_languages = set()
for country in countries_data:
    for lang in country['languages']:
        all_languages.add(lang)
print("Número total de idiomas únicos:", len(all_languages))

print("------")

# 4. Diez idiomas más hablados (simulado con conteo simple)
from collections import Counter

language_counter = Counter()
for country in countries_data:
    for lang in country['languages']:
        language_counter[lang] += 1

most_spoken = language_counter.most_common(10)
print("Los 10 idiomas más hablados:", most_spoken)

print("------")

# 5. Diez países más poblados
sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
top_10_population = sorted_countries[:10]
print("Los 10 países más poblados:")
for c in top_10_population:
    print(f"{c['name']}: {c['population']}")