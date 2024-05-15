def eh_par(numero):
    return numero % 2 == 0
def eh_impar(numero):
    return numero % 2 != 0
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
soma_pares = 0
multiplicacao_impares = 1
for numero in range(numero1, numero2 + 1):
    if eh_par(numero):
        soma_pares += numero
    else:
        multiplicacao_impares *= numero

print("A soma dos números pares é:", soma_pares)
print("A multiplicação dos números ímpares é:", multiplicacao_impares)
