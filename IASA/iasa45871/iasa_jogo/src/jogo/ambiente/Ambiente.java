package jogo.ambiente;

import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;


/**
	 * Classe Ambiente - Esta classe é responsável por gerar/mostrar os eventos para que o jogo vá avançando.
	 * A classe conta com um Hashmap de eventos, criado no construtor, cuja key vai servir para o utilizador introduzir na consola o evento
	 * que pretender, e cujo value vai ser o evento correspondente.
	 */
public class Ambiente {

	public Ambiente ambiente;
	private Evento evento;
	private Scanner sc = new Scanner(System.in);
	private Map<String, Evento> eventos;

	/**
	 * Construtor do Ambiente - Vai criar um HashMap de eventos 
	 */
	public Ambiente () {
		eventos = new HashMap<>();
		eventos.put("s", Evento.SILENCIO);
		eventos.put("r", Evento.RUIDO);
		eventos.put("a", Evento.ANIMAL);
		eventos.put("f", Evento.FUGA);
		eventos.put("foto", Evento.FOTOGRAFIA);
		eventos.put("t", Evento.TERMINAR);


	}
	
	/**
	 * Faz return do evento
	 * @return evento
	 */
	public Evento getEvento() {
		return evento;
	}
	
	/**
	 * No método evoluir do ambiente, que é chamado no executar do jogo, vamos gerar um evento e mostrá-lo na consola.
	 */
	public void evoluir() {
		evento = gerarEvento();
		mostrar(); 
	}

	/**
	 * Método que vai gerar um novo evento inserido pelo utilizador (comando) que é lido pelo scanner
	 * @return do evento inserido
	 */
	private Evento gerarEvento() {
		System.out.print("Evento? ");
        String comando = sc.next();
		return eventos.get(comando);
	}
	
	/**
	 * Mostra o evento inserido na consola
	 */
	private void mostrar() {
		System.out.printf("Evento:%s\n ", evento);
		System.out.println();
	}
	
}
