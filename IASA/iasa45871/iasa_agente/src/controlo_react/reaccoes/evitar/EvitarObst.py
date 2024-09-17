from controlo_react.reaccoes.evitar.EvitarDir import EvitarDir
from controlo_react.reaccoes.evitar.resposta.RespostaEvitar import RespostaEvitar
from lib.ecr.Hierarquia import Hierarquia
from lib.sae.ambiente.direccao import Direccao

#Vai ter apenas uma instancia da RespostaEvitar
#Todas as instancias partilham a mesma resposta, e tem direcoes diferentes
#Chama o construtor da classe super e da lhe o EvitarDir (com a RespostaEvitar a entrar como parametro) 
# para cada uma das direcoes existentes
class EvitarObst(Hierarquia):

    def __init__(self):
       self._resposta = RespostaEvitar()
       super().__init__([EvitarDir(direccao, self._resposta) for direccao in Direccao])