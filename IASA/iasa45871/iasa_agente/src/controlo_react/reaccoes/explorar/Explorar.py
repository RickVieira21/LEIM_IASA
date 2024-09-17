from controlo_react.reaccoes.resposta.RespostaMover import RespostaMover
from lib.ecr.Comportamento import Comportamento
from random import choice
from lib.sae.ambiente.direccao import Direccao


#Explorar - O agente vai vaguear pelo espaço à procura de alvos para recolher.
#Vai escolher uma direção para que o RespostaMover faça o agente vaguear.
class Explorar(Comportamento):

#Método activar:
#Escolhe uma direcao aleatoria dentro do enum Direcao (de sae) atraves do choice
#Chama uma RespostaMover que recebe essa direcao
#Retorna essa resposta (que é uma accao)

    def activar(self, percepcao): #NESTE CASO, a direccao escolhida é RANDOM, logo não é necessária a percepcao
        direccao = choice(list(Direccao))
        resposta = RespostaMover(direccao)
        return resposta.activar(percepcao)
