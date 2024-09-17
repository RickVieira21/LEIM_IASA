from blocos.OperadorBlocos import OperadorBlocos

class OperadorEmpilhar(OperadorBlocos):
    def __init__(self, origem, destino, custo):
        super().__init__(origem, destino, custo)

    def aplicar(self, estado):
        estado.empilhar_bloco(self._estado_destino.obter_bloco())
        return estado