#Ejercicio 3
#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
#Si el divisor es cero el programa debe mostrar un error.

print("$Code_bot")

N1 = float(input("Ingrese un numero: "))
N2 = float(input("Ingrese un numero: "))

if N2 == 0:
    print("ERROR no se puede dividir")
else:
    result = N1 / N2
    print("El resultado es:",result)