from controlo_react.reaccoes.evitar.estimulo.EstimuloObst import EstimuloObst
from lib.sae.ambiente.elemento import Elemento

#Classe EstimuloAlvo - É um estimulo, recebe uma direccao e uma valor gama
#Guarda estes dois valores no construtor
class EstimuloAlvo(EstimuloObst):

    def __init__(self, direccao, gama=0.9):
        self._direccao = direccao
        self._gama = gama

#Recebe uma percepcao, vai ver se há um estimulo na percepcao, neste caso um alvo
#Vai ver a percepcao na direccao recebida para ver se há alvo nessa direccao (posição não interessa aqui)
#Se for um alvo: retorna a intensidade, gama ^ distância (+ distância, menor intensidade)
#Se não for um alvo: retorna 0
    def detectar(self, percepcao):
        elemento, distancia, _ = percepcao[self._direccao]
        if elemento == Elemento.ALVO:
            return self._gama ** distancia
        else:
            return 0
       
        
    
