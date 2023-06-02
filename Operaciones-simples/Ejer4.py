#Ejercicio 4
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y 
#el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas = int(input("Ingrese horas: "))
coste = 12
pago_total = ''

pago_total = horas * coste

print("El pago total es: ", pago_total)