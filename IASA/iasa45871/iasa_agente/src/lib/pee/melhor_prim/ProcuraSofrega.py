from lib.pee.melhor_prim.aval.AvaliadorSof import AvaliadorSof
from lib.pee.melhor_prim.ProcuraInformada import ProcuraInformada

# Procura Sofrega - Tem como objetivo minimizar a estimativa de custo ("greedy")
# - Não tem em conta o custo do percurso explorado
# - As soluções são sub-óptimas
# - Tem menor complexidade computacional
class ProcuraSofrega(ProcuraInformada):
    
    def __init__(self):
        super().__init__(AvaliadorSof()) 

   