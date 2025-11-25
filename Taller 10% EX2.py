#Base del arbol
class NodoCategoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = []  

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

# Construcción del árbol
electronica = NodoCategoria("Electrónica")

# Nivel 1
computadores = NodoCategoria("Computadores")
celulares = NodoCategoria("Celulares")
televisores = NodoCategoria("Televisores")

# Nivel 2
portatiles = NodoCategoria("Portátiles")
escritorio = NodoCategoria("Escritorio")
android = NodoCategoria("Android")
iphone = NodoCategoria("iPhone")

# Conexiones
electronica.agregar_subcategoria(computadores)
electronica.agregar_subcategoria(celulares)
electronica.agregar_subcategoria(televisores)

computadores.agregar_subcategoria(portatiles)
computadores.agregar_subcategoria(escritorio)

celulares.agregar_subcategoria(android)
celulares.agregar_subcategoria(iphone)

# Solución

# 1. PREORDEN (Raíz primero -> Luego hijos)
def preorden(nodo):
    if nodo:
        print(nodo.nombre)  
        for sub in nodo.subcategorias:
            preorden(sub)   

# 2. POSORDEN (Hijos primero -> Luego Raíz)
def posorden(nodo):
    if nodo:
        for sub in nodo.subcategorias:
            posorden(sub)   
        print(nodo.nombre)  

# 3. INORDEN 
def inorden(nodo):
    if nodo:
        if len(nodo.subcategorias) > 0:
            inorden(nodo.subcategorias[0])
        
        print(nodo.nombre)
        
        for sub in nodo.subcategorias[1:]:
            inorden(sub)

# Prints de resultados
if __name__ == "__main__":
    print("=== RECORRIDO PREORDEN ===")
    preorden(electronica)
    print("-" * 30)

    print("=== RECORRIDO INORDEN ===")
    inorden(electronica)
    print("-" * 30)

    print("=== RECORRIDO POSORDEN ===")
    posorden(electronica)
