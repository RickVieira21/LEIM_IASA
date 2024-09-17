import math
from lib.pee.melhor_prim.Heuristica import Heuristica


class HeurBlocos(Heuristica):

    def __init__(self, estado_final):
        self.__estado_final = estado_final
    
    def h(self, estado):
        distancia_total = 0
        for pilha in estado.blocos:
            # Verifica se a pilha contém o estado final
            if self.__estado_final in pilha:
                # Calcula a distância desde do estado final até à primeira pilha
                distancia = len(pilha) - pilha.index(self.__estado_final)
                distancia_total += distancia
        return distancia_total
 
