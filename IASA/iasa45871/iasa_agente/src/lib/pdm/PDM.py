from lib.plan.Plano import Plano
from lib.pdm.MecUtil import MecUtil

# Classe PDM - O planeamento é baseado numa representação do problema sob a forma de um
# processo de decisão de Markov.
class PDM():

    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__mec_util = MecUtil(modelo, gama, delta_max)

    
    # Politica - O planeamento automático com base em processos de decisão de Markov produz como
    # resultado uma política de acção, a qual define para cada estado possível a respectiva acção a realizar 
    
    # Iteramos sobre todos os estados do modelo e para cada estado obtemos as acoes
    # (float('-inf')) é usado como valor inicial para a variável melhor_utilidade para garantir que qualquer utilidade calculada a partir das ações seja maior que o valor inicial.
    # Depois calculamos a utilidade através da classe mec_util
    # Por fim selecionamos a ação com a maior utilidade e a atribuímos ao estado correspondente na política.
    def politica(self, U): 
        politica = {}  # Dicionário para armazenar a política de ação
        for s in self.__modelo.S():
            accoes_possiveis = self.__modelo.A(s)
            if accoes_possiveis:
                melhor_acao = None
                melhor_utilidade = float('-inf')
                for acao in accoes_possiveis:
                    utilidade_acao = self.__mec_util.util_accao(s, acao, U)
                    if utilidade_acao > melhor_utilidade or melhor_acao is None:
                        melhor_utilidade = utilidade_acao
                        melhor_acao = acao
                politica[s] = melhor_acao
        return politica
    

    # Resolver - Calcula a utilidade e a politica ótima com base na utilidade 
    def resolver(self):
        u = self.__mec_util.utilidade()
        p = self.politica(u)
        return u, p

