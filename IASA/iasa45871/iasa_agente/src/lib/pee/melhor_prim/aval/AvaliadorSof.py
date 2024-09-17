from lib.pee.melhor_prim.aval.AvaliadorHeur import AvaliadorHeur

#A ProcuraSofrega é uma estratégia de busca greedy), em que a prioridade de um nó é a heurística do estado correspondente. 
# Portanto, o método prioridade pode simplesmente retornar o valor da heurística do estado atual do nó
# O avaliador da ProcuraSofrega estará definido para retornar a heurística do estado atual do nó.
class AvaliadorSof(AvaliadorHeur):
    
    def prioridade(self, no):
        return self._heuristica.h(no.estado)

   
    