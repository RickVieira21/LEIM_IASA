
from lib.pee.melhor_prim.aval.AvaliadorAA import AvaliadorAA
from lib.pee.melhor_prim.ProcuraInformada import ProcuraInformada


# Procura A* - Tem como objetivo a minimização do custo global - como tal pode ser visto como a melhor procura
# - Utiliza a distância de Manhattan (semelhante à euclidiana com diferença nas diagonais)
# - Corresponde a retirar a seguinte restrição -> "Não é possível movimentar através de obstáculos" 

# Uma heuristica admissivel é consistente.
# No entanto, não é suficiente ser admissivel para ser consistente!

# Se a heuristica for consistente, é só escolher um nó, tal que >= g(n) + h(n)
# Resulta que eualquer nó selecionado para expansão está num percurso ótimo.
class ProcuraAA(ProcuraInformada):
    
    def __init__(self):
        super().__init__(AvaliadorAA()) 
        

   