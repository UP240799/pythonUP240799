# 1. Concatenar las cadenas 'Thirty', 'Days', 'Of', 'Python'
cadena1 = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(cadena1)

# 2. Concatenar 'Coding', 'For', 'All'
cadena2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(cadena2)

# 3. Declarar variable company
company = "Coding For All"

# 4. Imprimir variable
print(company)

# 5. Longitud de la cadena
print(len(company))

# 6. Convertir a mayúsculas
print(company.upper())

# 7. Convertir a minúsculas
print(company.lower())

# 8. Métodos capitalize, title y swapcase
print(company.capitalize())  # Solo la primera letra en mayúscula
print(company.title())       # Cada palabra con mayúscula
print(company.swapcase())    # Invertir mayúsculas por minúsculas

# 9. Cortar la primera palabra
print(company[7:])  # Quita 'Coding'

# 10. Verificar si contiene 'Coding'
print(company.index('Coding'))
print(company.find('Coding'))
print('Coding' in company)

# 11. Reemplazar 'Coding' por 'Python'
print(company.replace('Coding', 'Python'))

# 12. Cambiar 'Python for Everyone' por 'Python for All'
frase = 'Python for Everyone'
print(frase.replace('Everyone', 'All'))

# 13. Separar usando espacios
print(company.split())

# 14. Separar por coma
empresas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(empresas.split(', '))

# 15. Caracter en el índice 0
print(company[0])

# 16. Último índice
print(len(company) - 1)

# 17. Caracter en el índice 10
print(company[10])

# 18. Acrónimo de 'Python For Everyone'
frase1 = 'Python For Everyone'
acronimo1 = ''.join([palabra[0] for palabra in frase1.split()])
print(acronimo1)

# 19. Acrónimo de 'Coding For All'
acronimo2 = ''.join([palabra[0] for palabra in company.split()])
print(acronimo2)

# 20. Índice de la primera C
print(company.index('C'))

# 21. Índice de la primera F
print(company.index('F'))

# 22. Última ocurrencia de 'l'
cadena3 = 'Coding For All People'
print(cadena3.rfind('l'))

# 23. Primera ocurrencia de 'because'
oracion = 'You cannot end a sentence with because because because is a conjunction'
print(oracion.find('because'))

# 24. Última ocurrencia de 'because'
print(oracion.rindex('because'))

# 25. Cortar 'because because because'
inicio = oracion.find('because')
fin = oracion.rindex('because') + len('because')
print(oracion[inicio:fin])

# 26. ¿Empieza con 'Coding'?
print(company.startswith('Coding'))

# 27. ¿Termina con 'coding'?
print(company.endswith('coding'))  # False, mayúscula/minúscula importa

# 28. Eliminar espacios en los extremos
espaciado = '   Coding For All      '
print(espaciado.strip())

# 29. ¿Cuál devuelve True con isidentifier?
print("30DaysOfPython".isidentifier())         # False
print("thirty_days_of_python".isidentifier())  # True

# 30. Unir librerías con #
librerias = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(librerias))

# 31. Separar con salto de línea
print("I am enjoying this challenge.\nI just wonder what is next.")

# 32. Separar con tabulaciones
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# 33. Formato para área de un círculo
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")

# 34. Operaciones con formato
a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
