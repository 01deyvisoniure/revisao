
repetir="s"
while repetir=="s":
    numero = int(input("digite um numero: "))
    if numero >0:
        if numero%2==0:
            print("o numero é positivo e par.")

        else:
            print("o numero é positivo e impar.")
    else:
        if numero%2==0:
            print("o numero  é negativo e par.")
        else:
            print("o numero é negativo e impar.")
    repetir = input("quer repetir? ")