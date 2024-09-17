import math
from mod.Operador import Operador
from mod.agente.EstadoAgente import EstadoAgente
from lib.sae.agente.accao import Accao

# Classe OperadorMover - implementa os métodos necessários para realizar a operação de movimento no modelo do mundo
class OperadorMover(Operador):

    def __init__(self, modelo_mundo, direccao):
        self._ang = direccao.value
        self._modelo_mundo = modelo_mundo
        self._accao = Accao(direccao)

    @property
    def ang(self):
        return self._ang
    
    @property
    def accao(self):
        return self._accao

    #Calculo dos diferenciais - Distância entre o ponto em que estamos até ao ponto que queremos ir
    #Depois calcula a nova nova posicao para o novo estado
    #Por fim verifica se o novo estado é válido (que significa estar no ModeloMundo) e se for faz return
    def aplicar(self, estado):
        x, y = estado.posicao
        dx = round(self._accao.passo * math.cos(self.ang))
        dy = -round(self._accao.passo * math.sin(self.ang))
        nova_pos = x + dx, y + dy
        novo_estado = EstadoAgente(nova_pos)
        if novo_estado in self._modelo_mundo.obter_estados():
           return novo_estado


    #O custo correponde à distância entre o estado atual e sucessor 
    def custo(self, estado, estado_suc):
        distancia = math.dist(estado.posicao, estado_suc.posicao)
        custo = distancia if distancia >= 1 else 1
        return custo

 