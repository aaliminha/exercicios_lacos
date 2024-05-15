N = int(input("Digite um número inteiro positivo par: "))
if N % 2 != 0 or N <= 0:
    print("Por favor, digite um número inteiro positivo par.")
else:
    print("Números pares de 0 até", N, "em ordem crescente:")
    for i in range(0, N + 1, 2):
        print(i)
