salario = 2000
aumento = 0.015 
for ano in range(1996, 2023): 
    salario += salario * aumento
    aumento *= 2
print("O salário atual do funcionário em 2022 é de R$", salario)
