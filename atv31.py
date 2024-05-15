saque = int(input("Digite o valor do saque: "))
notas_disponiveis = [200, 100, 50, 20, 10, 5, 2, 1]
quantidade_notas = {}
for nota in notas_disponiveis:
    quantidade_notas[nota] = saque // nota 
    saque %= nota 
print("Quantidade de notas necessárias para o saque:")
for nota, quantidade in quantidade_notas.items():
    print(f"Notas de {nota} reais: {quantidade}")
