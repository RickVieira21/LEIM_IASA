from lib.sae import Controlo

#A percepcao do agente é feita com base num sistema reactivo
#Produz uma resposta a uma percepcao com base nesse sistema
class ControloReact(Controlo):
    
    def __init__(self, comportamento):
        self._comportamento = comportamento
        self.mostrar_per_dir = True

    #Método que vai ditar a accao em resposta à percepcao
    #Cria uma accao com base na percepcao através do método activar do Comportamento
    #Retorna a accao
    def processar (self, percepcao):
        accao = self._comportamento.activar(percepcao)
        return accao
