from lib.ecr.ComportComp import ComportComp

#Os comportamentos estão definidos numa hierarquia onde existem prioridades.
class Prioridade(ComportComp):

    #O método selecionar_accao vai escolher uma acção da lista  
    #Caso não seja nula, vai retornar a accao, consoante a sua prioridade
    #Vai utilizar key=lambda para criar uma inline function em que o objetivo é retornar de dentro da lista de accoes
    #aquela que seja de maior prioridade
    def seleccionar_accao (self, accoes):
        if accoes:
           return max(accoes, key=lambda accao: accao.prioridade)
               
