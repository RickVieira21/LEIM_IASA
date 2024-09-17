from heapq import heappop, heappush
from lib.pee.mec_proc.fronteira.Fronteira import Fronteira

class FronteiraPrioridade(Fronteira):
    
    # O construtor guarda o avaliador 
    def __init__(self, avaliador):
        self._avaliador = avaliador

    # Avalia a prioridade do nó que é inserido na lista de acordo com a sua ordem natural (heappush para inserir)
    # O critério de ordenação é a prioridade
    def inserir(self, no):        
        prioridade = self._avaliador.prioridade(no)
        heappush(self._nos, (prioridade, no))
        super().nos_memoria()

    # Remove um nó (heappop para remover)
    # Vamos receber o nó e a prioridade -> Não queremos a prioridade, por isso fazemos "_ , no"
    def remover(self):
        _, no = heappop(self._nos)
        return no
       

    
        

  