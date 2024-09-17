from lib.plan.Plano import Plano
from lib.pee.mec_proc.Solucao import Solucao


# Classe PlanoPEE - representa um plano resultante do processo de planeamento utilizando Procura informada. 
# O plano é gerado a partir de uma solução encontrada pela procura informada.
class PlanoPEE(Plano):

    def __init__(self, solucao):
        self.__solucao = solucao
    
    # Através do método obter_accao() vai retornar o operador a utilizar.
    # Se for o primeiro temos de remover (porque é sempre None) 
    def obter_accao(self, estado): 
        if self.__solucao.dimensao > 1:
           if estado == self.__solucao[0].estado:
              operador = self.__solucao[1].operador 
              self.__solucao.remover()
              return operador
    
    def mostrar(self,vista):
        vista.mostrar_solucao(self.__solucao) 
