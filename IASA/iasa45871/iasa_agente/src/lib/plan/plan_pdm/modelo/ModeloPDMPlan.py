from lib.pdm.modeloPDM.ModeloPDM import ModeloPDM


# Classe ModeloPDMPlan - Classe que implementa a interface ModeloPlan e serve para que o planeador utilize os métodos definidos 
# na interface ModeloPDM para obter informações sobre o modelo e realizar o planeamento.
class ModeloPDMPlan(ModeloPDM):

    #rmax -> Valor máximo de recompensa
    def __init__(self, modelo_plan, objectivos, rmax = 1000.0):
        self.__modelo_plan = modelo_plan
        self.__objectivos = objectivos
        self.__rmax = rmax
     #   self.__transicoes = {}
     #    for s in self.obter_estados():
     #       for a in self.obter_operadores():
     #           if sl := a.aplicar(s):
     #               self.__transicoes[(s,a)] = sl

    
    # ----- ModeloPlan ------ #

    def obter_estado(self):
        return self.__modelo_plan.obter_estado()
    
    def obter_estados(self):
        return self.__modelo_plan.obter_estados()
    
    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()
    
    
    # ----- ModeloPDM------ #

    # S - Lista de estados
    def S(self):
        return self.obter_estados()


    # A - Lista de ações possíveis para o estado s. 
    # Verifica se o estado s é um objetivo e, se for, retorna uma lista vazia, indicando que não é necessária qualquer ação para alcançar o objetivo. 
    # Caso contrário, itera sobre os operadores disponíveis e adiciona à lista de ações aquelas que podem ser aplicadas ao estado s.
    def A(self, s):
        Accoes = []
        if s in self.__objectivos:
            return Accoes  
        for operador in self.obter_operadores():
            if operador.aplicar(s):
                Accoes.append(operador)
        return Accoes  


    # T - Probabilidade das transições de estado através de uma ação a partir de um estado s. 
    # Utiliza o método aplicar() do operador a para obter o próximo estado resultante da aplicação da ação.
    def T(self, s, a):
        sn = a.aplicar(s)
        if sn:
            return [(1, sn)]
        return []
    

       #Forma de resolver eficaz de resolver - Requer alterações no construtor e no util_accao (Mec_util)

       # sn = self.__transicoes.get((s,a))
       # return 1 if sn is not None else 0
        
    

    # R - Recompensa associada à transição de s para sn após a aplicação da ação a. 
    # Verifica se a ação a possui um custo definido e, se tiver, retorna o custo. 
    # Caso contrário, verifica se o estado sn é um objetivo. 
    # Se for, retorna a recompensa máxima (rmax) menos o custo. Caso contrário, retorna None
    def R(self, s, a, sn):
        custo = a.custo(s, sn)
        if custo is not None:
            if sn in self.__objectivos:
                return self.__rmax - custo
            else:
                return custo  
        return None
        

    
    @property
    def rmax(self):
        return self.__rmax

    @rmax.setter
    def rmax(self, value):
        self.__rmax = value

    @property
    def objectivos(self):
        return self.__objectivos

    @objectivos.setter
    def objectivos(self, value):
        self.__objectivos = value