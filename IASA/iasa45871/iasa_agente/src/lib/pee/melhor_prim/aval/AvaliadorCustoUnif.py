from lib.pee.mec_proc.fronteira.Avaliador import Avaliador

class AvaliadorCustoUnif(Avaliador):
    
    # Avaliador do Custo Uniforme -> Indica o custo do nó
    def prioridade(self, no):
        return no.custo

   
    