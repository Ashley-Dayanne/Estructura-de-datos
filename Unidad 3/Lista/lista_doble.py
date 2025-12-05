class NodoDoble:
"""Inserta al inicio en O(1)."""
nuevo = NodoDoble(dato)
nuevo.siguiente = self.cabeza
if self.cabeza is not None:
self.cabeza.previo = nuevo
self.cabeza = nuevo
if self.cola is None:
# lista vacía, cola también apunta al nuevo
self.cola = nuevo

def insertar_al_final(self, dato):
"""Inserta al final en O(1) usando self.cola."""
nuevo = NodoDoble(dato)
if self.cola is None:
# lista vacía
self.cabeza = nuevo
self.cola = nuevo
return
self.cola.siguiente = nuevo
nuevo.previo = self.cola
self.cola = nuevo

def buscar(self, dato):
actual = self.cabeza
while actual is not None:
if actual.dato == dato:
return actual
actual = actual.siguiente
return None

def eliminar(self, dato):
actual = self.cabeza
while actual is not None:
if actual.dato == dato:
if actual.previo is not None:
actual.previo.siguiente = actual.siguiente
else:
# eliminando cabeza
self.cabeza = actual.siguiente
if actual.siguiente is not None:
actual.siguiente.previo = actual.previo
else:
# eliminando cola
self.cola = actual.previo
return True
actual = actual.siguiente
return False

def __iter__(self):
actual = self.cabeza
while actual is not None:
yield actual.dato
actual = actual.siguiente

def iter_reversa(self):
actual = self.cola
while actual is not None:
yield actual.dato
actual = actual.previo

def __repr__(self):
return "ListaDoblementeEnlazada([" + ", ".join(repr(x) for x in self) + "])"

def imprimir_adelante(self):
print("<->".join(str(x) for x in self))

def imprimir_atras(self):
print("<->".join(str(x) for x in self.iter_reversa()))