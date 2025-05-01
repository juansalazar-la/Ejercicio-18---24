def mayor(a,b):
    if a > b:
        num= a
    else:
        num=b
    return num

def menor(a,b):
    if a > b:
        num1= b
    else:
        num1=a
    return num1


primer_num=float(input("Introduce el primer número: "))
segundo_num=float(input("Introduce el segundo número: "))
print(f"El número mayor es {mayor(primer_num,segundo_num)} y el número menor es {menor(primer_num,segundo_num)}")