import random
import time
import matplotlib.pyplot as plt

# ===================
# MEDICIÓN DE TIEMPO
# ===================
def medir_tiempo_promedio(func, *args, ejecuciones=1):
    """Rutina de temporización de alta precisión en nanosegundos."""
    tiempos = []
    for _ in range(ejecuciones):
        inicio = time.perf_counter()
        func(*args)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return sum(tiempos) / len(tiempos)

# =======================================
# MÓDULO 1: IMPLEMENTACIÓN DE ALGORITMOS
# =======================================

def insertion_sort(arr): # Algoritmo O(n^2) 
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr): # Algoritmo O(n log n) 
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]; R = arr[mid:]
        merge_sort(L); merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]: arr[k] = L[i]; i += 1
            else: arr[k] = R[j]; j += 1
            k += 1
        while i < len(L): arr[k] = L[i]; i += 1; k += 1
        while j < len(R): arr[k] = R[j]; j += 1; k += 1

def busqueda_secuencial(arr, x): # O(n) 
    for i in range(len(arr)):
        if arr[i] == x: return i
    return -1

def busqueda_binaria(arr, x): # O(log n) 
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == x: return mid
        elif arr[mid] < x: low = mid + 1
        else: high = mid - 1
    return -1

class Stack: # Complejidad O(1) 
    def __init__(self): self.items = []
    def push(self, x): self.items.append(x)
    def pop(self): return self.items.pop() if self.items else None

class Queue: # Complejidad O(1) 
    def __init__(self): self.items = []
    def enqueue(self, x): self.items.append(x)
    def dequeue(self): return self.items.pop(0) if self.items else None

# ===========================================
# MÓDULO 2 Y 3: MOTOR DE MEDICIÓN Y REPORTES
# ===========================================

print("="*60)
print("UNIVERSIDAD DE XALAPA - PROYECTO FINAL ESTRUCTURA DE DATOS")
print("GENERADOR DE REPORTES DE RENDIMIENTO")
print("="*60 + "\n")

# --- 1. MEDICIÓN DE ESTRUCTURAS LINEALES  ---
N_lin = 20000
pila, cola = Stack(), Queue()
t_push = medir_tiempo_promedio(lambda: [pila.push(i) for i in range(N_lin)])
t_pop = medir_tiempo_promedio(lambda: [pila.pop() for _ in range(N_lin)])
t_enq = medir_tiempo_promedio(lambda: [cola.enqueue(i) for i in range(N_lin)])
t_deq = medir_tiempo_promedio(lambda: [cola.dequeue() for _ in range(N_lin)])

print(f"--- 1. ESTRUCTURAS LINEALES (N={N_lin} operaciones) ---")
print(f"Pila  - Push: {t_push:.6f}s | Pop: {t_pop:.6f}s")
print(f"Cola  - Enqueue: {t_enq:.6f}s | Dequeue: {t_deq:.6f}s")
print(f"Costo unitario aprox: {((t_push+t_pop+t_enq+t_deq)/(4*N_lin)):.10f}s (Valida O(1))\n")

# --- 2. MEDICIÓN DE BÚSQUEDAS  ---
N_busq = 100000
datos_busq = sorted([random.randint(1, N_busq*10) for _ in range(N_busq)])
objetivo = datos_busq[-1] # Peor caso 
t_sec = medir_tiempo_promedio(busqueda_secuencial, datos_busq, objetivo, ejecuciones=5)
t_bin = medir_tiempo_promedio(busqueda_binaria, datos_busq, objetivo, ejecuciones=5)

print(f"--- 2. BÚSQUEDAS (Peor Caso, N={N_busq}) ---")
print(f"Búsqueda Secuencial O(n): {t_sec:.8f}s")
print(f"Búsqueda Binaria O(log n): {t_bin:.8f}s")
print(f"Diferencia de eficiencia: {int(t_sec/t_bin)}x veces más rápida la binaria.\n")

# --- 3. DATOS PARA GRÁFICA 1: COMPARACIÓN DE ESCENARIOS ---
N_esc = 10000
mejor = list(range(N_esc)) # MC 
peor = mejor[::-1] # PC
promedio = [random.randint(1, N_esc) for _ in range(N_esc)] # CP

print(f"--- 3. RECOPILACIÓN DATOS ESCENARIOS (N={N_esc}) ---")
# Medición Insertion Sort
t_ins_mejor = medir_tiempo_promedio(insertion_sort, mejor.copy())
t_ins_prom = medir_tiempo_promedio(insertion_sort, promedio.copy())
t_ins_peor = medir_tiempo_promedio(insertion_sort, peor.copy())
t_ins_casos = [t_ins_mejor, t_ins_prom, t_ins_peor]

# Medición Merge Sort
t_mer_mejor = medir_tiempo_promedio(merge_sort, mejor.copy())
t_mer_prom = medir_tiempo_promedio(merge_sort, promedio.copy())
t_mer_peor = medir_tiempo_promedio(merge_sort, peor.copy())
t_mer_casos = [t_mer_mejor, t_mer_prom, t_mer_peor]

print(f"Algoritmo Insertion Sort O(n²):   MC={t_ins_mejor:.4f}s | CP={t_ins_prom:.4f}s | PC={t_ins_peor:.4f}s")
print(f"Algoritmo Merge Sort O(n log n): MC={t_mer_mejor:.4f}s | CP={t_mer_prom:.4f}s | PC={t_mer_peor:.4f}s\n")

# --- 4. DATOS PARA GRÁFICA 2: ESCALABILIDAD [cite: 39] ---

tamanos = [1000, 5000, 10000, 20000, 30000]
escalabilidad_ins = []
escalabilidad_mer = []

print(f"--- 4. RECOPILACIÓN DATOS ESCALABILIDAD (N Variable) ---")
print(f"{'N Elements':<12} | {'O(n²) Time':<12} | {'O(n log n) Time':<12}")
print("-" * 45)

for n in tamanos:
    datos = [random.randint(1, n) for _ in range(n)]
    t_i = medir_tiempo_promedio(insertion_sort, datos.copy())
    t_m = medir_tiempo_promedio(merge_sort, datos.copy())
    escalabilidad_ins.append(t_i)
    escalabilidad_mer.append(t_m)
    print(f"{n:<12} | {t_i:<12.5f} | {t_m:<12.5f}")

# =======================
# GENERACIÓN DE GRÁFICAS
# =======================

# Gráfica 1: Comparación Escenarios
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
casos = ["Mejor Caso", "Caso Promedio", "Peor Caso"]
x = range(len(casos))
plt.bar([i - 0.2 for i in x], t_ins_casos, width=0.4, label="Insertion Sort $O(n^{2})$", color='salmon')
plt.bar([i + 0.2 for i in x], t_mer_casos, width=0.4, label="Merge Sort $O(n \log n)$", color='skyblue')
plt.xticks(x, casos)
plt.ylabel("Tiempo (s)")
plt.title("Comparación Escenarios ($N=10,000$)")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Gráfica 2: Escalabilidad
plt.subplot(1, 2, 2)
plt.plot(tamanos, escalabilidad_ins, marker='o', color='red', label="Insertion Sort $O(n^{2})$")
plt.plot(tamanos, escalabilidad_mer, marker='o', color='blue', label="Merge Sort $O(n \log n)$")
plt.xlabel("Tamaño de Datos (N)")
plt.ylabel("Tiempo (s)")
plt.title("Escalabilidad y Complejidad Teórica")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
print("\nGenerando gráficas comparativas...")
plt.show()
