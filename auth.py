from datetime import datetime

class Auth:
    
    # Metodo de cadastro de novo usuário
    def register(username, password, dir):

        parent_path = "C:/users" # Definindo a variavel do parent_path
        
        # Verificando se existe um usuário com mesmo username no sistema
        if dir.find_node("user_"+username, parent_path):
            
            # Retorno caso a condicao seja satisfeita
            print("Este username ja esta cadastrado no sistema. [" +  datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]")
            return False

        # Criando um novo usuário
        dir.add_node(node_name= "user_" + username, parent_path= parent_path, password=password)
        
        # Retorno apos a criacao do usuario
        print("Usuario registrado com sucesso. [" +  datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]")
        return True

    # Metodo de login de usuário
    def login(username, password,dir):

        # Definindo a variavel do parent_path
        parent_path = "C:/users"

        # Verificando se usuário existe no sistema e se a senha está correta
        user = dir.find_node("user_"+username, parent_path)

        # Verificando se o usuario existe no sistema
        if user:
            
            # Verificando se a senha recebida eh igual a senha armazenada no usuario
            if password == user.password:
                
                # Retorno caso a considacao seja satisfeita
                print("Logado com sucesso. [" +  datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]")
                return user
        
        # Retorno caso o algo esteja errado
        print("Username ou senha incorreto(os). [" +  datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]")    
        return None
