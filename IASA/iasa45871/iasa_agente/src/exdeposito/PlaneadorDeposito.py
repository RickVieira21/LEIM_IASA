from exdeposito.ProblemaDeposito import ProblemaDeposito
from lib.pee.melhor_prim.ProcuraCustoUnif import ProcuraCustoUnif

# PlaneadorDeposito - Tal como os outros planeadores, cria o problema inicial
# Utiliza a Procura por custo uniforme para encontrar a solucao.
class PlaneadorDeposito():

    def planear(self, volume_inicial, volume_final):
        prob = ProblemaDeposito(volume_inicial, volume_final)
        solucao = ProcuraCustoUnif().procurar(prob)
        return solucao
