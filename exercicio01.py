a=int(input("digite o valor de A: "))
b=int(input("digite o valor de B: "))
c=int(input("digite o valor de C: "))
soma=a+b
if soma >c:
    print(f"a soma de A e B:{soma} é maior que C:{c}")
else:
    if soma ==c:
        print(f"a soma de A e B:{soma} é igual a C:{c}")
    else:
        print(f"a soma de A e B:{soma} é menor que C:{c}")

