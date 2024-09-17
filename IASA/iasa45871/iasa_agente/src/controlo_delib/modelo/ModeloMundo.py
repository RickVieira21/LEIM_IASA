import math
from controlo_delib.modelo.OperadorMover import OperadorMover
from lib.sae.ambiente.direccao import Direccao
from lib.plan.modelo.ModeloPlan import ModeloPlan
from mod.agente.EstadoAgente import EstadoAgente

# Classe ModeloMundo - Extende ModeloPlan
# O modeloMundo representa o "Mundo" em questão, neste caso o cenário em que estamos a trabalhar.
# Contém métodos para obter os diferentes estados, operadores, e elementos.
class ModeloMundo(ModeloPlan):

    def __init__(self):
        self._estado = None
        self._estados = []
        self._elementos = {}
        #Cria um OperadorMover para cada direccao
        self._operadores = [OperadorMover(self, direccao) for direccao in Direccao]
        self._alterado = False


    @property
    def alterado(self):
        return self._alterado

    #Obtem o estado do sistema
    def obter_estado(self):
        return self._estado

    #Obtem a lista de estados do sistema
    def obter_estados(self):
        return self._estados
       
    #Obtem os operadores do sistema
    def obter_operadores(self):
        return self._operadores
 
    #Obtém o elemento na posição correspondente ao estado
    def obter_elemento(self, estado):
        return self._elementos.get(estado.posicao)

    def distancia(self, estado):
        return math.dist(estado.posicao, self._estado.posicao)

    #O estado do agente mudou:
    # - Criar novo estado do agente através da posicao da percepcao
    # - Depois verificar se mudaram, se for diferente:
    # - Atualiza os estados (cópia direta)
    # - Recalcular novos estados admissiveis
    def actualizar(self, percepcao):
        self._estado = EstadoAgente(percepcao.posicao)
        if self._elementos != percepcao.elementos:
           self._elementos = percepcao.elementos
           self._estados = []
           for posicao in percepcao.posicoes:
               self._estados.append(EstadoAgente(posicao))
           self._alterado = True
        else: 
           self._alterado = False

    # Método mostrar para o modelo do mundo 
    # Mostrar elementos - mostra os elementos todos
    # Marcar posicao - marca a posicao atual do agente
    def mostrar(self, vista):
        vista.mostrar_alvos_obst(self._elementos)
        vista.marcar_posicao(self._estado.posicao)
