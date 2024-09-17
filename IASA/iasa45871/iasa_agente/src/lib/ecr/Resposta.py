#Classe que vai ditar a resposta em relação ao estimulo/intensidade
#Chama o método activar, criado na interface Comportamento, que vai receber a intensidade como parametro. Este método define a prioridade 
#da resposta, que vai corresponder à intensidade, e retorna a respectiva acção.
class Resposta:

    # parameterized constructor
    def __init__(self, accao):
        self._accao = accao

    #A prioridade corresponde à intensidade
    #Retorna a accao, que corresponde à resposta em relação ao estimulo
    def activar(self, percepcao, intensidade=0):
        self._accao.prioridade = intensidade
        return self._accao
