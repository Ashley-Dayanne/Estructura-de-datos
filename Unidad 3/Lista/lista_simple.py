class Nodo:
self.dato = dato
self.siguiente = None

class ListaEnlazadaSimple:
"""Lista simplemente enlazada con operaciones básicas.
- insertar_al_inicio: O(1)
- insertar_al_final: O(n)
"""
def __init__(self):
self.cabeza = None

def insertar_al_inicio(self, dato):
"""Inserta un nodo al inicio en O(1)."""
nuevo = Nodo(dato)
nuevo.siguiente = self.cabeza
self.cabeza = nuevo

def insertar_al_final(self, dato):
"""Inserta un nodo al final. Recorrido lineal -> O(n)."""
nuevo = Nodo(dato)
if self.cabeza is None:
self.cabeza = nuevo
return
actual = self.cabeza
while actual.siguiente is not None:
actual = actual.siguiente
actual.siguiente = nuevo

def buscar(self, dato):
"""Busca un valor y devuelve el nodo o None."""
actual = self.cabeza
while actual is not None:
if actual.dato == dato:
return actual
actual = actual.siguiente
return None

def eliminar(self, dato):
"""Elimina la primera ocurrencia del dato. O(n)."""
actual = self.cabeza
previo = None
while actual is not None:
if actual.dato == dato:
if previo is None:
# eliminar cabeza
self.cabeza = actual.siguiente
else:
previo.siguiente = actual.siguiente
return True
previo = actual
actual = actual.siguiente
return False

def __iter__(self):
actual = self.cabeza
while actual is not None:
yield actual.dato
actual = actual.siguiente

def __repr__(self):
return "ListaEnlazadaSimple([" + ", ".join(repr(x) for x in self) + "])"

def imprimir(self):
print("->".join(str(x) for x in self))