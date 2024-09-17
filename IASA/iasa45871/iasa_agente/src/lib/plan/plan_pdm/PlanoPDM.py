from lib.plan.Plano import Plano
from lib.pee.mec_proc.Solucao import Solucao


# Classe PlanoPDM - Representa um plano para o Processo de Decisão de Markov (PDM)
# Utiliza a utilidade e a política de ação associadas a um plano resultante de um processo de planeamento baseado em PDM. 
# Fornece métodos para obter a ação de um estado e para mostrar o plano no simulador
class PlanoPDM(Plano):

    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade
        self.__politica = politica
       
    # Método obter_accao - Primeiro precisa de ver se há politica:
    # Se houver, retorna a politica para o estado dado como parametro, else None
    def obter_accao(self, estado): 
        if self.__politica:
           return self.__politica[estado]
        return None

    def mostrar(self, vista):
        if self.__politica:
                vista.mostrar_valor(self.__utilidade) 
                vista.mostrar_politica(self.__politica)

    @property
    def utilidade(self):
        return self.__utilidade

    @utilidade.setter
    def utilidade(self, value):
        self.__utilidade = value

    @property
    def politica(self):
        return self.__politica

    @politica.setter
    def politica(self, value):
        self.__politica = value