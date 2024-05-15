n = int(input("Digite um número inteiro positivo: "))
if n <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    soma = (n * (n + 1)) // 2
    print("A soma dos", n, "primeiros números naturais é:", soma)
