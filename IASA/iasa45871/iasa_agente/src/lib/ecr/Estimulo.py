from abc import ABC, abstractmethod

#Estimulo - Ativa uma reacao
#Interface Estimulo - Interface que vai implementar o método detectar
#Este estimulo será depois usado como intensidade, para ser usado na resposta
class Estimulo:
    
    #Método que vai detetar um estimulo através da percepcao 
    @abstractmethod
    def detectar(self, percepcao):
        pass
