from mod.Operador import Operador
from plan_traj.mod_prob.EstadoLocalidade import EstadoLocalidade

# Classe que vai servir para criar o operador para este exemplo
# Vai extender o Operador e completar os seus métodos utilizando agora as localizações dadas.

class OperadorLigacao(Operador):

    def __init__(self, origem, destino, custo):
        self._estado_origem = EstadoLocalidade(origem)
        self._estado_destino = EstadoLocalidade(destino)
        self.__custo = custo
    
    def aplicar(self, estado):
        if estado == self._estado_origem:
           return self._estado_destino  
    
    def custo(self, estado, estado_suc):
        if estado == self._estado_origem and estado_suc == self._estado_destino:
           return self.__custo
    
    #Método para reproduzir na consola a transição do estado origem para o estado destino
    def __repr__(self):
        return f"{self._estado_origem._localidade} -> {self._estado_destino._localidade}"

