from lib.ecr.Estimulo import Estimulo


class EstimuloObst(Estimulo):

    def __init__(self, direccao, intensidade = 1.0):
        self._direccao = direccao
        self._intensidade = intensidade

#A receber uma percepcao, vai ver se há um estimulo na percepcao, neste caso um alvo
#Cria um tuplo com o elemento e a distância, (Posicao não interessa aqui)
#Se houver contacto com um obstaculo: retorna a intensidade
#Se não houver contacto com um obstaculo: retorna 0
    def detectar(self, percepcao):
        if percepcao.contacto_obst(self._direccao): 
            return self._intensidade
        else:
            return 0
    