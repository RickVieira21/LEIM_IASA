from mod.Estado import Estado
from lib.sae.ambiente.posicao import Posicao


# Classe EstadoAgente - Vai guardar a posicao (x,y) do agente no construtor e o seu valor de id
# Do ponto de vista teórico contém os dados do próprio agente. 
class EstadoAgente(Estado):

    def __init__(self, posicao):
        self._posicao = posicao

    def id_valor(self):
        return self._posicao.__hash__()
 
    @property
    def posicao(self):
        return self._posicao