from mod.Estado import Estado


class EstadoBlocos(Estado):
    def __init__(self, pilhas):
        self.pilhas = pilhas  # Lista de pilhas de blocos

    @property
    def estado_inicial(self):
        return self.pilhas

    def id_valor(self):
        return hash(tuple(tuple(pilha) for pilha in self.pilhas))

    def __str__(self):
        return str(self.pilhas)

    def objetivo(self, objetivo):
        return self.pilhas[0] == objetivo
