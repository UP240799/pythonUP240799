#Nivel 1
# 1. Declarar una lista vacía
lista_vacia = []

# 2. Declarar una lista con más de 5 elementos
lista_5 = ['manzana', 'banana', 'naranja', 'kiwi', 'sandía', 'mango']

# 3. Longitud de la lista
print(len(lista_5))

# 4. Primer, medio y último elemento
print(lista_5[0])               # Primer
print(lista_5[len(lista_5)//2]) # Medio
print(lista_5[-1])              # Último

# 5. Lista con diferentes tipos de datos
mixed_data_types = ['Carlos', 25, 1.75, 'Soltero', 'México']

# 6. Lista de empresas de tecnología
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Imprimir la lista
print(it_companies)

# 8. Número de empresas
print(len(it_companies))

# 9. Primera, media y última empresa
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])

# 10. Modificar una empresa
it_companies[1] = 'Alphabet'
print(it_companies)

# 11. Agregar una empresa
it_companies.append('Intel')
print(it_companies)

# 12. Insertar una empresa en el medio
it_companies.insert(len(it_companies)//2, 'Samsung')
print(it_companies)

# 13. Cambiar una empresa a mayúsculas (menos IBM)
it_companies[0] = it_companies[0].upper()
print(it_companies)

# 14. Unir las empresas con '#; '
print('#; '.join(it_companies))

# 15. Verificar si existe una empresa
print('Amazon' in it_companies)

# 16. Ordenar alfabéticamente
it_companies.sort()
print(it_companies)

# 17. Invertir el orden
it_companies.reverse()
print(it_companies)

# 18. Cortar las primeras 3 empresas
print(it_companies[:3])

# 19. Cortar las últimas 3 empresas
print(it_companies[-3:])

# 20. Cortar la(s) del medio
medio = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    print(it_companies[medio-1:medio+1])
else:
    print(it_companies[medio])

# 21. Eliminar la primera empresa
it_companies.pop(0)
print(it_companies)

# 22. Eliminar la del medio
medio = len(it_companies) // 2
it_companies.pop(medio)
print(it_companies)

# 23. Eliminar la última empresa
it_companies.pop()
print(it_companies)

# 24. Eliminar todas
it_companies.clear()
print(it_companies)

# 25. Destruir la lista
del it_companies
# print(it_companies)  # Esto causará error porque ya no existe

# 26. Unir listas frontend y backend
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# 27. Insertar Python y SQL después de Redux
pos = full_stack.index('Redux') + 1
full_stack.insert(pos, 'Python')
full_stack.insert(pos+1, 'SQL')
print(full_stack)

#Nivel 2
# Lista de edades de estudiantes
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Ordenar, obtener min y max
ages.sort()
print("Edades ordenadas:", ages)
min_age = min(ages)
max_age = max(ages)
print("Min:", min_age, "Max:", max_age)

# 2. Agregar min y max de nuevo
ages.append(min_age)
ages.append(max_age)
print("Con duplicados:", ages)

# 3. Mediana
ages.sort()
n = len(ages)
if n % 2 == 0:
    mediana = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    mediana = ages[n//2]
print("Mediana:", mediana)

# 4. Promedio
promedio = sum(ages) / len(ages)
print("Promedio:", promedio)

# 5. Rango
print("Rango:", max_age - min_age)

# 6. Comparar diferencias absolutas
print("abs(min - promedio):", abs(min_age - promedio))
print("abs(max - promedio):", abs(max_age - promedio))

# 7. País(es) del medio
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
n = len(countries)
if n % 2 == 0:
    print("Países del medio:", countries[n//2 - 1: n//2 + 1])
else:
    print("País del medio:", countries[n//2])

# 8. Dividir en dos mitades
if len(countries) % 2 == 0:
    mitad1 = countries[:len(countries)//2]
    mitad2 = countries[len(countries)//2:]
else:
    mitad1 = countries[:len(countries)//2 + 1]
    mitad2 = countries[len(countries)//2 + 1:]
print("Mitad 1:", mitad1)
print("Mitad 2:", mitad2)

# 9. Desempaquetar los primeros 3 países y el resto como países escandinavos
p1, p2, p3, *scandic_countries = countries
print("Países:", p1, p2, p3)
print("Países escandinavos:", scandic_countries)