# Codigo python que realiza as manipulacoes necessarias apra as interfaces apos usuario realizar login

# Importacao das bibliotecas necessarias 
import os
from tkinter import messagebox
import math
from anytree import Node, RenderTree

# Metodo que lista os arquivos do de um diretorio especifico 
def list_files(dir, path):
    
    parent_path, node_name =  path.rsplit('/', 1) if '/' in path else parent_path.rsplit('\\', 1) # Separando o path do pai e o nome do pai 
    children = dir.find_node(node_name, parent_path).children # Intanciando os filho do no pai encontrado
    return children

# Metodo que criar um arquivo
def create_file(self):
    
    # Intanciando as informacoes do arquivo e do sistema
    file_name = self.crtf.filename.get()
    file_text = self.crtf.text.get("1.0", "end-1c")
    file_allocation = self.crtf.radio_var.get()
    current_dir = self.current_dir
    dir = self.dir
    memory = self.memory
    
    
    # Verficando se existe informacao faltante
    if file_name=="" or file_text=="":
        messagebox.showerror("Criar arquivo","Preencha todos os campos")
    else:
        
        # Calculando o tamanho do arquivo (1 bloco cabe 10 caracteres)
        size = math.ceil(len(file_text) / 10)
        
        # Defindo o tipo de alocacao
        if file_allocation==0:
            allocation = "contiguous"
        else:   
            allocation = "linked"
        
        # Criando o objeto 'arquivo'
        file = {
            'name':file_name,
            'size': size
        }
        
        # Realizando a alocacao da memoria e intanciando o retorno 
        start_index = memory.allocate(file,allocation)
        
        # Verificando se deu certo a alaocacao da memoria
        if start_index is not None:
            
            # Realizando a adicao do novo no
            status = dir.add_node(file_name,current_dir,file_size=size, allocation=allocation,start_index=start_index,type="Arquivo", text=file_text)
            
            # Verificando o status da operacao de adicao e retornando a resposta
            if status == 0:
                messagebox.showerror("Erro ao criar o arquivo","Ja existe um arquivo com este nome no diretorio")
            elif status == 1:
                messagebox.showinfo("Criar arquivo", "Arquivo criado com sucesso")
                self.current_selected = None
                self.current_selected_option.configure(text=f"  {'Selecione um arquivo ou diretorio.'}")
                self.create_mainFileList()
                self.crtf.destroy()
            else:
                messagebox.showerror("Erro ao criar o arquivo","O diretorio nao foi encontrado")
    
        else:
            messagebox.showerror("Erro ao criar o arquivo","Nao ha espaco suficiente na memoria")
        
# Metodo para criar pasta
def create_folder(self):
    
    # Intanciando dados da pasta
    folder_name = self.crtd.direname.get()
    current_dir = self.current_dir
    dir = self.dir
    
    # Adicionando o no que contem a pasta
    status = dir.add_node(folder_name,current_dir, type="Pasta de arquivos")
    
    # Verificando o status da operacao e rotornando a resposta
    if status == 0:
        messagebox.showerror("Erro ao criar pasta","Ja existe uma pasta com este nome no diretorio")
    elif status == 1:    
        messagebox.showinfo("Criar pasta", "Pasta criada com sucesso")
        self.current_selected = None
        self.current_selected_option.configure(text=f"  {'Selecione um arquivo ou diretorio.'}")
        self.create_mainFileList()
        self.crtd.destroy()
    else:
        messagebox.showerror("Erro ao criar pasta","O diretorio nao foi encontrado")

# Metodo para deletar item
def delete(self):
    
    # Intanciando variaveis do sistema 
    dir = self.dir
    current_dir = self.current_dir
    memory = self.memory
    current_selected = self.current_selected
    
    # Verificando se existe item selecionado
    if current_selected:
        
        # Verificando o tipo do item selecioando
        if current_selected.type == "Arquivo":
            
            # Intanciando dados do arquivo selcionado
            start_index = current_selected.start_index
            size = current_selected.file_size
            allocation_type = current_selected.allocation
            
            # Removendo o no do arquivo
            status = dir.remove_node(current_selected.name,current_dir)
            
            # Verificando o status da operacao e rotornando a resposta
            if status == 0:
                messagebox.showerror("Erro ao deletar","Arquivo  nao encontrada no diretorio")
            elif status == 1:
                
                # Realizando a desalocacao na memoria do arquivo
                memory.deallocate(start_index=start_index,size=size,allocation_type=allocation_type)
                messagebox.showinfo("Delete completo", "Arquivo deletado com sucesso com sucesso")
                
                # Desselecionando item 
                self.current_selected = None
                self.current_selected_option.configure(text=f"  {'Selecione um arquivo ou diretorio.'}")
                self.create_mainFileList()
            else:
                messagebox.showerror("Erro ao deletar","O diretorio nao foi encontrado") 
        else:
            
            # Removendo o no do arquivo
            status = dir.remove_node(current_selected.name, current_dir)
            
            # Verificando o status da operacao e rotornando a resposta
            if status == 0:
                messagebox.showerror("Erro ao deletar","Pasta nao encontrada no diretorio")
            elif status == 1:
                messagebox.showinfo("Delete completo", "Pasta deletada com sucesso com sucesso")
                
                # Desselecionando item 
                self.current_selected = None
                self.current_selected_option.configure(text=f"  {'Selecione um arquivo ou diretorio.'}")
                self.create_mainFileList()
            else:
                messagebox.showerror("Erro ao deletar","O diretorio nao foi encontrado") 
    else: 
        messagebox.showerror("Erro ao deletar","Selecione algo")

