from mod.Estado import Estado
from mod.problema.Problema import Problema


# Classe ProblemaPlan - Extende o problema, criando o problema para o modo delibrativo
# Continua a usar o método objetivo para saber se atingiu o objetivo.
# No construtor da classe, é recebido o modelo do plano (modelo_plan) e o estado final desejado (estado_final). 
# O estado final é armazenado para ser utilizado posteriormente na verificação do objetivo.
class ProblemaPlan(Problema):

    def __init__(self, modelo_plan, estado_final):
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())
        self.__estado_final = estado_final
    
    #Verifica se o estado recebido é o estado objetivo
    def objetivo(self, estado):
        if estado == self.__estado_final:
           return True
        return False

    
 
