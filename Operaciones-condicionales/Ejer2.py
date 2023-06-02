#Ejercicio 1
#Realizar un programa que lea 3 numeros introducidos por el usuario y que diga cual de 
# esos 3 numeros es mayor, si el usuario ingresa los mismo numeros debe mostrar un mensaje
# los numeros son iguales

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero: "))
n3 = int(input("Ingrese un numero: "))

if n1 > n2 and n1 > n3:
    print("El numero ", n1 , "es mayor")
if n2 > n1 and n2 > n3:
    print("El numero ", n2 , "es mayor")
if n3 > n1 and n3 > n2:
    print("El numero ", n3 , "es mayor")
else:
    print("Todos son iguales")