from lib.pee.mec_proc.fronteira.Fronteira import Fronteira

#O ultimo a entrar é o 1o a sair -> Inserir de inicio
class FronteiraLIFO(Fronteira):
    
    #Logo - > Faz insert do nó na posição 0 e chama os nós em memória
    def inserir(self, no):
        self._nos.insert(0, no)
        super().nos_memoria()
        

    

   