from lib.pee.mec_proc.ProcuraGrafo import ProcuraGrafo
from lib.pee.mec_proc.fronteira.FronteiraPrioridade import FronteiraPrioridade

# ProcuraMelhorPrim -> A fronteira de exploração é ordenada por ordem crescente do custo da solução  através de cada nó 
class ProcuraMelhorPrim(ProcuraGrafo):
    
     def __init__(self, avaliador):
         self._avaliador = avaliador
         super().__init__(FronteiraPrioridade(avaliador))

     # Antes tinhamos que -> se não estava nos explorados era para manter
     # Agora precisamos ainda de ver dentro dos nós explorados o custo dos nós, e se atingimos esse mesmo estado através de um nó com custo inferior
     # Se o custo for inferior queremos manter, se for superior descartamos
     def _manter(self, no):
         return super()._manter(no) or no._custo < self._explorados[no.estado].custo

         
         
       



   