from lib.pee.mec_proc.fronteira.Avaliador import Avaliador

#O avaliador da heuristica guarda a heuristica
class AvaliadorHeur(Avaliador):
    
    def definir_heuristica(self, heuristica):
        self._heuristica = heuristica 

   
    