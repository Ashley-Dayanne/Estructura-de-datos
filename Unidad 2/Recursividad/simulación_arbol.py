def es_manzana(fruta):

    # Caso base: si ya sabemos la respuesta final
    if fruta.get("respuesta_final") is not None:
        return fruta["respuesta_final"]

    # Caso recursivo: primera pregunta
    if "es_roja" not in fruta:
        fruta["es_roja"] = input("¿La fruta es roja? (si/no): ").lower()
        # Rama del árbol
        if fruta["es_roja"] == "si":
            return es_manzana({"es_redonda": None})  # siguiente pregunta

        else:
            return es_manzana({"respuesta_final": False})  # no es manzana

    # Segunda pregunta
    if fruta.get("es_redonda") is None:
        fruta["es_redonda"] = input("¿La fruta es redonda? (si/no): ").lower()
        if fruta["es_redonda"] == "si":
            return es_manzana({"respuesta_final": True})  # sí es manzana
        else:
            return es_manzana({"respuesta_final": False})  # no es manzana


# Uso del programa
resultado = es_manzana({})
print("\n¿Es una manzana?:", "Sí" if resultado else "No")
