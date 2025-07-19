import string

# 1. Filtrar solo negativos y ceros usando list comprehension
def filtrar_negativos_cero(numbers):
    return [n for n in numbers if n <= 0]

# 2. Aplanar lista de listas de listas a una lista unidimensional
def aplanar_lista(list_of_lists):
    return [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]

# 3. Crear lista de tuplas con potencias usando list comprehension
def lista_tuplas_potencias():
    return [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

# 4. Aplanar lista y transformar países en listas con abreviación y mayúsculas
def transformar_paises(countries):
    return [[
        country.upper(),
        country[:3].upper(),
        city.upper()
    ] for [[country, city]] in countries]

# 5. Convertir lista en lista de diccionarios con país y ciudad en mayúsculas
def lista_diccionarios_paises(countries):
    return [
        {'country': country.upper(), 'city': city.upper()}
        for [[country, city]] in countries
    ]

# 6. Convertir lista de listas en lista de strings concatenadas
def concatenar_nombres(names):
    return [' '.join(name) for [name] in names]

# 7. Funciones lambda para pendiente y ordenada al origen
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else 'Pendiente indefinida'
intercept = lambda m, x, y: y - m*x

# --- Uso de las funciones con ejemplos ---

if __name__ == "__main__":
    # Ejercicio 1
    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
    print("Negativos y ceros:", filtrar_negativos_cero(numbers))

    # Ejercicio 2
    list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
    print("Lista aplanada:", aplanar_lista(list_of_lists))

    # Ejercicio 3
    print("Lista de tuplas con potencias:")
    for t in lista_tuplas_potencias():
        print(t)

    # Ejercicio 4
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    print("Paises transformados:", transformar_paises(countries))

    # Ejercicio 5
    print("Lista de diccionarios:", lista_diccionarios_paises(countries))

    # Ejercicio 6
    names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
    print("Nombres concatenados:", concatenar_nombres(names))

    # Ejercicio 7
    print("Pendiente entre (1,2) y (3,8):", slope(1, 2, 3, 8))
    print("Ordenada al origen con m=3, punto (1,2):", intercept(3, 1, 2))
