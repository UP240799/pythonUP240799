import math

# Variable declarations
first_name = "Hiram"
last_name = "Vazquez"
full_name = first_name + " " + last_name
country = "MEX"
city = "AGS"
age = 18
year = 2025
is_married = False
is_true = True
is_light_on = True

# Multiple variables on one line
a, b, c = 1, 2, 3

# Check data types
print("Data Types:")
print("first_name:", type(first_name))
print("last_name:", type(last_name))
print("full_name:", type(full_name))
print("country:", type(country))
print("city:", type(city))
print("age:", type(age))
print("year:", type(year))
print("is_married:", type(is_married))
print("is_true:", type(is_true))
print("is_light_on:", type(is_light_on))
print("a, b, c:", type(a), type(b), type(c))

# Length of first name
print("\nLength of first name:", len(first_name))

# Compare name lengths
print("Is first name longer than last name?", len(first_name) > len(last_name))

# Arithmetic operations
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("\nArithmetic Results:")
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor Division:", floor_division)

# Circle calculations
radius = 30
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius

print("\nCircle Calculations:")
print("Area of circle:", area_of_circle)
print("Circumference of circle:", circum_of_circle)

# Circle area with user input
user_radius = float(input("\nEnter radius: "))
user_area = math.pi * user_radius ** 2
print("Area with user input:", user_area)

# Collect user info
user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = input("Enter your age: ")

print("\nUser Information:")
print("First Name:", user_first_name)
print("Last Name:", user_last_name)
print("Country:", user_country)
print("Age:", user_age)

# Check Python reserved keywords
print("\nPython Reserved Keywords:")
help('keywords')