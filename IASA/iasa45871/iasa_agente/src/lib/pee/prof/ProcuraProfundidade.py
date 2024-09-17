from lib.pee.mec_proc.MecanismoProcura import MecanismoProcura
from lib.pee.mec_proc.fronteira.FronteiraLIFO import FronteiraLIFO

# A procura em profundidade utiliza a FronteiraLIFO
#-> A procura em profundidade pode não possuir solução
class ProcuraProfundidade(MecanismoProcura):
    
    #Chama o construtor da FronteiraLIFO
    def __init__(self):
     super().__init__(FronteiraLIFO())

    #Guarda na fronteira e nos explorados se existir
    def _memorizar(self, no):
       self._fronteira.inserir(no)