package jogo.personagem;

import jogo.ambiente.*;

public class Personagem {
	
	public Ambiente ambiente;
	public Evento evento;
	Controlo controlo = new Controlo();
	
	/**
	 * Construtor da Personagem
	 * @param ambiente
	 */
	public Personagem (Ambiente ambiente) {
		this.ambiente=ambiente;
	}
	
	/**
	 * Executa a Personagem.
	 * Cria objetos dos tipos Percepcao e Accao através do métodos percepcionar e processar do Controlo
	 * Chama o método atuar com o parametro accao
	 */
	public void executar() {
    Percepcao percepcao = percepcionar();
	Accao accao = controlo.processar(percepcao);
	actuar(accao);
	}
	
/**
 * Cria um evento e uma percepcao
 * @return percepcao
 */
	private Percepcao percepcionar() {
		Evento evento = ambiente.getEvento();
		Percepcao percepcao = new Percepcao(evento);
		return percepcao;
	}
	


	/**
	 * Faz print do valor da accao caso exista
	 * @param accao
	 */
	private void actuar(Accao accao) {
		if(accao != null){
			System.out.printf("Accao:%s\n ", accao);
		}
	}
	
}
