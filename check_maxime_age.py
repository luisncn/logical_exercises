"""
Program: asks for the name and age of 3 people, the program must
indicate who is the oldest person, additional if the oldest
is greater than 60 prints a message, otherwise a different message
"""

name_age = {}

for x in range(0, 3):
    global name, age
    name = input("Introduce tu nombre: ")
    age = int(input("Introduce tu edad: "))
    for y in (0, 3):
        name_age[name] = age

print(f"La persona con mayor edad es: {max(name_age, key=name_age.get)}")

if name_age[max(name_age, key=name_age.get)] > 60:
    print("Jubilado")
else:
    print("continua trabajando")
