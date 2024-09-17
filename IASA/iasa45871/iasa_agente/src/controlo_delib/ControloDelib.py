from controlo_delib.MecDelib import MecDelib
from controlo_delib.modelo.ModeloMundo import ModeloMundo
from lib.plan.plan_pee.PlaneadorPEE import PlaneadorPEE
from lib.sae.agente.controlo import Controlo


# Classe ControlDelib - Extende controlo.
# O controlo delibrativo engloba: 
# - O modelo do mundo (memória, representação interna do agente), 
# - O mecanismo de delibração (pode incorporar vários mecanismos de delibração)
# - O planeador (O planeador depois escolhe um do mecanismos para utilizar)

class ControloDelib(Controlo):

    def __init__(self, planeador):
        self.__planeador = planeador
        self.__modelo_mundo = ModeloMundo()
        self.__mec_delib = MecDelib(self.__modelo_mundo)
        self._plano = None
        self._objectivos = None

# Processar:
# - 1. Observar o mundo, gerando percepções
# - 2. Actualizar o modelo do mundo, com base nas percepções
# - 3. Deliberar o que fazer, gerando um conjunto de objectivos
# - 4. Planear como fazer, gerando um plano de acção
# - 5. Executar o plano de acção
    def processar(self, percepcao):
                 self.__assimilar(percepcao)
                 if self.__reconsiderar():
                    self.__deliberar()
                    self.__planear()
                   # print("num objetivos: ", len(self._objectivos))
                 self.__mostrar()
                 return self.__executar()  
                     

    #Recebe uma percepcao e actualiza usando a percepcao
    def __assimilar(self, percepcao):
        self.__modelo_mundo.actualizar(percepcao)
         
    # Temos de reconsiderar quando:
    # Não há plano (plano vazio)
    # ou havia plano mas o modelo do mundo mudou
    def __reconsiderar(self):
        if self._plano is None or self.__modelo_mundo.alterado:
           return True
        return False

    #Chama o delibrar do Mecanismo Delibração que:            
    # - Ordenar através do sort a lista de objetivos
    # - Escolher aquele com a menor distância
    def __deliberar(self):
        self._objectivos = self.__mec_delib.deliberar()
        #self.__mec_delib.deliberar()
        #print(len(self._objectivos)) #31 objetivos inicialmente
    
    # Cria um plano só se houver objetivos
    # O plano é criado através do Planeador
    def __planear(self):
        if self._objectivos:
           self._plano = self.__planeador.planear(self.__modelo_mundo, self._objectivos)
       
   
    # Vai obter a accao através do método obter_accao do PlanoPEE
    # Se houver operador, retornamos a accao desse operador
    def __executar(self): 
        operador = self._plano.obter_accao(self.__modelo_mundo.obter_estado())
        if operador:
            return operador.accao

    #Mostrar plano, objetivos e estados para que seja possível observar ao testar
    def __mostrar(self):
        self.vista.limpar()
        self.__modelo_mundo.mostrar(self.vista)
        if self._plano:
           self._plano.mostrar(self.vista)
        if self._objectivos:
           self.vista.mostrar_estados(self._objectivos)