from exdeposito.PlaneadorDeposito import PlaneadorDeposito
    
#Teste Exercicio Deposito

# Resultados enunciado:

# Volume inicial: 0
# Volume final: 9
# Solucao : [Encher(2), Encher(2), Encher(2), Encher(3)]
# Dimensao : 5
# Custo : 21

def main():
    
    volume_inicial = 0
    volume_final = 9
    
    # A solucao vem de planear do PlaneadorDeposito tal como foi feito noutros casos
    solucao = PlaneadorDeposito().planear(volume_inicial, volume_final)

    # Mostra na consola os resultados finais 
    print("Solução: ", [no.operador for no in solucao if no.operador])
    print("Dimensão: ", solucao[-1].profundidade + 1)
    print("Custo: ", solucao[-1].custo)

if __name__ == "__main__":
    main()