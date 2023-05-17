class Vertice():
    def __init__(self, id):
        self.id = id;
        self.visitado = False
        self.predecessor = []

    def setVisitado(self, valor):
        self.visitado = valor

    def getVisitado(self):
        return self.visitado

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id