package maqest;


/**
 * Classe Transicao - Esta classe vai ter no seu construtor um estado sucessor e uma acção.
 * Na classe Estado vamos usar as transições para que, quando haja um evento, e para sabermos para que estado vamos passar, recorremos às
 * transições que associam um estado sucessor à acção realizada.
 * Nesta classe alé do construtor, apenas temos métodos de get, para o estado sucessor e para a acção.
 */
public class Transicao<EV,AC> {

    public AC accao;
    public Estado<EV, AC> estadoSucessor;
    
    /**
     * Construtor da Transicao 
     * @param estadoSucessor
     * @param accao
     */
    public Transicao(Estado<EV, AC> estadoSucessor, AC accao){
      this.estadoSucessor=estadoSucessor;
      this.accao=accao;
    }

    /**
     * Faz return do estadoSucessor
     * @return estadoSucessor
     */
    public Estado<EV, AC> getEstadoSucessor(){
     return estadoSucessor;
    }

    /**
     * Faz return da accao
     * @return accao
     */
    public AC getAccao(){
     return accao;
    }
}
