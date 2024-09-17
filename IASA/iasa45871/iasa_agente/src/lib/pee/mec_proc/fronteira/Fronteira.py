from abc import ABC, abstractmethod


# Classe Fronteira:
# - Permite inserir e remover nós de forma ordenada
# - Indica se a fronteira está vazia
#   NOTA: Um nó fica na fronteira enquanto não for expandido
class Fronteira(ABC):
    
    _nos_em_Memoria = 0

    #Construtor chama o método iniciar
    def __init__(self):
       self.iniciar()

    #Limpa a fronteira
    def iniciar(self):
       self._nos = []          
       self._vazia = True                               

    @abstractmethod
    def inserir(self, no):
     pass

    #Vai remover o primeiro nó na lista                      
    def remover(self):
     return self._nos.pop(0)
    
    # Método extra - NÃO ESTÁ NA ARQUITETURA/SLIDES
    # Conta o número máximo de nós mantidos em memória
    # O máximo em memória não conta os nós removidos! 
    # Verifica a dimensão máxima da fronteira:
    # Se a dimensão da fronteira atual for maior que a dimensão anterior, guardamos a nova.
    def nos_memoria(self):
        if len(self._nos) > self._nos_em_Memoria:
           _nos_em_Memoria = len(self._nos)
           print("Máx. nós em memória: " + str(_nos_em_Memoria))


    #Propriedade Booleana - Indica se a fronteira está vazia
    # -> É vazia não tiver nenhum nó
    @property
    def vazia(self):
        if len(self._nos) > 0:
           self._vazia = False
        else:
           self._vazia = True
        return self._vazia