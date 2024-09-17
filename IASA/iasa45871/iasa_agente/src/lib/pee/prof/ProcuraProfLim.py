from lib.pee.prof.ProcuraProfundidade import ProcuraProfundidade 
 

# Procura em Profundidade Limitada - Limita a procura a uma profundidade máxima
class ProcuraProfLim(ProcuraProfundidade):

         
    # O construtor incializa o super da ProcuraProfundidade e
    # Guarda a prof_max 
    def __init__(self, prof_max = 100) :
     super().__init__()
     self._prof_max = prof_max
     
     
    # Expande nó se a sua profundidade for inferior à profundidade máxima da procura
    # Faz yield do expandir do super (que já fazia yield do nó)
    def _expandir(self, problema, no):    
        if no.profundidade < self._prof_max:
           yield from super()._expandir(problema, no)    


    # Memoriza nó se não corresponder a um ciclo
    # Utiliza o memorizar da ProcuraProfundidade
    def _memorizar(self, no):
        if self._ciclo(no) == False:
           super()._memorizar(no)
  
   
    # Verifica se nó corresponde a um ciclo no ramo
    # respectivo, para evitar a expansão de nós referentes a
    # estados já explorados (não evita ciclos em relação a
    # outros ramos)

    # Vai "andar para trás" percorrendo os nós antecessores até
    # encontrar outro nó no mesmo estado que o nó ou até que não haja mais
    # nós antecessores
    def _ciclo(self, no):
       noAntecessor = no.antecessor
       while noAntecessor:    
          if no.estado == noAntecessor.estado:
             return True
          noAntecessor = noAntecessor.antecessor
       return False
        

    #Profundidade Máxima da procura - Property e Setter
    @property
    def prof_max(self):
         return self._prof_max   

    @prof_max.setter
    def prof_max(self, valor):
         if valor < 100:
            self._prof_max = valor
    
   

   