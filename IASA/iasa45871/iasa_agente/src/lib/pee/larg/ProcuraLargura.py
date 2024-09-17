from lib.pee.mec_proc.ProcuraGrafo import ProcuraGrafo
from lib.pee.mec_proc.fronteira.FronteiraFIFO import FronteiraFIFO

# A procura em largura utiliza a FronteiraFIFO 
class ProcuraLargura(ProcuraGrafo):

    #Chama o construtor da FronteiraFIFO
    def __init__(self):
     super().__init__(FronteiraFIFO())
    




   