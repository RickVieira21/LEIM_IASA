package jogo;

import jogo.ambiente.*;
import jogo.personagem.*;

/**
	 * Classe Jogo - Esta é a classe principal, que contém a função main, e vai instanciar e criar uma personagem e um ambiente, que depois
	 * no método executar() vão ser chamados para que o jogo funcione.
	 */
public class Jogo {

	private static Ambiente ambiente;
	private static Personagem personagem;


	/**
	 * Função Main - Executa o jogo criando um novo ambiente e uma nova personagem (que recebe esse ambiente).
	 * @param args
	 */
	public static void main(String[] args) {
		ambiente = new Ambiente();
		personagem = new Personagem(ambiente);
		executar();
	}

	/**
	 * Executa o jogo - vai chamar as funções necessárias para executar o jogo, são elas o executar() da personagem, o evoluir() do ambiente.
	 * Vai continuar a chamar estes métodos até que o evento recebido seja Terminar.
	 */
	private static void executar() {

		do {
			personagem.executar();
			ambiente.evoluir();
		} while(ambiente.getEvento() != Evento.TERMINAR);

	}

}