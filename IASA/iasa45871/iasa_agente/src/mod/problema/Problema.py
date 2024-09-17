from abc import ABC, abstractmethod

#Problema - Cada problema vai ter um estado inicial e operadores
# Vai implementar o método abstrato objetivo
class Problema(ABC):
    
    def __init__(self, estado_inicial, operadores):
        self._estado_inicial = estado_inicial
        self._operadores = operadores

    @abstractmethod
    def objetivo(self, estado):
        pass                      
        

    
        

  