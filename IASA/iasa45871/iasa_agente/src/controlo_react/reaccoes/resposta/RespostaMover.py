from lib.ecr.Resposta import Resposta
from lib.sae import Accao

# A RespostaMover é uma acção numa determinada direção (esta direção é dada por essa mesma acção)
# Para já é chamada na classe Explorar, onde lhe é atribuida uma direção random.
#Guarda a direccao e utiliza o super() para aceder ao construtor da classe Resposta
class RespostaMover(Resposta):
       
       def __init__(self , direccao):
        self._direccao = direccao
        super().__init__(Accao(self._direccao))
