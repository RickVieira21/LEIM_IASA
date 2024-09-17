from lib.plan.Planeador import Planeador
from lib.pdm.PDM import PDM
from lib.plan.plan_pdm.PlanoPDM import PlanoPDM
from lib.plan.plan_pdm.modelo.ModeloPDMPlan import ModeloPDMPlan


# Classe PlaneadorPDM - PlaneadorPDM é responsável por realizar o planeamento utilizando um PDM. 
# Define os valores de gama e delta_max.
# Através do método planear realiza o planeamento e obtém um plano resultante com a utilidade e a política de ação.
class PlaneadorPDM(Planeador):

    # Importante: gama deve variar entre 0.85 e 0.95
    def __init__(self, gama = 0.85, delta_max = 1.0):
        self.__gama = gama
        self.__delta_max = delta_max
        
    
    # Método planear - o método planear cria uma instância de ModeloPDMPlan com o modelo_plan e os objectivos fornecidos. 
    # Depois instancia um PDM passando os diferentes parametros (modelo, gama, delta)
    # Através do método resolver do PDM, obtém a utilidade e a politica. 
    # Com essas informações, cria uma instância de PlanoPDM e retorna esse mesmo plano.
    def planear(self, modelo_plan, objectivos):
        modelo_pdm = ModeloPDMPlan(modelo_plan, objectivos)
        #print(modelo_pdm)
        pdm = PDM(modelo_pdm, self.__gama, self.__delta_max)
        utilidade, politica = pdm.resolver()
        plano_pdm = PlanoPDM(utilidade, politica)
        return plano_pdm
        
       

    @property
    def gama(self):
        return self.__gama

    @gama.setter
    def gama(self, value):
        self.__gama = value

    @property
    def delta_max(self):
        return self.__delta_max

    @delta_max.setter
    def delta_max(self, value):
        self.__delta_max = value