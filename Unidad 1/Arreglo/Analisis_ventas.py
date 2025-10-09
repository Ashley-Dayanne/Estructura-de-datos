# Análisis de ventas diarias con arreglos
''' Problema: Una tienda en línea registra las ventas de cada día de la semana en un arreglo de tamaño 7. Cada posición representa el total de ventas de un día (Lunes a Domingo). '''
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
ventas = [2580, 2770, 7595, 3264, 4500, 9372, 7205]

# Total ventas por día
print(f"Total vendido por día:\n {dias[0]}: {ventas[0]}\n {dias[1]}: {ventas[1]}\n {dias[2]}: {ventas[2]}\n {dias[3]}: {ventas[3]}\n {dias[4]}: {ventas[4]}\n {dias[5]}: {ventas[5]}\n {dias[6]}: {ventas[6]}")

# Total de ventas de la semana
total_ventas = sum(ventas)
print("Total de ventas de la semana: ", total_ventas)

mas_ventas = max(ventas)
dia_max = dias[ventas.index(mas_ventas)]
print(f"El día con más ventas fue el día {dia_max}")

menos_ventas = min(ventas)
dia_min = dias[ventas.index(menos_ventas)]
print(f"El día con menos ventas fue el día {dia_min}")
