from abc import abstractmethod
from mod.Operador import Operador

# OperadorDeposito - Classe base para realizar as operações de encher e vazar.
# Operadores encher e vazar vão herdar esta classe para realizarem o seu próprio aplicar
# O custo é calculado como a diferença entre os estados (neste caso com volumes) elevado ao quandrado
class OperadorDeposito(Operador):
    
    def __init__(self, volume):
        self._volume = volume
    
    @abstractmethod
    def aplicar(self, estado):
        pass
        
    def custo(self, estado, estado_suc):
        return (estado_suc.volume - estado.volume) ** 2

    # Mostrar na consola
    def __repr__(self):
        return f"{self._estado_origem} -> {self._estado_destino}"
