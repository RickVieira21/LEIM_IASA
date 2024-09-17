from abc import abstractmethod
from blocos.EstadoBlocos import EstadoBlocos
from mod.Operador import Operador

class OperadorBlocos(Operador):

    def __init__(self, origem, destino, custo):
        self._estado_origem = EstadoBlocos(origem)
        self._estado_destino = EstadoBlocos(destino)
        self.__custo = custo
    
    @abstractmethod
    def aplicar(self, estado):
        pass
    
    # O custo correponde ao número da pilha
    def custo(self, estado, estado_suc):
        pilha_origem = self._estado_origem.pilha
        pilha_destino = self._estado_destino.pilha
        self.__custo = abs(pilha_origem - pilha_destino)
        return self.__custo