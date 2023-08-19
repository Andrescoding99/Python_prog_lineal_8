#Validar un numero del 1 al 10
# a) Que no deje de pedir el numero mientras este fuera del rango
#b ) Si el numero es par o impar

x = 0

x = int(input("Ingrese el numero adecuado: "))

while x < 1 or x > 10:
    print("El numero esta fuera de rango")
    x = int(input("Ingrese el numero adecuado: "))
print("Felicidades el numero esta dentro del rango")

if x % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")