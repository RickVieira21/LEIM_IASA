from random import choice
from controlo_react.reaccoes.resposta.RespostaMover import RespostaMover
from lib.sae.ambiente.direccao import Direccao

class RespostaEvitar(RespostaMover):

#Recebe uma dir_inicial, que corresponde a direcao que vai tomar de inicio (Este)
#Cria uma lista de direccoes para ser usada nos outros metodos
 def __init__(self, dir_inicial = Direccao.ESTE): 
     super().__init__(dir_inicial)
     self._dir_inicial = dir_inicial
     self._direccoes = list(Direccao)
     

#Verifica se esta em contacto com um obstaculo
#Se estiver: Verifica se existem posições livres 
#Se existirem direccoes livres: Toma essa direccao e boolean contacto_obst passa a ser falso porque não tem um obstáculo na frente
#Se não tiver um obstáculo faz uma RespostaMover através do super().
 def activar (self, percepcao, intensidade):
     contacto_obst = percepcao.contacto_obst(self._accao.direccao)
     if contacto_obst:
         direccao_livre = self._direccao_livre(percepcao)
         if direccao_livre:
             self._accao.direccao = direccao_livre
             contacto_obst = False
     if not contacto_obst:
        return super().activar(percepcao,intensidade) 

#Cria dir_livres, que vai ser:
#Uma lista de direccoes para as direccoes em que nao ha contacto com obstaculos
 def _direccao_livre(self, percepcao):
        dir_livres = [direccao for direccao in Direccao if not percepcao.contacto_obst(direccao)]
        return choice(dir_livres)
 



