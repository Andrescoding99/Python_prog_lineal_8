"""Numero del 1 al 10 con For"""

print("Estructura For")

i = 0
#Manipulando al iterador
for i in range (1,11):
    print(i)
print()
#Engañar a la vista
for i in range (10):
    print(i + 2)

"""Numero del 1 al 10 con While"""

print("\nEstructura While")

x = 0
#Manipulando al iterador
while x < 10:
    x = x + 2
    print(x)
print()
#Engañar a la vista
x = 0
while x > -10:
    print(x - 1)
    x = x - 1
    