# Metodo para renomear item
def rename(self):
    
    # Instanciando item selecioando
    current_selected = self.current_selected
    
    # Percorrendo os nomes dos items do diretorio atual
    for name in self.current_files:
        
        # Verificando se o item do diretorio atual tem mesmo nome do novo nome do item selecionado
        if name.name == self.rnm.direname.get():
            messagebox.showerror("Erro ao renomear", "Ja existe um arquivo ou pasta com esse nome")
            
            # Desselecioando item 
            self.current_selected = None
            self.current_selected_option.configure(text=f"  {'Selecione um arquivo ou diretorio.'}")
            self.rnm.destroy()
            return self.create_mainFileList()
    
    # Mudando o nome do item selecionado
    current_selected.name = self.rnm.direname.get()
    messagebox.showinfo("Renomear", "Arquivo ou pasta renomeado(a) com sucesso")
    self.create_mainFileList()
    self.rnm.destroy()

# Metodo para salvar alteracoes do arquivo
def file_save(self):
    
    # Verficando se o conteudo do arquivo eh o mesmo que ja estava la
    if self.open_file.text.get("1.0", "end-1c") == self.current_selected.text:
        
        # Desselecioando item 
        self.current_selected = None
        self.current_selected_option.configure(text=f"  {'Selecione um arquivo ou diretorio.'}")
        
        # Retornando resultado da opecacao
        messagebox.showinfo("Alteracoes", "Arquivo salvo (sem novas alteracoes)")
        self.open_file.destroy()
    
    else:
        
        # Setando o novo conteudo do arquivo 
        self.current_selected.text = self.open_file.text.get("1.0", "end-1c")
        
        # Desselecioando item
        self.current_selected = None
        self.current_selected_option.configure(text=f"  {'Selecione um arquivo ou diretorio.'}")
        
        # Retornando resultado da opecacao
        messagebox.showinfo("Alteracoes", "Alterecoes realizadas com sucesso.")
        self.open_file.destroy()

# Metodo para abrir uma pasta
def folder_open(self):
    
    # Atualizando o novo diretorio 
    new_dir = self.current_dir+f"/{self.current_selected.name}"
    
    # Intanciando o diretorio atual como o novo diretorio
    self.current_dir = new_dir
    
    # Desselecionando item
    self.current_selected = None
    self.current_selected_option.configure(text=f"  {'Selecione um arquivo ou diretorio.'}")
    
    # Gerando a lista de itens do diretorio atual 
    self.create_mainFileList()
    self.directory_label.configure(text=f"  {self.current_dir}")

# Metodo para acessar o diretorio pai
def parent_dir(self):
    
    # Verificando se o diretorio atual eh o diretorio raiz do usuario
    if self.current_dir == "C:/users/user_"+self.username:
        messagebox.showerror("Erro", "Voce nao tem acesso ao diretorio pai atual")
    else:
        
        # Setando o diretorio atual como o diretorio do pai 
        self.current_dir = os.path.dirname(self.current_dir)
        
        # Desselecionando item
        self.current_selected = None
        self.current_selected_option.configure(text=f"  {'Selecione um arquivo ou diretorio.'}")
        
        # Gerando a lsita de itens do diretorio atual 
        self.create_mainFileList()
        self.directory_label.configure(text=f"  {self.current_dir}")
        
# Metodo mostrar a memoria 
def display_memory(self):
    
    # Intanciando o conteudo da memoria
    memory_info = self.memory.display_memory()
    
    # Inserindo o conteudo da memoria no textbox
    self.mmr.text.insert("1.0",memory_info)
    self.mmr.text.configure(state="disabled")

 
