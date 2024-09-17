from lib.plan.plan_pee.PlaneadorPEE import PlaneadorPEE
from lib.sae.simulador import Simulador
from controlo_delib.ControloDelib import ControloDelib


# TESTE DELIBRATIVO - Este teste suporta agora diferentes Heuristicas
# Para escolher a heuristica usada é só alterar o método definir_heuristica no PlaneadorPEE

controlo = ControloDelib(PlaneadorPEE())
Simulador(4, controlo).executar()



