def fibonacci():
    a, b = 1, 2
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b
soma_pares = 0
for termo in fibonacci():
    if termo > 4000000:
        break
    if termo % 2 == 0:
        soma_pares += termo
print("A soma dos termos pares da sequência de Fibonacci até 4 milhões é:", soma_pares)
