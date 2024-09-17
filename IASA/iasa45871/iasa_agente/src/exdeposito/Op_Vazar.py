from exdeposito.EstadoDeposito import EstadoDeposito
from exdeposito.OperadorDeposito import OperadorDeposito

# Operador Vazar - Herda o OperadorDeposito para vazar o depósito
# Aplicar para vazar - Basta subtrair ao volume atual o volume que vazou
# __repr__ para mostrar aquilo que vazar
class Op_Vazar(OperadorDeposito):
    
    def aplicar(self, estado):
        novo_volume = estado.volume - self._volume
        if novo_volume < 0:
            novo_volume = 0
        return EstadoDeposito(novo_volume)
    
    # Método para mostrar na consola
    def __repr__(self):
        return "Vazar(%s)" % self._volume