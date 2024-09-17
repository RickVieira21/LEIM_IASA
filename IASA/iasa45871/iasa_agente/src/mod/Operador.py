from abc import ABC, abstractmethod

from mod.Estado import Estado

#Interface Operador - Vai criar os métodos abstratos aplicar e custo
class Operador(Estado):
     
    @abstractmethod
    def aplicar(self, estado):
        pass

    @abstractmethod
    def custo(self, estado, estado_suc):
        pass                                 

    