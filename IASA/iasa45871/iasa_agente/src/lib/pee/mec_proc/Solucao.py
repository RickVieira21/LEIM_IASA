
 #Dimensão é a lenght do percurso - devolve dimensão da lista
#Classe Solução: 
# - É uma sequência de nós
# - Permite acesso indexado e iteração sobre o percurso
# - Permite remover o primeiro nó do percurso
class Solucao():
    
    #Inserir nós na lista percurso - Enquanto o nó tiver antecessor, insere no conjunto
    #Vai empurrando os outros nós para trás à medida que vai adicionando os novos
    #Desta forma a lista de nós fica do inicio para o fim
    def __init__(self, no_final):
     self.__percurso = []
     no = no_final #Nó temporário
     while no:
         self.__percurso.insert(0, no)
         no = no._antecessor

    #Remove a primeira posição da lista
    #Ao contrário do remover() de fronteira, tem de fazer verificação 
    def remover(self):
         if self.__percurso:
            return self.__percurso.pop(0)

    #Devolve um iterador sobre o percurso efetuado 
    def __iter__(self):
        return iter(self.__percurso)

    #Devolve um item 
    def __getitem__(self, index):
        return self.__percurso[index]


    @property
    def dimensao(self):
        return len(self.__percurso)
