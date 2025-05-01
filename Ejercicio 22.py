
num=int(input("Ingrese un número entero: "))

impares= []

if num > 0:
    x= 0 
    while num > x:
        if x % 2 != 0:
            impares=impares + [x]
        x+=1

else:
    x= -1
    while num < x:
        if x % 2 != 0:
            impares=impares + [x]
        x -= 1

print(f"Los números impares menores que {num} son: {impares}")




    