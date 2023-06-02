#Ejercicio 6
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
#calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla 
#la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal 
#calculado redondeado con dos decimales.

kg = (input("Ingrese su peso en KG: "))
metros = (input("Ingrese su estatura en METROS: "))

imc = round( float(kg) / float(metros) ** 2,2 )

print("Tu índice de masa corporal es " + str(imc))