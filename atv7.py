menor_valor = None
maior_valor = None
for i in range(10):
    valor = int(input("Digite um número: "))
    if menor_valor is None or valor < menor_valor:
        menor_valor = valor
    if maior_valor is None or valor > maior_valor:
        maior_valor = valor
print("O menor valor digitado é:", menor_valor)
print("O maior valor digitado é:", maior_valor)
