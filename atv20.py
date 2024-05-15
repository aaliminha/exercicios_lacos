numeros_lidos = 0
numeros_pares = 0
while True:
    numero = int(input("Digite um número inteiro (digite 1000 para sair): "))
    if numero == 1000:
        break
    numeros_lidos += 1
    if numero % 2 == 0:
        numeros_pares += 1
print("Número de dados lidos:", numeros_lidos)
print("Número de valores pares:", numeros_pares)
