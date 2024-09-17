
from lib.pee.melhor_prim.aval.AvaliadorCustoUnif import AvaliadorCustoUnif
from lib.pee.melhor_prim.ProcuraMelhorPrim import ProcuraMelhorPrim

# Procura Custo Uniforme - Explorar primeiro percursos com menor custo
# - Minimização de custo acumulado até cada nó explorado
# - Não tira partido de conhecimento do domínio do problema expresso através da função h(n)
class ProcuraCustoUnif(ProcuraMelhorPrim):

    #Chama uma ProcuraMelhorPrim com o Avaliador de Custo Uniforme
    def __init__(self):
       super().__init__(AvaliadorCustoUnif()) 


   