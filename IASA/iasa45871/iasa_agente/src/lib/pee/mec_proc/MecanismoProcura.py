from abc import ABC, abstractmethod
from lib.pee.mec_proc.No import No
from lib.pee.mec_proc.Solucao import Solucao
from lib.pee.mec_proc.fronteira.Fronteira import Fronteira



# Classe MecanismoProcura:
#- Permite procurar uam solução para um problema
#- Utiliza uma fronteira de exploração para memorizar e gerir nós explorados

class MecanismoProcura():

    #totalProcessados = 0
    
    def __init__(self, fronteira):
        self._fronteira = fronteira
        self._nosProcessados = 0



    #Chama o iniciar da fronteira, que depois inicia a lista
    def _iniciar_memoria(self):                                                         
        self._fronteira.iniciar()


     #Método abstrato que vai memorizar os nós pelos quais já passou
    @abstractmethod
    def _memorizar(self, no):
        pass


    #Implementação - BREADTH-FIRST-SEARCH
    #Método que faz a procura, avançando para o próximo nó 
    #Vai returnar a solucao caso atinja o objetivo  
    def procurar(self, problema):   

        self._iniciar_memoria()
        no = No(problema._estado_inicial)
        self._memorizar(no)
        while not self._fronteira.vazia:
            no = self._fronteira.remover()
            self._nosProcessados += 1                            #NÓ PROCESSADO
            if problema.objetivo(no.estado):
                print("Complexidade Temporal: ", self.nosProcessados())
                return Solucao(no)
            else:
                for no_suc in self._expandir(problema, no):
                    self._memorizar(no_suc)
        return None

    #Expande o nó - Gera os vários nós sucessores em relação a esse nó
    #Obtém o estado succesor aplicando o operador
    #Se houver estado sucessor, faz yield do nó

    #O yield em vez de devolver uma lista com todos os nós lá dentro
    #"iteramos" sobre um nó de cada vez, e devolvemos esse nó
    def _expandir(self, problema , no):
        for operador in problema._operadores:
            estado_suc = operador.aplicar(no._estado)
            if estado_suc:
               yield No(estado_suc, operador, no)


    # Método extra - NÃO ESTÁ NA ARQUITETURA/SLIDES
    # Conta o número máximo de nós processados
    # Para contar os nós processados temos de fazer um contador sempre que processamos um nó
    # Dentro do método de procura, incrementamos o contador a cada nó processado
    def nosProcessados(self):
        return self._nosProcessados
    