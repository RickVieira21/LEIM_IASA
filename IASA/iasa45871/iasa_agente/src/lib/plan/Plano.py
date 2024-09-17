from abc import ABC, abstractmethod

#Interface Plano - Interface usada para representar um plano, 
# que é uma sequência de ações a serem executadas para alcançar um objetivo.

# As classes que implementam a interface Plano devem fornecer as informações necessárias
# para obter a próxima ação do plano e para exibir o plano de forma adequada.

class Plano:
    
    #Método abstrato (explicado nas classes onde é utilizado)
    @abstractmethod
    def obter_accao(self, estado):
        pass

    #Método abstrato (explicado nas classes onde é utilizado)
    @abstractmethod
    def mostrar(self, vista):
        pass