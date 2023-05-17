class Aresta():
    def __init__(self, origem, destino):
        self.origem = origem
        self.destino = destino

    def setOrigem(self, origem):
        self.origem = origem

    def getOrigem(self):
        return self.origem

    def setDestino(self, destino):
        self.destino = destino

    def getDestino(self):
        return  self.destino

    def __str__(self):
        return "A(%s------>%s)" % (self.origem.getId(), self.destino.getId())