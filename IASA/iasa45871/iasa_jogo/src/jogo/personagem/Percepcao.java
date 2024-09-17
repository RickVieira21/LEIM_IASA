package jogo.personagem;

import jogo.ambiente.*;

/**
 * Classe Percepcao - A Percepcao vai ser responsável por detetar o evento que está acontecer, para que depois na classe Controlo seja
 * tomada a melhor acção para cada um dos eventos percepcionados.
 */
public class Percepcao {
	
	public Evento evento;

	/**
	 * Construtor da Percepcao
	 * @param evento
	 */
	public Percepcao (Evento evento) {
		this.evento=evento;
	}
	
	/**
	 * Retorna o evento
	 * @return evento
	 */
	public Evento getEvento() {
		return evento;
	}
}
