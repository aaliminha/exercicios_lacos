numero = int(input("Digite um número inteiro: "))
if numero <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    soma_divisores = 0

    for i in range(1, numero):
        if numero % i == 0:
            soma_divisores += i

    print("A soma dos divisores de", numero, "é:", soma_divisores)
