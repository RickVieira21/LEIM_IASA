from lib.ecr.ComportComp import ComportComp

#Os comportamentos estão organizados numa hierarquia fixa 
#Dentro da hierarquia, há comportamentos com prioridade sobre os outros

class Hierarquia(ComportComp):

    #O método selecionar_accao vai receber a lista de accoes e vai realizar a primeira accao na lista
    def seleccionar_accao (self, accoes):
        return accoes[0]
