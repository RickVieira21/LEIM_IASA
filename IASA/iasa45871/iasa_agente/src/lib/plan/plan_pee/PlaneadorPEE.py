from lib.plan.Planeador import Planeador
from lib.pee.melhor_prim.ProcuraAA import ProcuraAA
from lib.plan.plan_pee.mod_prob.ProblemaPlan import ProblemaPlan
from lib.plan.plan_pee.mod_prob.HeurDist import HeurDist
from lib.plan.plan_pee.PlanoPEE import PlanoPEE
from lib.plan.plan_pee.mod_prob.HeurManhattan import HeurManhattan
from lib.pee.melhor_prim.ProcuraSofrega import ProcuraSofrega


# Classe PlaneadorPEE - Vai realizar o plano, criando um problema para realizar a procura pretendida
# Realiza o planeamento utilizando a abordagem do Planeamento por Procura com Informação (AA/Sofrega). 
# Esta abordagem utiliza um algoritmo de busca informada para encontrar um plano que atinja os objetivos desejados.
# No construtor vamos escolher que tipo de ProcuraInformada queremos realizar, para que no planear seja utilizada.
class PlaneadorPEE(Planeador):

    # A ProcuraInformada deve ser uma das duas criadas (AA ou Sofrega), não deve instanciar uma ProcuraInformada.
    def __init__(self):
        self._solucao = None
        #self._mec_pee = ProcuraSofrega()
        self._mec_pee = ProcuraAA()
        
    # Método Extra - Usado para escolher a heuristica que vai usar (ex última aula)    
    # HeurDist - distância euclidiana
    # HeuManhattan - distância de Manhattan 
    def definir_heuristica(self, objectivos):
        estado_final = objectivos[0]
       # heuristica = HeurDist(estado_final)
        heuristica = HeurManhattan(estado_final)
        nome_heuristica = type(heuristica).__name__  #Mostra o nome da heuristica a ser usada 
        print("Heuristica:", nome_heuristica)
        return heuristica

    # Método planear - Para planear, vai chamar o método procurar() da procuraInformada (que é o do MecanismoProcura)
    # que vai receber um problema como parâmetro do tipo ProblemaPlan
    def planear(self, modelo_plan, objectivos):
        if objectivos:
            estado_final = objectivos[0]
            problema = ProblemaPlan(modelo_plan, estado_final)

            heuristica = self.definir_heuristica(objectivos)

            self._solucao = self._mec_pee.procurar(problema, heuristica)
            return PlanoPEE(self._solucao)
       
