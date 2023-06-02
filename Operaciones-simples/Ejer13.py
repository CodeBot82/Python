#Ejercicio 13
#Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla
#la cuenta atras desde ese numero hasta cero separados por comas.

n = int(input("Ingresar un numero: "))

for i in range(n, -1, -1):
    print(i, end = ", ")