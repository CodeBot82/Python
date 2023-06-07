#Ejercicio 15
#Escriba un programa que pida la anchura y altura de un rectángulo 
#y lo dibuje con caracteres producto (*):

print("$Code_bot")

a = int(input("Ingrese la anchura: "))
b = int(input("Ingrese la altura: "))

for i in range(b):
    for j in range(a):
        print("* ", end="")
    print()