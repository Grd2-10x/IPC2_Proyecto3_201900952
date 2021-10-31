class Nodo:
    def __init__(self, Instrucc):
        self.Instrucc = Instrucc
        self.siguiente = None
        self.anterior = None


class Prod:
    def __init__(self,nombre):
        self.nombre = nombre
        self.lista_elab = Lista_Elab()
        self.siguiente = None
        self.anterior = None

class ListaProd():
    def __init__(self):
        self.inicio = None

    def insertar(self, nombre): #insertar
        nuevo = Prod(nombre)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            nuevo.anterior = tmp

    def mostrar(self):
        tmp = self.inicio
        while tmp is not None:
            print('Nombre Producto:', tmp.nombre)
            tmp = tmp.siguiente

class Lista_Elab():
    def __init__(self):
        self.inicio = None

    def insertar(self, Instrucc):  # insertar
        nuevo = Nodo(Instrucc)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            nuevo.anterior = tmp

    def mostrarProds(self):
        tmp = self.inicio
        while tmp is not None:
            print('Intrucciones:', tmp.Instrucc)
            tmp = tmp.siguiente