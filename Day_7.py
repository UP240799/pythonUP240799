#Nivel 1 
# Conjuntos iniciales
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Longitud del conjunto de empresas
print("Número de empresas:", len(it_companies))

# 2. Agregar 'Twitter'
it_companies.add('Twitter')
print(it_companies)

# 3. Agregar múltiples empresas
it_companies.update(['Tesla', 'Intel', 'Spotify'])
print(it_companies)

# 4. Eliminar una empresa
it_companies.remove('Google')  # Si no existe lanza error
print(it_companies)

# 5. Diferencia entre remove y discard
# remove lanza error si el elemento no existe
# discard NO lanza error si el elemento no existe
it_companies.discard('Google')  # Google ya fue removido, no da error

#Nivel 2
# 1. Unión de A y B
print("Unión A ∪ B:", A.union(B))

# 2. Intersección de A y B
print("Intersección A ∩ B:", A.intersection(B))

# 3. ¿A es subconjunto de B?
print("¿A ⊆ B?", A.issubset(B))

# 4. ¿A y B son disjuntos?
print("¿A y B son disjuntos?", A.isdisjoint(B))

# 5. Unión A con B y B con A
print("A ∪ B:", A.union(B))
print("B ∪ A:", B.union(A))  # Mismo resultado, unión es conmutativa

# 6. Diferencia simétrica (elementos únicos en A o B pero no en ambos)
print("Diferencia simétrica:", A.symmetric_difference(B))

# 7. Borrar completamente los sets
A.clear()
B.clear()
print("A:", A)
print("B:", B)

#Nivel 3
# 1. Convertir age (lista) a set y comparar longitudes
age_set = set(age)
print("Longitud lista:", len(age))        # Repite elementos
print("Longitud set:", len(age_set))      # Solo únicos
# El set es más pequeño porque elimina duplicados

# 2. Diferencia entre tipos de datos
"""
string: cadena de texto, inmutable, ordenada.
list: colección de elementos, ordenada, mutable, permite duplicados.
tuple: como lista pero inmutable, ordenada, permite duplicados.
set: colección desordenada, no permite duplicados, mutable.
"""

# 3. ¿Cuántas palabras únicas hay en la oración?
frase = "I am a teacher and I love to inspire and teach people"
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
print("Número de palabras únicas:", len(palabras_unicas))