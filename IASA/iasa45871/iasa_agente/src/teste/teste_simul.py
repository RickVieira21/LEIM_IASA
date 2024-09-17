from lib.sae import Simulador
from lib.sae import Controlo

class ControloTeste(Controlo):
    def processar(self,percepcao):
        pass

controlo = ControloTeste()
Simulador(1, controlo).executar()