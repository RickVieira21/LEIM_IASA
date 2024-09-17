from lib.pee.prof.ProcuraProfLim import ProcuraProfLim

# Proura em Profundidade Iterativa - Esta procura é bastante semelhante à procura em 
# largura, diferenciando-se desta principalmente em termos do uso de memória (usa menos).

# A procura em profundidade iterativa é uma variante da procura em profundidade que utiliza 
# uma abordagem iterativa com aumento gradual da profundidade máxima permitida.
# Realiza múltiplas iterações, aumentando progressivamente o limite de profundidade, até encontrar a solução ou esgotar todas as possibilidades.
class ProcuraProflter(ProcuraProfLim):
    
    # Para um limite de profundidade crescente, realiza procura com o limite actual
    # Se existe solução, retorna a solução
    # Utiliza a procura em profundidade limitada para fazer a procura
    def procurar(self, problema, inc_prof = 1, limite_prof = 100):
     result = None
     for prof_atual in range(0, limite_prof+1, inc_prof):
         super().__init__(prof_atual)
         result = super().procurar(problema)          
         if result != None:
            break
     return result


   