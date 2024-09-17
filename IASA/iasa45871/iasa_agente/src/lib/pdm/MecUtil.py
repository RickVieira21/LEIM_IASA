
# Classe MecUtil: Realiza os cálculos para as utilidades em PDM.
# Recebe o estado e a ação como entrada e utiliza as informações do modelo do PDM para determinar a utilidade correspondente. 
class MecUtil():

    def __init__(self, modelo, gama, delta_max):
        self.__delta_max = delta_max
        self.__gama = gama
        self.__modelo = modelo


    # O raciocínio automático com base em processos de decisão de Markov envolve o cálculo da
    # função de utilidade (valor), que define o valor associado a cada estado do problema
    # A utilidade serve depois de suporte ao cálculo da política de acção.
    # (float('inf')) é usado para garantir a execução do ciclo while (pelo menos 1 vez) e realizar a iteração do processo de atualização das utilidades
    # até que a condição seja alcançada.
    
    #Cálculo da utilidade - slides
    def utilidade(self):
        U = {s: 0 for s in self.__modelo.S()}
        delta = float('inf')  # Inicializar com valor infinito positivo
        while delta > self.__delta_max:
            uA = U.copy()
            delta = 0
            for s in self.__modelo.S():
                acoes = self.__modelo.A(s)
                if acoes:
                    U[s] = max(self.util_accao(s, a, uA) for a in acoes)
                    delta = max(delta, abs(U[s] - uA[s]))
        return U


    #S – Conjunto de estados válidos
    #A(s) – Conjunto de operadores definidos
    #T(s,a,s’) – Modelo de dinâmica
    #R(s,a,s’) – Modelo de recompensa

    #∑ T(s,a,s')[R(s,a,s')+ yU[s']]
    def util_accao(self, s, a, U):
        util_accao =  sum(p * self.__modelo.R(s, a, sn) + self.__gama * U[sn] for p, sn in self.__modelo.T(s, a))
        return util_accao
    
        #T, R, suc = self.__modelo.T, self.__modelo.R, self.__modelo.suc
        #return sum(T(s,a,sn) * (R(s,a,sn)) + self.__gama * U[sn]) for sn in suc(s,a))


    @property
    def delta_max(self):
        return self.__delta_max

    @delta_max.setter
    def delta_max(self, value):
        self.__delta_max = value

    @property
    def gama(self):
        return self.__gama

    @gama.setter
    def gama(self, value):
        self.__gama = value