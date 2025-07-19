#Nivel 1
# 1. Función que suma dos números
def add_two_numbers(a, b):
    return a + b

# 2. Función que calcula el área de un círculo
import math
def area_of_circle(radio):
    return math.pi * radio * radio

# 3. Función que suma un número arbitrario de argumentos
def add_all_nums(*args):
    if all(isinstance(x, (int, float)) for x in args):
        return sum(args)
    else:
        return "Todos los elementos deben ser números."

# 4. Convertir Celsius a Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 5. Función que devuelve la estación según el mes
def check_season(mes):
    mes = mes.capitalize()
    if mes in ['September', 'October', 'November']:
        return 'Autumn'
    elif mes in ['December', 'January', 'February']:
        return 'Winter'
    elif mes in ['March', 'April', 'May']:
        return 'Spring'
    elif mes in ['June', 'July', 'August']:
        return 'Summer'
    else:
        return 'Mes no válido'

# 6. Calcular la pendiente (slope) entre dos puntos (x1,y1) y (x2,y2)
def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Pendiente indefinida (división por cero)"
    return (y2 - y1) / (x2 - x1)

# 7. Solución para ecuación cuadrática ax² + bx + c = 0
import cmath
def solve_quadratic_eqn(a, b, c):
    discriminante = b**2 - 4*a*c
    raiz1 = (-b + cmath.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - cmath.sqrt(discriminante)) / (2*a)
    return raiz1, raiz2

# 8. Función para imprimir elementos de una lista
def print_list(lista):
    for elem in lista:
        print(elem)

# 9. Función para invertir una lista usando loops
def reverse_list(lista):
    invertida = []
    for i in range(len(lista)-1, -1, -1):
        invertida.append(lista[i])
    return invertida

# 10. Función para capitalizar los items de una lista
def capitalize_list_items(lista):
    return [str(i).capitalize() for i in lista]

# 11. Función para agregar un ítem a una lista
def add_item(lista, item):
    lista.append(item)
    return lista

# 12. Función para remover un ítem de una lista
def remove_item(lista, item):
    if item in lista:
        lista.remove(item)
    return lista

# 13. Suma de todos los números hasta n (inclusive)
def sum_of_numbers(n):
    return sum(range(1, n+1))

# 14. Suma de números impares hasta n
def sum_of_odds(n):
    return sum(i for i in range(1, n+1, 2))

# 15. Suma de números pares hasta n
def sum_of_even(n):
    return sum(i for i in range(0, n+1, 2))

#Nivel 2
# 1. Contar pares e impares hasta n
def evens_and_odds(n):
    evens = sum(1 for i in range(n+1) if i % 2 == 0)
    odds = n + 1 - evens
    print(f"The number of odds are {odds}.")
    print(f"The number of evens are {evens}.")

# 2. Factorial de un número
def factorial(n):
    if n < 0:
        return "No definido para números negativos"
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

# 3. Verificar si un parámetro está vacío
def is_empty(x):
    if not x:
        return True
    return False

# 4. Funciones estadísticas básicas para listas
import statistics

def calculate_mean(lista):
    return statistics.mean(lista)

def calculate_median(lista):
    return statistics.median(lista)

def calculate_mode(lista):
    try:
        return statistics.mode(lista)
    except statistics.StatisticsError:
        return "No hay un modo único."

def calculate_range(lista):
    return max(lista) - min(lista)

def calculate_variance(lista):
    return statistics.variance(lista)

def calculate_std(lista):
    return statistics.stdev(lista)

#Nivel 3
# 1. Verificar si un número es primo
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# 2. Verificar si todos los ítems en una lista son únicos
def all_unique(lista):
    return len(lista) == len(set(lista))

# 3. Verificar si todos los ítems en una lista son del mismo tipo
def all_same_type(lista):
    if not lista:
        return True
    tipo = type(lista[0])
    return all(isinstance(x, tipo) for x in lista)

# 4. Verificar si una variable es un nombre válido en Python
import keyword
import re
def is_valid_python_var(variable):
    if keyword.iskeyword(variable):
        return False
    return re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', variable) is not None

# Simulación de datos (se puede adaptar a datos reales)
countries_data = [
    {'name': 'China', 'population': 1409517397, 'languages': ['Chinese']},
    {'name': 'India', 'population': 1339180127, 'languages': ['Hindi', 'English']},
    {'name': 'USA', 'population': 324459463, 'languages': ['English']},
    {'name': 'Indonesia', 'population': 263991379, 'languages': ['Indonesian']},
    {'name': 'Brazil', 'population': 209288278, 'languages': ['Portuguese']},
    # ... más países
]

from collections import Counter

def most_spoken_languages(countries, top_n=10):
    language_counter = Counter()
    for country in countries:
        for lang in country['languages']:
            language_counter[lang] += 1
    return language_counter.most_common(top_n)

def most_populated_countries(countries, top_n=10):
    sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:top_n]

# Ejemplo de uso
print(most_spoken_languages(countries_data, 10))
print(most_populated_countries(countries_data, 10))