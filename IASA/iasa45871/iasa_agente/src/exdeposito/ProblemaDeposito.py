from exdeposito.EstadoDeposito import EstadoDeposito
from exdeposito.Op_Encher import Op_Encher
from exdeposito.Op_Vazar import Op_Vazar
from mod.problema.Problema import Problema


# Problema deposito - Cria o problema do deposito 
class ProblemaDeposito(Problema):
    def __init__(self, vol_inicial, vol_final):
        super().__init__(EstadoDeposito(vol_inicial),
                         [Op_Encher(2),
                          Op_Encher(3),
                          Op_Vazar(2),
                          Op_Vazar(3)])
        self._volume_final = vol_final

    # Atingiu o objectivo se o volume atual for igual à aquele que era esperado (volume final)
    def objetivo(self, estado):
        return estado.volume == self._volume_final
