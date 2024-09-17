from mod.problema.Problema import Problema

class ProblemaBlocos(Problema):
    def __init__(self, estado_inicial, operadores):
        super().__init__(estado_inicial, operadores)

    # Ver se tem 1 2 3 na primeira pilha
    def objetivo(self, estado):
        primeira_pilha = estado.pilhas[0]  # Primeira pilha do estado
        return primeira_pilha == [1, 2, 3]
        
