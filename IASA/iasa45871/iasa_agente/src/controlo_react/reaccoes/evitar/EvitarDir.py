from controlo_react.reaccoes.evitar.estimulo.EstimuloObst import EstimuloObst
from controlo_react.reaccoes.evitar.resposta.RespostaEvitar import RespostaEvitar
from lib.ecr.Reacao import Reacao


#Classe EvitarDir - Subclasse de Reacao que associa um estímulo a uma resposta específica. O objetivo desta classe é permitir que o agente
#possa evitar obstáculos, definindo uma direção que evite a colisão e a respetiva resposta.
#O construtor recebe a direção e a resposta como argumentos e chama o construtor da superclasse Reacao usando o método super().
class EvitarDir(Reacao):

    def __init__(self, direccao, resposta):
        self._direccao = direccao
        self._resposta = resposta
        super().__init__(EstimuloObst(self._direccao), self._resposta)