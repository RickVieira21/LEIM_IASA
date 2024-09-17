from abc import ABC, abstractmethod

#Interface ModeloPDM - Implementa os métodos que fornecem a estrutura básica para representar um modelo PDM -
# Como informações sobre os estados, ações, transições e recompensas do modelo/ambiente em que opera. 
class ModeloPDM(ABC):
    
    # S - Conjunto de estados do mundo
    @abstractmethod
    def S(self):
        pass

    # A - Conjunto de ações possíveis para um determinado estado s
    @abstractmethod
    def A(self, s):
        pass

    # T - Probabilidade de transição de um estado para outro através de determinada ação
    @abstractmethod
    def T(self, s, a):
        pass

    # R - Recompensa esperada pela transição entre estados s e sn através de determinada ação a
    @abstractmethod
    def R(self, s, a, sn):
        pass







