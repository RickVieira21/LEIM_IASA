package maqest;

import java.util.HashMap;
import java.util.Map;

/**
 * Classe Estado - Cada estado terá um nome e um HashMap transicoes, que vai conter um tipo de evento e uma transicao.
 * Através das transições é possível sabermos para que estado vamos a partir das acções que ocorram como já foi visto na classe Transicao
 * Esta classe contém métodos para retornar uma transicao ou um estado, consoante a açção seja ou não nula.
 */
public class Estado<EV, AC> {

    private String nome;
    private Map<EV, Transicao<EV, AC>> transicoes;

    /**
     * Construtor do Estado
     * Cria o HashMap transicoes
     * @param nome
     */
    public Estado (String nome){
    this.nome=nome;
    transicoes = new HashMap<EV, Transicao<EV, AC>>();
    }

    /**
     * Faz return do nome do estado
     * @return nome
     */
    public String getNome() {
        return nome;
    }

    /**
     * Retorna o evento dentro do Hashmap transicoes
     * @param evento
     * @return evento 
     */
    public Transicao<EV, AC> processar(EV evento) {
        return transicoes.get(evento);
    }


    /**
     * Chama o método transicao para os eventos sem ação (null)
     * @param evento
     * @param estadoSucessor
     * @return o valor atual do objeto
     */
    public Estado<EV, AC> transicao(EV evento, Estado<EV, AC> estadoSucessor) {
        return transicao(evento, estadoSucessor, null);
    }


    /**
     * Coloca o evento (key) e a transicao (value) no Hashmap transicoes
     * @param evento
     * @param estadoSucessor
     * @param accao
     * @return o valor atual do objeto
     */
    public Estado<EV, AC> transicao(EV evento, Estado<EV, AC> estadoSucessor, AC accao) {
        transicoes.put(evento, new Transicao<EV, AC>(estadoSucessor, accao));
        return this;
    }

    //Override usado para converter o estado para string para que seja possível fazer print
    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return nome;
    }
}
