from abc import ABC, abstractmethod

#Interface Comportamento - Implementa o método activar
#Cada Comportamento vai produzir uma resposta

class Comportamento:
    
    #Método abstrato (explicado nas classes onde é utilizado)
    @abstractmethod
    def activar(self, percepcao):
        pass