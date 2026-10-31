class Nodo:
    def __init__(self, numero):
    
        self.numero = numero
        self.siguiente = None


class ListasEnlazadas:
    def __init__(self):
        self.cabeza = None

    def Insertar_Nodo_al_Inicio(self, numero):
        nuevo_nodo = Nodo(numero)
        
        if(self.cabeza is None):
            self.cabeza = Nodo(numero)
            return
            
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def Insertar_Nodo_al_Final(self, numero):
        nuevo_nodo = Nodo(numero)
        
        if(self.cabeza == None):
            self.cabeza = nuevo_nodo
            return
            
        # Referencia temporal
        actual = self.cabeza
        
        while(actual.siguiente):
            actual = actual.siguiente
            
        actual.siguiente = nuevo_nodo

    def Eliminar_Nodo_al_Inicio(self):
        
        if(self.cabeza == None):
            print("La lista esta vacia")
            return
            
        self.cabeza = self.cabeza.siguiente

    def Eliminar_Nodo_al_Final(self):
        
        if(self.cabeza == None):
            print("La lista esta vacia")
            return
            
        if(self.cabeza.siguiente == None):
            self.cabeza = None
            return
            
        # Referencia temporal
        actual = self.cabeza
        
        while(actual.siguiente.siguiente):
            actual = actual.siguiente
            
        actual.siguiente = None

    def Imprimir_ListaEnlazada(self):
        actual = self.cabeza
        
        while(actual):
            print(actual.numero, " -> ", end=" ")
            actual = actual.siguiente
            
        print("None")


Mi_lista = ListasEnlazadas()

Mi_lista.Insertar_Nodo_al_Inicio(5)
Mi_lista.Insertar_Nodo_al_Inicio(4)
Mi_lista.Insertar_Nodo_al_Inicio(3)

print("Lista original:")
Mi_lista.Imprimir_ListaEnlazada()
Mi_lista.Eliminar_Nodo_al_Inicio()
print("Eliminar al inicio:")
Mi_lista.Imprimir_ListaEnlazada()
Mi_lista.Eliminar_Nodo_al_Final()
print("Eliminar al final:")
Mi_lista.Imprimir_ListaEnlazada()