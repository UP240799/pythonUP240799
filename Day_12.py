#Nivel 1
import random
import string

# 1. Generar un ID de usuario aleatorio de 6 caracteres/dígitos
def random_user_id():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(6))

print(random_user_id())

# 2. Generar IDs con inputs de usuario: longitud y cantidad de IDs
def user_id_gen_by_user():
    longitud = int(input("Número de caracteres por ID: "))
    cantidad = int(input("Número de IDs a generar: "))
    caracteres = string.ascii_letters + string.digits
    ids = []
    for _ in range(cantidad):
        nuevo_id = ''.join(random.choice(caracteres) for _ in range(longitud))
        ids.append(nuevo_id)
    return ids

for user_id in user_id_gen_by_user():
    print(user_id)

# 3. Generar un color RGB aleatorio en formato 'rgb(r,g,b)'
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())

#Nivel 2
# 1. Generar lista de colores hexadecimales
def list_of_hexa_colors(n):
    hexa_chars = string.digits + 'abcdef'
    colores = []
    for _ in range(n):
        color = '#' + ''.join(random.choice(hexa_chars) for _ in range(6))
        colores.append(color)
    return colores

print(list_of_hexa_colors(3))

# 2. Generar lista de colores RGB
def list_of_rgb_colors(n):
    colores = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colores.append(f"rgb({r},{g},{b})")
    return colores

print(list_of_rgb_colors(3))

# 3. Función para generar colores 'hexa' o 'rgb'
def generate_colors(tipo, n):
    if tipo.lower() == 'hexa':
        return list_of_hexa_colors(n)
    elif tipo.lower() == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Tipo inválido. Use 'hexa' o 'rgb'."

print(generate_colors('hexa', 3))
print(generate_colors('rgb', 3))


#Nivel 3
# 1. Función que mezcla una lista y devuelve la lista mezclada
def shuffle_list(lista):
    copia = lista[:]
    random.shuffle(copia)
    return copia

print(shuffle_list([1,2,3,4,5]))

# 2. Función que genera 7 números aleatorios únicos entre 0 y 9
def unique_random_numbers():
    return random.sample(range(10), 7)

print(unique_random_numbers())
