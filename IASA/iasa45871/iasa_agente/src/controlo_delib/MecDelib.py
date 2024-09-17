from controlo_delib.modelo.ModeloMundo import ModeloMundo
from lib.sae import Elemento


# Classe MecDelib - Responsável por realizar o mecanismo de deliberação no contexto deliberativo. 
# Este mecanismo é responsável por selecionar os objetivos a serem alcançados com base nas informações disponíveis no modelo do mundo.
class MecDelib:

    def __init__(self, modelo_mundo):
        self._modelo_mundo = modelo_mundo


    # Delibrar realiza o processo de deliberação:
    # Primeiro obtém os estados através do modelo mundo.
    # Depois cria uma lista com todos os objetivos (alvos) e percorre os estados
    # Se o elemento para um determinado estado for um alvo, então adicionamos esse estado à lista de objetivos
    # Ordena a lista de objetivos com base no critério da distância e por fim retorna essa lista
    def deliberar(self):
        estados = self._modelo_mundo.obter_estados()
        objetivos = []
        for estado in estados:
            if self._modelo_mundo.obter_elemento(estado) == Elemento.ALVO:
                objetivos.append(estado)
        objetivos.sort(key=lambda estado: self._modelo_mundo.distancia(estado))
        #print(len(estados)) #para testar
        #print("jetivos: ", len(objetivos))
        return objetivos
        