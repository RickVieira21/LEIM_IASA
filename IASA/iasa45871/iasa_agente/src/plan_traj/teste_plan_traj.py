from plan_traj.planeador.Ligacao import Ligacao
from plan_traj.planeador.PlaneadorTrajecto import PlaneadorTrajecto
from plan_traj.apresent.Vista_Trajecto import Vista_Trajecto


# ESTADO - Define situação

# OPERADOR - Define transformação (transição de estado), à qual associamos um custo

# PROBLEMA - Estado inicial, Objetivo, Operadores

# SOLUÇÃO - Percurso (plano de accão)

# Classe para realizar os testes através da tabela/gráfico nos slides.
class teste_plan_traj():
    
    def main():

    #Tabela

        LIGACOES = [Ligacao("Loc-0", "Loc-1", 5),
            Ligacao("Loc-0", "Loc-2", 25),
            Ligacao("Loc-0", "Loc-7", 7),
            Ligacao("Loc-1", "Loc-3", 12),
            Ligacao("Loc-1", "Loc-6", 5),
            Ligacao("Loc-2", "Loc-4", 30),
            Ligacao("Loc-2", "Loc-7", 5),
            Ligacao("Loc-2", "Loc-8", 15),
            Ligacao("Loc-3", "Loc-2", 10),
            Ligacao("Loc-3", "Loc-5", 5),
            Ligacao("Loc-4", "Loc-3", 2),
            Ligacao("Loc-5", "Loc-4", 10),
            Ligacao("Loc-5", "Loc-6", 8),
            Ligacao("Loc-5", "Loc-9", 1),
            Ligacao("Loc-6", "Loc-3", 15),
            Ligacao("Loc-7", "Loc-8", 8),
            Ligacao("Loc-8", "Loc-4", 25),
            Ligacao("Loc-9", "Loc-6", 2),
            Ligacao("Loc-9", "Loc-10", 2),
            Ligacao("Loc-10", "Loc-4", 2)]

        LOC_INICIAL = "Loc-0"
        LOC_FINAL = "Loc-4"


        Solucao = PlaneadorTrajecto().planear(LIGACOES, LOC_INICIAL, LOC_FINAL)
        Vista_Trajecto().mostrar(Solucao)

    if __name__ == "__main__":
         main()

