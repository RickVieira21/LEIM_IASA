
# Classe No - Elemento constituinte da árvore de procura, mantendo informação sobre...
# • Estado, a que corresponde o nó
# • Operador, que gerou o estado a que corresponde o nó
# • Antecessor, nó antecessor na árvore de procura
# • Profundidade do nó, na árvore de procura
# • Custo do percurso correspondente ao nó
class No:

    _profundidade = 0
    _custo = 0
   
    #Precisamos de 2 construtores porque o nó raiz não tem antecessor

    def __init__(self, estado, operador = None, antecessor = None):
        self._estado = estado
        self._antecessor = antecessor #False
        self._operador = operador

        if antecessor and operador:         #Outros Nós
            self._profundidade = antecessor.profundidade + 1
            self._custo = antecessor.custo + operador.custo(antecessor.estado, self._estado)
        else:                  #Nó Raiz   
            self._profundidade = 0 
            self._custo = 0


    #Less than - Método de comparação entre os nós
    #Um nó é menor que outro nó se o seu custo for menor
    #Usado depois nos avaliadores para comparar os nós
    def __lt__(self, no):
        return self.custo < no.custo

    #Propriedades dos nós - Métodos "get"
    @property 
    def profundidade(self):
        return self._profundidade

    @property
    def custo(self):
        return self._custo  
    
    @property
    def antecessor(self):
        return self._antecessor 
    
    @property
    def operador(self):
        return self._operador 
    
    @property
    def estado(self):
        return self._estado 