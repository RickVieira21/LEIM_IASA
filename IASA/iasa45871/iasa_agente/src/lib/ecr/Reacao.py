from lib.ecr.Comportamento import Comportamento

#Classe Reacao, recebe o comportamento como parametro 
# Conjunto Estimulo -> Resposta
#  A Reacao contém desde a detetação do estimulo, à activação da resposta
#  1- Detetar o estimulo
#  2- Atribuir a este uma intensidade
#  3- Caso haja estimulo, activa uma resposta para essa intensidade -> (accao)


class Reacao(Comportamento):

    # parameterized constructor
    def __init__(self, estimulo, resposta):
        self._estimulo = estimulo
        self._resposta = resposta

#Método activar - Derivado do Comportamento
#1 - Detectar o estimulo (se houver).
    # Verifica se há estimulo, através da percepcao.
    # Este valor passa a ser a intensidade.
#2 - Caso haja estimulo, vai chamar o activar da resposta.
    # Se a intensidade for maior que 0 há estimulo.
    # Retorna a accao, ou seja, a resposta ao estimulo.
    #Caso não haja, não faz nada
    def activar(self, percepcao):
        intensidade = self._estimulo.detectar(percepcao)
        if intensidade <= 0:
             return None
        if intensidade > 0:
              accao = self._resposta.activar(percepcao, intensidade)
        return accao
