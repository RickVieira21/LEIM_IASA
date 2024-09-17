from lib.pee.melhor_prim.aval.AvaliadorHeur import AvaliadorHeur
from lib.pee.melhor_prim.ProcuraMelhorPrim import ProcuraMelhorPrim

# Procura Informada - Estratégia de exploração do espaço de estados que tira partido do conhecimento d dominio do problema
# para ordenar a fronteira de exploração.
# (A procura não informada é uma procura "cega", onde não temos acesso a esse tipo de informação:
# A Procura em profundidade e em largura são dois exemplos de procura não informada!)

#Código: 
# Primeiro definimos a heuristica com o método definir heuristica do Avaliador de Heuristicas
# Depois já podemos fazer return do super (procura melhor primeiro) do método procurar com o problema
# O avaliador está a ordenar as filas!
class ProcuraInformada(ProcuraMelhorPrim):
    
    def procurar(self, problema, heuristica):
        self._problema = problema
        self._heuristica = heuristica
        self._avaliador.definir_heuristica(heuristica)
        return super().procurar(problema)
        




   