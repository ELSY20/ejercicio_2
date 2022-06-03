import math


cantidad = int(input("Cantidad a invertir: "))
interesAnual = int(input("Interes anual: "))
years = int(input("Número de años: "))

capitalFinal = cantidad * math.pow((interesAnual / 100 + 1),years) 

print(round(capitalFinal,2))