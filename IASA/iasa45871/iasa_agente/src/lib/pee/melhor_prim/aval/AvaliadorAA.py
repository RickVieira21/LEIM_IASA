from lib.pee.melhor_prim.aval.AvaliadorHeur import AvaliadorHeur

# Vai returnar o h do avaliador
# No método prioridade(), é somado o custo acumulado do nó atual ao valor da heurística h do estado desse nó. 
# A heurística h é herdada da classe AvaliadorHeur.
class AvaliadorAA(AvaliadorHeur):
    
    def prioridade(self, no):
        return no.custo + self._heuristica.h(no.estado)

    