from controlo_react.reaccoes.aproximar.estimulo.EstimuloAlvo import EstimuloAlvo
from controlo_react.reaccoes.resposta.RespostaMover import RespostaMover
from lib.ecr.Reacao import Reacao


# Classe AproximarDir - É uma reação que tem como objetivo movimentar o agente na direção especificada. 
# Utilizada em conjunto com a classe AproximarAlvo, que tem como objetivo aproximar o agente de um alvo, utilizando quatro instâncias de 
# AproximarDir - uma para cada direção possível (norte, sul, leste e oeste).
class AproximarDir(Reacao):

#Aqui, guarda a direcao desejada, e chama o construtor da classe pai Reacao, passando como argumentos uma instância de EstimuloAlvo
#e uma instância de RespostaMover com a direção desejada.
     def __init__(self, direccao):
            self._direccao = direccao
            super().__init__(EstimuloAlvo(self._direccao), RespostaMover(self._direccao))
            
        