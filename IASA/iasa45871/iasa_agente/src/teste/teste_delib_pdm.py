from lib.plan.plan_pdm.PlaneadorPDM import PlaneadorPDM
from lib.sae.simulador import Simulador
from controlo_delib.ControloDelib import ControloDelib


# TESTE PDM

controlo = ControloDelib(PlaneadorPDM())
Simulador(1, controlo).executar()