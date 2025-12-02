def revertir_cadena(cadena):
    # Caso base
    if len(cadena) == 0:
        return cadena
    
    # Llamada recursiva (divide y vencerás)
    return revertir_cadena(cadena[1:]) + cadena[0]


# Ejemplo:
texto = "IA_es_genial"
print("Original:", texto)
print("Revertida:", revertir_cadena(texto))
