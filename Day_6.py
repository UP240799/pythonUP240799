#Nivel 1
# 1. Crear una tupla vacía
tupla_vacia = ()

# 2. Crear tuplas con nombres de hermanos y hermanas (pueden ser inventados)
hermanas = ('Ana', 'Lucía', 'María')
hermanos = ('Carlos', 'Juan')

# 3. Unir hermanos y hermanas
siblings = hermanas + hermanos
print("Hermanos y hermanas:", siblings)

# 4. ¿Cuántos hermanos en total?
print("Total de hermanos:", len(siblings))

# 5. Agregar padres a la tupla de hermanos y crear family_members
family_members = siblings + ('Papá', 'Mamá')
print("Miembros de la familia:", family_members)

#Nivel 2
# 1. Desempaquetar hermanos y padres de la tupla family_members
*hermanos_todos, padre, madre = family_members
print("Hermanos:", hermanos_todos)
print("Padre:", padre)
print("Madre:", madre)

# 2. Crear tuplas de frutas, vegetales y productos animales
frutas = ('manzana', 'banana', 'mango')
vegetales = ('zanahoria', 'lechuga', 'tomate')
productos_animales = ('leche', 'queso', 'huevo')

# 3. Unir todas las tuplas en una sola
food_stuff_tp = frutas + vegetales + productos_animales
print("Comida en tupla:", food_stuff_tp)

# 4. Convertir tupla a lista
food_stuff_lt = list(food_stuff_tp)
print("Comida en lista:", food_stuff_lt)

# 5. Cortar el elemento(s) del medio
n = len(food_stuff_lt)
if n % 2 == 0:
    print("Medio:", food_stuff_lt[n//2 - 1 : n//2 + 1])
else:
    print("Medio:", food_stuff_lt[n//2])

# 6. Cortar los primeros 3 y los últimos 3 elementos
print("Primeros 3:", food_stuff_lt[:3])
print("Últimos 3:", food_stuff_lt[-3:])

# 7. Eliminar completamente la tupla
del food_stuff_tp
# print(food_stuff_tp)  # Esto dará error si lo descomentas porque ya no existe

# 8. Verificar si un ítem existe en la tupla
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print("¿Estonia es un país nórdico?", 'Estonia' in nordic_countries)
print("¿Iceland es un país nórdico?", 'Iceland' in nordic_countries)