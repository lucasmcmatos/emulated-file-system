# Implementacao da integracao principal do sistema

# Importando metodos e bibliotecas necessarios para o funcionamento do sistema
from menagement_diretory import Directory
from menagement_memory import MemoryManager
from interface_logged import Logged
from interface_login import Login

# Instanciando as variaveis necessarias
memoria = MemoryManager() # Iniciando a memoria e o seu gerenciador
diretorio = Directory() # Iniciando o diretorio e seu gerenciador
root = diretorio.root # Intenciando o root do diretorio

# Looping que roda o sistema por completo 
while True:
    
    # Iniciando a interface de login
    app = Login(diretorio,memoria)
    app.mainloop()

    # Entrando na interface logada caso o usuario esteja logado
    if app.user_logged_in:
        
        # Inciando a interface logada
        menager = Logged(app.dir,app.memory,app.username)
        menager.mainloop()
        print("Usuario esta logado.")
    
    else:
        break
        

