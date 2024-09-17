from abc import ABC, abstractmethod
from lib.ecr.Comportamento import Comportamento

#Classe ComportComp - Esta classe contém a lista de comportamentos e de accoes
#Tem como objetivo ativar um comportamento da lista, que depende da perceção, caso existam acções.

class ComportComp(Comportamento):

    def __init__(self, comportamentos):
        self._comportamentos = comportamentos

    #Método que vai correr a lista de comportamentos:
    # - Se houver accoes, adiciona essa accao à lista de accoes e ativa o comportamento com base na percepcao recebida.
    # - Por fim retorna a accao selecionada 
    # - Caso contrário, não faz nada.
    def activar(self, percepcao):
        accoes = []
        for comportamento in self._comportamentos:
            accao = comportamento.activar(percepcao)
            if accao:
               accoes.append(accao)
        if accoes:
            return self.seleccionar_accao(accoes)       
             

    #Método abstrato - Servirá para escolher a acção a tomar nas classes Prioridade e Hierarquia
    @abstractmethod
    def seleccionar_accao (self, accoes):
       pass