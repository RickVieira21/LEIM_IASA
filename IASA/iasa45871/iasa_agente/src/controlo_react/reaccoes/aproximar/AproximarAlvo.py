from controlo_react.reaccoes.aproximar.AproximarDir import AproximarDir
from lib.ecr.Prioridade import Prioridade
from lib.sae.ambiente.direccao import Direccao

class AproximarAlvo(Prioridade):

#Construtor que chama a classe super com as várias instâncias do Aproximar
#O ciclo for atribui uma direccao a cada uma das instâncias da classe AproximarDir
#São 4 as instâncias: Norte, Sul, Este, Oeste
    def __init__(self):
        super().__init__([
            AproximarDir(direccao) for direccao in Direccao
        ])
    
