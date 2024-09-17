from lib.pee.mec_proc.MecanismoProcura import MecanismoProcura

# -> Cada espaço de estados pode ser considerado um grafo
# -> Tem os vários nós, e cada arco (que no fundo é uma transição)

class ProcuraGrafo(MecanismoProcura):
    
    def _iniciar_memoria(self):
     super()._iniciar_memoria()
     self._explorados = {}

    #Tem de saber se quer ou não manter o nó
    #Se for para manter - adiciona aos explorados para esse estado
    #Também inserir na fronteira 
    def _memorizar(self, no):
        estado = no._estado
        if self._manter(no):
           self._explorados[estado] = no
           self._fronteira.inserir(no)


    #Se não existir nos nós explorado, mantém o nó 
    def _manter(self, no):
     return no._estado not in self._explorados
    
    
    #Redefine o método para calcular o número máx de nós em memória para a ProcuraGrafo
    # -> Nesta procura os nós em memória correspondem ao total de nós explorados
    def nos_memoria(self):
        return len(self._explorados)


   