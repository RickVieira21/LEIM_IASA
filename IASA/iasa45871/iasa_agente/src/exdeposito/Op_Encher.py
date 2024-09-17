from exdeposito.EstadoDeposito import EstadoDeposito
from exdeposito.OperadorDeposito import OperadorDeposito

# Operador Encher - Herda o OperadorDeposito para encher o depósito
# Aplicar para encher - Basta somar o volume do estado ao volume adicionado
# __repr__ para mostrar aquilo que encheu
class Op_Encher(OperadorDeposito):
    
    def aplicar(self, estado):
        return EstadoDeposito(estado.volume + self._volume)
    
    # Método para mostrar na consola 
    def __repr__(self):
        return "Encher(%s)" % self._volume