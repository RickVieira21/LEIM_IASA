package jogo.personagem;

import maqest.Estado;
import maqest.MaquinaEstados;
import jogo.ambiente.*;


/**
 * Classe Controlo - Vai escolher qual a melhor acção a tomar para cada evento recebido.
 * No construtor da classe vamos definir todos os estados e todas as transições possíveis para cada uma dos estados.
 * Desta forma, ficamos com tudo pronto para que sempre que ocorra um evento inserido pelo utilizador, observando o estado atual, consigamos
 * alterar o nosso estado através de uma transição.
 * Por fim começamos a máquina de estados, por exemplo, no estado de "procura".
 */
public class Controlo {

	public Percepcao percepcao;
	private MaquinaEstados<Evento, Accao> maqEst;

	
/**
 * Contrutor da classe Controlo
 */
	 public Controlo() {
		 
		//Definir estados
		Estado<Evento,Accao> procura = new Estado<>("Procura");
		Estado<Evento,Accao> inspeccao = new Estado<>("Inspecção");
		Estado<Evento,Accao> observacao = new Estado<>("Observação");
		Estado<Evento,Accao> registo = new Estado<>("Registo");

	    //Definir trasicoes
	procura 
		.transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR)
		.transicao(Evento.RUIDO, inspeccao, Accao.APROXIMAR)
		.transicao(Evento.SILENCIO, procura, Accao.PROCURAR);

	inspeccao
		.transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR)
		.transicao(Evento.RUIDO, inspeccao, Accao.APROXIMAR)
		.transicao(Evento.SILENCIO, procura, Accao.PROCURAR);

	observacao
		.transicao(Evento.ANIMAL, registo, Accao.OBSERVAR)
		.transicao(Evento.FUGA, inspeccao);

	registo
		.transicao(Evento.ANIMAL, registo, Accao.FOTOGRAFAR)
		.transicao(Evento.FUGA, procura)
		.transicao(Evento.FOTOGRAFIA, procura);

		 maqEst = new MaquinaEstados<>(procura);
		 
	 }
	
	/**
	 * Método processar - Primeiramente vai criar uma acção que vai corresponder ao valor retornado pelo método processar da máquina de 
	 * estados, que poderá ser nula caso não exista transição.
	 * Depois mostra esse estado na consola e por fim retorna essa mesma acção.
	 * @param percepcao
	 */
	public Accao processar(Percepcao percepcao) {
		Accao accao = maqEst.processar(percepcao.getEvento());
		mostrar();
        return accao;
	}

	/**
	 * Mostra o estado na consola
	 */
	public void mostrar() {
		System.out.printf("Estado:%s\n ", maqEst.getEstado());
	}
	
}
