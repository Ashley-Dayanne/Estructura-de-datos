'''
 Priorización de Alertas de un istsema de Detección de fraudes
 Problema: Un sistema de detección de fraudes ha generado 10 alertas, cada una con una puntuación de riesgo entre 0 y 1. Implementa el algoritmo de ordenamiento por selección para ordenar las alertas de mayor a menor riesgo.
 Objetivo: Comprender cómo el ordenamiento de las alertas por nivel de riesgo puede ayudar a priorizar la atención de los casos más críticos en sistemas automatizados de seguridad.
'''

# Lista con las puntuaciones de riesgo entre 0 y 1
alertas = [0.32, 0.85, 0.10, 0.67, 0.93, 0.54, 0.76, 0.48, 0.29, 0.61]

print("Alertas sin ordenar:")
print(alertas)

# Aplicar algoritmo de ordenamiento por selección (de mayor a menor)
n = len(alertas)

for i in range(n):
    # Suponemos que el elemento i es el de mayor riesgo
    maximo = i
    for j in range(i + 1, n):
        if alertas[j] > alertas[maximo]:
            maximo = j
    # Intercambiar posiciones
    temp = alertas[i]
    alertas[i] = alertas[maximo]
    alertas[maximo] = temp

print("\nAlertas ordenadas por riesgo (de mayor a menor):")
print(alertas)