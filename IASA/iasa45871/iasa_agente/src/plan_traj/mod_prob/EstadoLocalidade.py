from mod.Estado import Estado

# Classe EstadoLocalidade - Vai extender o estado para testar este exemplo especifico, utilizando a localidade recebida
class EstadoLocalidade(Estado):

    def __init__(self, localidade):
        self._localidade = localidade

    @property  
    def localidade(self):
        return self._localidade
    
    def id_valor(self):
        return self._localidade.__hash__()
    
    #Reproduz na consola a localidade
    def __repr__(self):
        return str(self._localidade)
    