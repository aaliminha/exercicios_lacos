soma = 0
for i in range(3, 1000, 3):
    soma += i
for i in range(5, 1000, 5):
    soma += i
for i in range(15, 1000, 15):
    soma -= i
print("A soma dos múltiplos de 3 ou 5 abaixo de 1000 é:", soma)
