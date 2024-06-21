# Implementação dos diretórios do sistema de arquivos

# Importando os métodos e bibliotecas necessários para o sistema
from anytree import Node
from datetime import datetime

# Definao da classe que comportara todos os metodos do sistema
class Directory:
    
    # Cosntrutor da classe que incializara o sistema de diretorios
    def __init__(self):
        self.root = Node('C:') # Criando o diretorio principal
        self.users = Node('users', parent= self.root) # Criando o diretorio de usuarios dentro do diretorio principal
    
    # Metodo para buscar o nó por toda a árvore
    def find_node(self,node_name, parent_path=None):
        
        current_node = self.root # Setando o No atual a ser analisado como o root
        
        # Verificando se o "parent_path" foi recebido
        if parent_path:
            
            # Verificando se o "parent_path" eh igual a "C:", para diminuir o processamento enviando diretamente o unico diretorio que eh filho de "C:", o "users"
            if parent_path == "C:":
                return self.users 
            else:
                path_parts = parent_path.strip('/').split('/') # Separando os nomes dos diretorios no path do pai recebido
                
                # Percorrendo os nomes dos diretorios do path do pai
                for part in path_parts:
                    found = False # Setando a variavel "found" (encontrado) como falsa
                    
                    # Percorrendo os descendentes de cada diretorio 
                    for descendant in current_node.descendants:
                        
                        # Verificando se o nome do descendente eh igual ao nome do diretorio
                        if descendant.name == part:
                            current_node = descendant # Se for igual, a variavel "current_node" (no atual) recebe ela e retorna ao looping ate enccontrar o no buscado
                            found = True
                            break
                
                # Verificando se, o final do looping, a variavel "found" (encontrado) ainda eh falsa
                if not found:
                    return None # Caso seja, significa que nao foi encontrado nenhum no

        # Procurando o nó pelo nome entre os descendentes do nó pai (ou root se não houver pai)
        for node in current_node.descendants:
            if node.name == node_name: # Se o no tiver o mesmo nome que o no buscado, o no foi encontrado
                return node

        # Caso o no nao seja encontrado
        return None

    # Metodo para adicionar um novo nó na árvore
    def add_node(self,node_name, parent_path, **kwargs): # '**kwargs' argumento que pode receber qualquer chave e qualquer valor (Serve para adicionar os atributos no nó)
        
        # Processando o path do pai para pegar os nome do no pai e o path do no pai
        parent_path = parent_path.rstrip('/\\') 
        parent_parent_path, parent_name =  parent_path.rsplit('/', 1) if '/' in parent_path else parent_path.rsplit('\\', 1)
        
        # Pesquisando pelo no pai na arvore
        parent_node = self.find_node(parent_name, parent_parent_path)
        if parent_node:
            
            # Verificando se ja existe um no filho do no pai com o mesmo nome do no que deseja criar
            for child in parent_node.children:
                
                # Verificando se cada no "child" tem o mesmo nome do no a ser criado
                if child.name == node_name:
                    print(f"Ja existe um '{node_name}' nesse diretorio. ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    return 0 # Status caso ja exista um no  com o mesmo nome no diretorio
            
            # Criando o novo no 
            Node(node_name, parent_node, **kwargs)
            return 1 # Status caso o no for criado com sucesso
        
        # Caso nenhuma das condicoes a cima seja realizada significa que o no pai nao foi encontrado
        else:
            print(f"Diretorio '{parent_path}' nao foi encontrado. [" +  datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]")
            return 2 # Status caso o no pai nao for encontrado

    # Metodo para remover um nó da árvore
    def remove_node(self,node_name, parent_path):

        # Processando o path do pai para pegar os nome do no pai e o path do no pai
        parent_path = parent_path.rstrip('/\\') 
        parent_parent_path, parent_name =  parent_path.rsplit('/', 1) if '/' in parent_path else parent_path.rsplit('\\', 1)
        
        # Pesquisando pelo no pai na arvore
        parent_node = self.find_node(parent_name, parent_parent_path)
        if parent_node:
            
            # Pegando o no buscado na arvore
            node = self.find_node(node_name, parent_path)            
            
            # Verificando se o no foi encontrado se o seu no pai tem o nome do no referido
            if node and node.parent == parent_node:
                
                # Removendo o No da arvore
                node.parent = None
                print(f"No removido de '{parent_path}'. [" +  datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]")
                return 1
            # Se o verificado for falso, indica que o no nao foi encontrao no diretorio recebido
            else:
                print(f"O no '{node_name}' nao foi enontrado no diretorio '{parent_path}'. [" +  datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]")
                return 0
        # Caso o no pai nao for encontrado
        else:
            print(f"O diretorio '{parent_path}' nao foi encontrado. [" +  datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]")
            return 2
