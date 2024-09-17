from controlo_react.reaccoes.Recolher import Recolher
from controlo_react.reaccoes.explorar.Explorar import Explorar
from controlo_react.ControloReact import ControloReact
from lib.sae.simulador import Simulador


# TESTE REACTIVO

comportamento = Recolher()
controlo = ControloReact(comportamento)

Simulador(1, controlo).executar()