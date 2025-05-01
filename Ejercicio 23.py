num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))

a= abs(num1)
b= abs(num2)

while b != 0:
    a,b=b, a % b

print(f"El maximo común divisor de {num1} y {num2} es: {a}")