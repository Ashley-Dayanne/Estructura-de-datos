def torres_hanoi(n, origen, destino, auxiliar):

    # Caso base
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return

    # Paso 1: mover N-1 discos del origen al auxiliar
    torres_hanoi(n - 1, origen, auxiliar, destino)

    # Paso 2: mover el disco más grande al destino
    print(f"Mover disco {n} de {origen} a {destino}")

    # Paso 3: mover los N-1 discos del auxiliar al destino
    torres_hanoi(n - 1, auxiliar, destino, origen)


# Ejemplo de uso
n_discos = 3
torres_hanoi(n_discos, "A", "C", "B")
