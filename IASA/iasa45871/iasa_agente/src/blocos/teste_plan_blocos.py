from blocos.Accao import Accao
from plan_traj.planeador.PlaneadorTrajecto import PlaneadorTrajecto
from plan_traj.apresent.Vista_Trajecto import Vista_Trajecto
from blocos.PlaneadorBLC import PlaneadorBLC


# ESTADO - Define situação

# OPERADOR - Define transformação (transição de estado), à qual associamos um custo

# PROBLEMA - Estado inicial, Objetivo, Operadores

# SOLUÇÃO - Percurso (plano de accão)

class teste_plan_blocos():
    
    def main():

    #Tabela - Falta Planeador para realizar os testes

        ACCOES = [ Accao("Desempilhar", 1),
                   Accao("Desempilhar", 2),
                   Accao("Empilhar", 1),
                   Accao("Empilhar", 2)
        ]

        PILHA_ORIGEM =  [ [2, 3, 1] ,[] ,[]]
        PILHA_DESTINO = [ [1, 2, 3] ,[] ,[]]


        Solucao = PlaneadorBLC().planear(ACCOES, PILHA_ORIGEM, PILHA_DESTINO)
       # Vista_Trajecto().mostrar(Solucao)

    if __name__ == "__main__":
         main()

