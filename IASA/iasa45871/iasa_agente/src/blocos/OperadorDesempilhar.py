from blocos.OperadorBlocos import OperadorBlocos

class OperadorDesempilhar(OperadorBlocos):
    def __init__(self, origem, destino, custo):
        super().__init__(origem, destino, custo)

    def aplicar(self, estado):
        bloco_desempilhado = estado.desempilhar_bloco()
        if bloco_desempilhado is not None:
            estado_destino = self._estado_destino.adicionar_bloco(bloco_desempilhado)
            return estado_destino
        else:
            return None