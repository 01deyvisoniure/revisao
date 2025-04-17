altura=float(input("digite sua altura: "))
peso=float(input("digite seu peso: "))
imc=peso/(altura*altura)
print(f"{imc:.1f}")

if imc <=18.5:
    print(f"abaixo do peso")
else:
    if imc>= 18.6 and imc <= 24.9:
        print("peso  ideal")
    else:
        if imc >= 25 and imc <= 29.9:
            print("levemente acima do peso")
        else:
            if imc >= 30 and imc <= 34.9:
                print("obesidade grau 1")
            else:
                if imc >= 35 and imc <= 39.9:
                    print("obesidade grau 2")
                else:
                    print("obesidade grau 3")


