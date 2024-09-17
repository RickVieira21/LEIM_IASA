from abc import ABC, abstractmethod

#Interface ModeloPlan 

class ModeloPlan(ABC):
    
    #Método abstrato (explicado nas classes onde é utilizado)
    @abstractmethod
    def obter_estado(self):
        pass

    #Método abstrato (explicado nas classes onde é utilizado)
    @abstractmethod
    def obter_estados(self):
        pass

    #Método abstrato (explicado nas classes onde é utilizado)
    @abstractmethod
    def obter_operadores(self):
        pass