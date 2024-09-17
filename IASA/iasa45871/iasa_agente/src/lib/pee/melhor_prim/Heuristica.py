from abc import ABC, abstractmethod

#Interface que implementa o método activar
#Esta classe recebe os comportamentos da ComportComp
class Heuristica:
    
    #Método abstrato (explicado nas classes onde é utilizado)
    @abstractmethod
    def h(self, estado):
        pass

