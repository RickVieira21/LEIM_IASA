from lib.pee.mec_proc.fronteira.Fronteira import Fronteira

#First in first out - Inserir no fim
class FronteiraFIFO(Fronteira):
    
    #Logo - > Faz append do nó para ficar no fim e chama os nós em memória
    def inserir(self, no):
        self._nos.append(no)
        super().nos_memoria()

    

   