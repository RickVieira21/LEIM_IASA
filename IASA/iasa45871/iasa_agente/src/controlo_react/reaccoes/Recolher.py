#Recolher - Contém todos os comportamentos que o agente realiza - aproximação aos alvos, evitar obstáculos, e explorar.

from controlo_react.reaccoes.aproximar.AproximarAlvo import AproximarAlvo
from controlo_react.reaccoes.evitar.EvitarObst import EvitarObst
from controlo_react.reaccoes.explorar.Explorar import Explorar
from lib.ecr.Hierarquia import Hierarquia

class Recolher(Hierarquia):

#Invoca o construtor da super classe com a lista de comportamentos
 def __init__(self):
        super().__init__([
             AproximarAlvo(),
             EvitarObst(),
             Explorar()
        ])