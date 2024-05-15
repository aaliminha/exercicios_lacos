def calcular_meses_igualdade(salario_carlos, salario_joao, taxa_poupanca, taxa_renda_fixa):
    saldo_carlos = salario_carlos
    saldo_joao = salario_joao
    meses = 0

    while saldo_joao <= saldo_carlos:
        saldo_carlos *= 1 + taxa_poupanca
        saldo_joao *= 1 + taxa_renda_fixa
        meses += 1

    return meses

salario_carlos = float(input("Digite o salário de Carlos: "))
salario_joao = salario_carlos / 3
taxa_poupanca = float(input("Digite a taxa de rendimento da poupança (em % ao mês): ")) / 100
taxa_renda_fixa = float(input("Digite a taxa de rendimento da renda fixa (em % ao mês): ")) / 100
meses = calcular_meses_igualdade(salario_carlos, salario_joao, taxa_poupanca, taxa_renda_fixa)
print(f"São necessários {meses} meses para que o valor pertencente a João iguale ou ultrapasse o valor pertencente a Carlos.")
