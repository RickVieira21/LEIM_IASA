package maqest;


/**
 * Classe da Máquina de estados - A máquina de estados vai ser responsável por fazer o sistema mudar de estados consoante os eventos
 * recebidos, através de transições. As classes Estado e Transicao vão gerar os respectivos estados e transicoes e em conjunto com a máquina
 * de estados vão fazer o sistema avançar trabalhando em conjunto (método processar). 
 * 
 */
public class MaquinaEstados<EV, AC> {

    private Estado<EV, AC> estado;

    /**
     * Construtor da MaquinaEstados
     * EV - Tipo de Evento
     * AC - Tipo de Accao
     * @param estado
     */
    public MaquinaEstados(Estado<EV, AC> estado){
      this.estado=estado;
    }

    /**
     * Faz return do estado
     * @return estado
     */
    public Estado<EV, AC> getEstado(){
      return estado;
    }

    /**
     * Cria uma nova transicao através do método processar da classe Estado.
     * Se existir transicao, cria um objeto estado para receber o estado sucessor e faz return da accao para esse estado.
     * Caso contrário faz return null.
     * @param evento
     * @return accao
     */
    public AC processar(EV evento){
        Transicao<EV, AC> transicao = estado.processar(evento);
        if(transicao != null){
           estado = transicao.getEstadoSucessor();
           return transicao.getAccao(); 
        }
        
         return null;
    }
    
}
