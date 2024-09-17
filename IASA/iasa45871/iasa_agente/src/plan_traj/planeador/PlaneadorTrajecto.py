from lib.pee.melhor_prim.aval.AvaliadorAA import AvaliadorAA
from lib.pee.larg.ProcuraLargura import ProcuraLargura
from lib.pee.mec_proc.MecanismoProcura import MecanismoProcura
from lib.pee.mec_proc.Solucao import Solucao
from lib.pee.melhor_prim.ProcuraAA import ProcuraAA
from lib.pee.melhor_prim.ProcuraCustoUnif import ProcuraCustoUnif
from lib.pee.melhor_prim.ProcuraMelhorPrim import ProcuraMelhorPrim
from lib.pee.prof.ProcuraProfundidade import ProcuraProfundidade
from lib.pee.melhor_prim.ProcuraSofrega import ProcuraSofrega
from lib.pee.melhor_prim.Heuristica import Heuristica
from lib.pee.prof.ProcuraProfLim import ProcuraProfLim
from lib.pee.prof.ProcuraProflter import ProcuraProflter
from plan_traj.mod_prob.ProblemaPlanTraj import ProblemaPlanTraj
from plan_traj.planeador.Ligacao import Ligacao


# Classe PlaneadorTrajeto - Vai criar um problema para o planeador de trajetos com os parâmetros recebidos
# Depois chama o Mecanismo de Procura, para ser usado o seu método procurar (que recebe o problema) e retorna a solucao
class PlaneadorTrajecto:
    
    def planear(self, ligacoes, loc_inicial, loc_final):
        problema = ProblemaPlanTraj(ligacoes, loc_inicial, loc_final)
        mec_proc = ProcuraProflter()   
        solucao = mec_proc.procurar(problema)   #Procuras Informadas (AA e Sofrega) precisam de uma heuristica 
        return solucao
        
    