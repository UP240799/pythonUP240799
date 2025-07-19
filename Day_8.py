# 1. Crear un diccionario vacío llamado dog
dog = {}

# 2. Agregar propiedades al diccionario dog
dog['name'] = 'Max'
dog['color'] = 'brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

print("Diccionario dog:", dog)

# 3. Crear un diccionario del estudiante
student = {
    'first_name': 'Carlos',
    'last_name': 'Pérez',
    'gender': 'Male',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['Python', 'HTML'],
    'country': 'Mexico',
    'city': 'CDMX',
    'address': 'Calle Falsa 123'
}

# 4. Longitud del diccionario student
print("Longitud del diccionario student:", len(student))

# 5. Obtener valor de 'skills' y verificar tipo
skills = student['skills']
print("Habilidades:", skills)
print("Tipo de dato de skills:", type(skills))  # Debe ser list

# 6. Agregar una o dos habilidades
student['skills'].extend(['CSS', 'JavaScript'])
print("Habilidades actualizadas:", student['skills'])

# 7. Obtener claves del diccionario como lista
print("Claves:", list(student.keys()))

# 8. Obtener valores del diccionario como lista
print("Valores:", list(student.values()))

# 9. Convertir diccionario a lista de tuplas con items()
print("Tuplas clave-valor:", list(student.items()))

# 10. Eliminar un ítem del diccionario (por ejemplo 'city')
del student['city']
print("Diccionario sin 'city':", student)

# 11. Eliminar completamente el diccionario dog
del dog
# print(dog)  # Esto lanzaría error porque ya no existe