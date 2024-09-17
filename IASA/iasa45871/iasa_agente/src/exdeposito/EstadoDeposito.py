from mod.Estado import Estado

# EstadoDeposito  Contém os mesmos métodos mas desta vez aplicados ao volume
class EstadoDeposito(Estado):
    
    def __init__(self, volume):
        self._volume = volume
        
    def id_valor(self):
        return hash(self._volume)
    
    def __repr__(self):
        return str(self._volume)
    
    @property
    def volume(self):
        return self._volume