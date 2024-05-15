N = int(input("Digite um número inteiro positivo par: "))
if N % 2 != 0 or N <= 0:
    print("Por favor, digite um número inteiro positivo par.")
else:
    print("Números pares de", N, "até 0 em ordem decrescente:")
    for i in range(N, -1, -2):
        print(i)
