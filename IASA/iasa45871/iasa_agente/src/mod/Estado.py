from abc import abstractmethod

# -> É importante não guardar todos os estados em que já estivemos, por questões de memória

class Estado:
    
    #Define um determinado método com a semântica de propriedade.
    #É como se fosse um getter sem um setter (read only)
    @property  
    def estado_inicial(self):
     return self._estado.inicial


    #Método abstrato - Identificação do valor 
    #Gera uma identificação única (usa hash)
    @abstractmethod
    def id_valor(self):
     pass

    #Retorna uma identificação única para um objeto
    def __hash__(self):
     return self.id_valor()

    #Os objetos são iguais se os seus dados internos forem iguais 
     # -> Não comparamos inteiros porque são objetos
    def __eq__(self, other):
     return  self.__hash__() == other.__hash__()