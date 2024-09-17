from abc import ABC, abstractmethod

#Interface Planeador - Serve para implementar os diferentes planeadores propostos
# -> O planeamento automático é um processo deliberativo que tem por objectivo gerar 
# sequências de acção, designadas planos, para concretização de objectivos pré-definidos

class Planeador:
    
    #Método abstrato (explicado nas classes onde é utilizado)
    @abstractmethod
    def planear(self, modelo_plan, objectivos):
        pass