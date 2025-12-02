def fibonacci(n):
    # Caso base
    if n <= 1:
        return n

    # Caso recursivo
    return fibonacci(n - 1) + fibonacci(n - 2)


# Imprimir los primeros 10 números de Fibonacci
print("Primeros 10 números de Fibonacci:")
for i in range(10):
    print(fibonacci(i), end=" ")
