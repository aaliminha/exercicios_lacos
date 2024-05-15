def primeiro_multiplo(numero):
    atual = numero + 1
    while True:
        if atual % 11 == 0 or atual % 13 == 0 or atual % 17 == 0:
            return atual
        atual += 1

numero_dado = int(input("Digite um número: "))

primeiro = primeiro_multiplo(numero_dado)

print("O primeiro múltiplo de 11, 13 ou 17 após", numero_dado, "é:", primeiro)