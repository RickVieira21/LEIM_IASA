import math
from lib.pee.melhor_prim.Heuristica import Heuristica


class HeurManhattan(Heuristica):
    def __init__(self, estado_final):
        self.__estado_final = estado_final

    def h(self, estado):
        pos_atual = estado.posicao
        pos_final = self.__estado_final.posicao
        dist_x = abs(pos_atual[0] - pos_final[0])
        dist_y = abs(pos_atual[1] - pos_final[1])
        return dist_x + dist_y
