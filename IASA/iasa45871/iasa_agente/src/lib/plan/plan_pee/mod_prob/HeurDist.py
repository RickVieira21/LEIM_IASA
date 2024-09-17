import math
from lib.pee.melhor_prim.Heuristica import Heuristica


# Classe HeurDist - Extende Heuristica
# É uma implementação da classe abstrata Heuristica e é utilizada para calcular a heurística de distância entre estados na procura informada.

# No construtor da classe, é recebido o estado final, que representa o estado do destino desejado. 
# O estado final é guardado para ser utilizado posteriormente no cálculo da heurística.
class HeurDist(Heuristica):

    def __init__(self, estado_final):
        self.__estado_final = estado_final
    
    # Calcular a heuristica da distancia para os estados recebidos.
    # Neste caso, a heurística é calculada como a distância euclidiana entre a posição do estado atual e a posição do estado final. 
    # A função math.dist é utilizada para calcular essa distância.
    def h(self, estado):
         return math.dist(estado.posicao, self.__estado_final.posicao)
    
 
