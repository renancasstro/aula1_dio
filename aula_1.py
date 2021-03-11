# Imprimir números inteiros pares de zero até o valor que o usuário informar#

num = 0
count: int = 0
total = int(input("Informe o valor máximo: "))
if total > 0:
    print("A seguir todos os numeros pares de 0 até", total)
    while num < total:
        num += 1
        resto = num % 2
        if total - num >= 2:
            if resto == 0:
                print(num, end=", ")
                count += 1
        else:
            if resto == 0:
                print(num, end=". ")
                count += 1
else:
    if total == 0:
        print("0 é par")
        count += 1
    else:
        print("A seguir todos os numeros pares de 0 até", total)
        while num > total:
            num -= 1
            resto = num % 2
            if num - total >= 2:
                if resto == 0:
                    print(num, end=", ")
                    count += 1
            else:
                if resto == 0:
                    print(num, end=". ")
                    count += 1
print("")  # A intenção é que a próxima linha seja impressa abaixo dos números
print("Quantidade de números pares até", total, "é:", count)
