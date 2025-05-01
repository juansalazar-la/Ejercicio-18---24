import math

a=float(input("Ingrese el coeficiente a:"))
b=float(input("Ingrese el coeficiente b:"))
c=float(input("Ingrese el coeficiente c:"))

#Verificar si es una ecuación cudrática o lineal
if a == 0:
    if b != 0:
        x= -c / b
        print(f"Es una ecuación lineal. La solución es: x = {x}")
    elif c == 0:
        print(f"Es una ecuación lineal. Tiene infinitas soluciones")
    else:
        print(f"Es una ecuación lineal. No tiene soluciones")

else:
    discriminante= b ** 2 - 4 * a * c #formula del discriminante para hallar las soluciones
    
    if discriminante > 0:   #Si el discriminante es positivo, la ecuación tiene dos soluciones
        x1= (-b + math.sqrt(discriminante)) / (2 * a)
        x2= (-b - math.sqrt(discriminante)) / (2 * a)
        print(f"La ecuación tiene dos soluciones reales, x1= {x1} y x2={x2}")

    elif discriminante == 0:   #Si el discriminante es igual a 0, la ecuación tiene una solución
        x= -b / (2 * a)
        print(f"La ecuación tiene una solución, x= {x}")

    else:                      #Si el discriminante es negativo, la ecuación no tiene soluciones reales
        print("La ecuación no tiene soluciones reales")



