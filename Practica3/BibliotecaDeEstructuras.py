class GenericList: #Lista generica
    def __init__(self):
        self.items = []
    
    def add(self, item): #Añadir elemento
        self.items.append(item)
    
    def insert(self, index, item): #Insertar en posición
        if 0 <= index <= len(self.items):
            self.items.insert(index, item)
        else:
            print(f"Índice fuera de rango: {index}")
    
    def remove(self, item):#Eliminar aparición de un elemento
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"Elemento {item} no encontrado en la lista")
    
    def pop(self, index=None): #Eliminar elemento en posición indicada
        if index is None:
            return self.items.pop()  # Elimina el último si no se especifica un índice
        elif 0 <= index < len(self.items):
            return self.items.pop(index)
        else:
            print(f"Índice fuera de rango: {index}")
            return None
    
    def get(self, index): #Obtener elemento en posición
        if 0 <= index < len(self.items):
            return self.items[index]
        else:
            print(f"Índice fuera de rango: {index}")
            return None
    
    def size(self): #Tamaño de lista
        return len(self.items)
    
    def is_empty(self): #Lista vacia
        return len(self.items) == 0
    
    def clear(self): #Vaciar
        self.items.clear()
    
    def __str__(self):#Visualizar lista 
        return str(self.items)

class Queue: #Cola FIFO
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item): #Añadir al final
        self.queue.append(item)
    
    def dequeue(self): #Eliminar y mostrar elemento al frente 
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("La cola está vacía")
            return None
    
    def front(self): #Elemento al frente sin eliminar
        if not self.is_empty():
            return self.queue[0]
        else:
            print("La cola está vacía")
            return None
    
    def is_empty(self): #Cola vacia
        return len(self.queue) == 0
    
    def size(self): #Tamaño de cola
        return len(self.queue)
    
    def clear(self): #Vaciar colar
        self.queue.clear()
    
    def __str__(self): #Visualizar cola 
        return str(self.queue)

class Stack: #Fila LIFO
    def __init__(self):
        self.stack = []
    
    def push(self, item): #Añadir elemento en la cima
        self.stack.append(item)
    
    def pop(self): #Eliminar y mostrar elemento en la cima
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("La pila está vacía")
            return None
    
    def top(self): #Elemento de la cima sin eliminar
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("La pila está vacía")
            return None
    
    def is_empty(self): #Pila vacia
        return len(self.stack) == 0
    
    def size(self): #Tamaño de pila
        return len(self.stack)
    
    def clear(self): #Vaciar pila
        self.stack.clear()
    
    def __str__(self): #Visualizar pila
        return str(self.stack)