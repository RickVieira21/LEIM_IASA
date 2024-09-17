from blocos.ProblemaBlocos import ProblemaBlocos
from lib.pee.melhor_prim.ProcuraCustoUnif import ProcuraCustoUnif

# Classe PlaneadorBLC - Vai criar um problema para o planeador de blocos
# Depois chama o Mecanismo de Procura, para ser usado o seu método procurar (que recebe o problema) e retorna a solucao

class PlaneadorBLC:
    def planear(self, accoes, loc_inicial, loc_final):
        estado_inicial = loc_inicial
        operadores = accoes
        problema = ProblemaBlocos(estado_inicial, operadores)
        mec_proc = ProcuraCustoUnif()
        solucao = mec_proc.procurar(problema)
        return solucao

        
    