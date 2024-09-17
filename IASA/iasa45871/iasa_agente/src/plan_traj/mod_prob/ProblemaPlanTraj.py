from mod.problema.Problema import Problema
from plan_traj.mod_prob.EstadoLocalidade import EstadoLocalidade
from plan_traj.mod_prob.OperadorLigacao import OperadorLigacao
from plan_traj.planeador.Ligacao import Ligacao

class ProblemaPlanTraj(Problema):

    def __init__(self, ligacoes, loc_inicial, loc_final):
        self._estado_final = EstadoLocalidade(loc_final)   
        self._ligacoes = ligacoes
        self._loc_inicial = loc_inicial
        self._loc_final = loc_final

        listaOperadores = []
        for ligacao in ligacoes:
            operador = OperadorLigacao(ligacao.origem, ligacao.destino, ligacao.custo)
            listaOperadores.append(operador)
        super().__init__(EstadoLocalidade(loc_inicial), listaOperadores)
    
    def objetivo(self, estado):
        return estado == self._estado_final

   
    