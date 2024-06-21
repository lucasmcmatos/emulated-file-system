# Condigo python que gera e manipula as interfaces apos o usuario realizar login

# Importacao das bibliotecas necessarias 
import tkinter
import customtkinter
from tkinter import messagebox
import menagement_loggedInterface
from PIL import Image

# Setando o tema da interface de acordo com o tema do sistema
customtkinter.set_appearance_mode("system")

# Classe responsavel por manipular todos os metodos necessarios para o funcionamento da interface
class Logged(customtkinter.CTk):
    
    # Construtor da classe logada
    def __init__(self, dir, memory, username):
        
        # Incializacao das principais variaveis usadas pela interface
        super().__init__() 
        self.dir = dir
        self.memory = memory
        self.current_selected = None
        self.current_dir = "C:/users/user_" + username
        self.username = username
        self.create_widgets() # Criando a janela principal do sistema
        
    # Metodo que configura a janela principal do sistema e seus elementos
    def create_widgets(self):
        
        # Configuracoes base do interface principal: Definindo e configurando as informacoes estaticas do interface principal
        
        # Definindo as informacoes base da janela e as suas proporcoes
        self.title("Gerenciador de Arquivos AJLLS")
        self.geometry(f"{1285}x{550}")
        self.resizable(False, False)
        self.iconbitmap('images/ajllslogo.ico')
        
        # Logotipo do sistema
        self.logo_image = customtkinter.CTkImage(dark_image=Image.open('images/ajllslogo.png'), size=(200,200))
        self.logo_label = customtkinter.CTkLabel(self, text="", image=self.logo_image)
        self.logo_label.place(x=945, y=230)
        
        # Definindo a versao do sistema
        self.version = customtkinter.CTkLabel(master=self, text="app.version.Beta 1.0. Todos os direitos reservados.", font=("Bahnschrift",10))
        self.version.place(x=950, y=430)

        # Definindo o select para mudar o tema da aplicacao
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self, values=["Dark", "Light", "System"], command=self.change_appearance_mode_event, fg_color="#9128e2", button_color="#9128e2", button_hover_color="#58168d", font=("Bahnschrift",14), dropdown_font=("Bahnschrift",14))
        self.appearance_mode_optionemenu.place(x=1120, y=505)

        # Diretorio atual: defindo e configurando as dimensoes do frame que mostra o diretorio atual
        self.directory_frame = customtkinter.CTkFrame(master=self, height=30, width=662, corner_radius=5)
        self.directory_frame.place(x=160, y=26)
        self.directory_title = customtkinter.CTkLabel(master=self, width=100,text=f"Diretorio atual",font=("Bahnschrift SemiBold", 18), anchor="w")
        self.directory_title.place(x=30, y=25)
        self.directory_label = customtkinter.CTkLabel(master=self.directory_frame,font=("Bahnschrift", 12), width=662,text=f"  {self.current_dir}", anchor="w")
        self.directory_label.pack(fill="both", expand=True, padx=5)

        # Item selecionado: definindo e configurando as dimensoes do frame que mostra o item selecionado (pasta ou arquivo)
        self.current_selected_option_frame = customtkinter.CTkFrame(master=self, height=30, width=662, corner_radius=5)
        self.current_selected_option_frame.place(x=160, y=66)
        self.current_selected_option_title = customtkinter.CTkLabel(master=self, width=100,text=f"Selecionado",font=("Bahnschrift", 18), anchor="w")
        self.current_selected_option_title.place(x=30, y=65)
        self.current_selected_option = customtkinter.CTkLabel(self.current_selected_option_frame, text=f"  {'Selecione um arquivo ou diretorio.'}",fg_color="transparent" ,width=662 ,font=("Bahnschrift", 12),  anchor="w")
        self.current_selected_option.pack(fill="both", expand=True, padx=5)

        # Lista de items: Definindo e configurando as dimensoes da lista de itens (pastas e arquivos)
        self.list_frame = customtkinter.CTkFrame(master=self, width=800, height=424)
        self.list_frame.place(x=30, y=106)
        self.create_mainFileList() # Chamando a funcao que gera a lista de itens (pastas e arquivos)
        
        # Botoes do sistema: Definindo os motoes do sistema 
        
        # Botao de criar arquivo
        self.createfile_btn = customtkinter.CTkButton(master=self, width=200, height=30, text="Criar Arquivo", font=("Bahnschrift SemiBold", 14), fg_color="#9128E2", hover_color="#300D51",  command=self.window_createFile) # Chama a funcao que cria o arquivo
        self.createfile_btn.place(x=850, y=25)
        
        # Botao de criar pasta
        self.createdrctr_btn = customtkinter.CTkButton(master=self, width=200, height=30, text="Criar Pasta", font=("Bahnschrift SemiBold", 14), fg_color="#9128E2", hover_color="#300D51",  command=self.window_createFolder) # Chama a funcao que cria a pasta
        self.createdrctr_btn.place(x=1060, y=25)
        
        # Botao de abrir item (pasta ou arquivo)
        self.open_btn = customtkinter.CTkButton(master=self, width=200, height=30, text="Abrir", font=("Bahnschrift SemiBold", 14), fg_color="#9128E2", hover_color="#300D51", command=self.window_open)
        self.open_btn.place(x=1060, y=105)
        
        # Botao para renomear item (pasta ou arquivo)
        self.rename_bnt = customtkinter.CTkButton(master=self, width=200, height=30, text="Renomear", font=("Bahnschrift SemiBold", 14), fg_color="#9128E2", hover_color="#300D51", command=self.window_rename)
        self.rename_bnt.place(x=1060, y=65)
        
        # Botao para deletar item (pasta ou arquivo)
        self.delete_bnt = customtkinter.CTkButton(master=self, width=200, height=30, text="Excluir", font=("Bahnschrift SemiBold", 14), fg_color="#9128E2", hover_color="#300D51",  command=lambda: menagement_loggedInterface.delete(self))
        self.delete_bnt.place(x=850, y=105)
        
        # Botao para vizualizar a memoria 
        self.memory_bnt = customtkinter.CTkButton(master=self, width=200, height=30, text="Ver Memória", font=("Bahnschrift SemiBold", 14), fg_color="transparent", hover_color="#300D51", border_width=2,border_color="#9128E2" , text_color="#9128E2", command=self.window_displayMemory)
        self.memory_bnt.place(x=1060, y=145)
        
        # Botao para voltar para o diretorio pai
        self.comeback_bnt = customtkinter.CTkButton(master=self, width=200, height=30, text="Diretorio pai", font=("Bahnschrift SemiBold", 14), fg_color="transparent", hover_color="#300D51", border_width=2,border_color="#9128E2" , text_color="#9128E2", command=lambda: menagement_loggedInterface.parent_dir(self))
        self.comeback_bnt.place(x=850, y=145)
        
        # Botao para mover um item (pasta ou arquivo) para algum diretorio
        self.move_bnt = customtkinter.CTkButton(master=self, width=200, height=30, text="Mover", font=("Bahnschrift SemiBold", 14), fg_color="#9128E2", hover_color="#300D51", command= self.window_move)
        self.move_bnt.place(x=850, y=65)
    
    # Metodo que pega o item clickado na lista e define ele como selecionado
    def button_click_handler(self, node):
        self.current_selected = node
        self.current_selected_option.configure(text=f"  {self.current_selected.name}")
    
    # Metodo para criar a lista de itens do diretorio atual
    def create_mainFileList(self):
        
        # Gerando a lista com funcao para gerar lista
        self.current_files = menagement_loggedInterface.list_files(self.dir,self.current_dir)
        
        # Destruindo os itens da lista atual do sistema
        for widget in self.list_frame.winfo_children():
            widget.destroy()
        
        # Criando o header da lista com seus labels
        header_frame = customtkinter.CTkFrame(self.list_frame)
        header_frame.pack(fill="x")
        customtkinter.CTkLabel(header_frame, text="Nome", width=500).pack(side="left")
        customtkinter.CTkLabel(header_frame, text="Tipo", width=150).pack(side="left")
        customtkinter.CTkLabel(header_frame, text="Tamanho (blocos)", width=150).pack(side="left")
        
        # Gerando os items da lista 
        for node in self.current_files:
            
            # Crian do frame do item
            info_frame = customtkinter.CTkFrame(self.list_frame, fg_color="transparent")
            info_frame.pack(fill="x")
            
            # Instanciando o nome e tipo do arquivo
            name = getattr(node, 'name', 'Unknown')
            file_type = getattr(node, 'type', 'Unknown')
            
            # Verificando o tipo do item (pasta ou arquivo)
            if file_type == "Arquivo":
                size = getattr(node, 'file_size', 'Unknown')
            else:
                size = ""
            
            # Definindo os frames das informacoes do item
            customtkinter.CTkButton(info_frame,text=f"{name}",width=500,corner_radius=0 , hover_color="#300D51", fg_color="transparent",command=lambda n=node: self.button_click_handler(n)).grid(row=0, column=0)
            customtkinter.CTkLabel(info_frame, text=f"{file_type}", width=150).grid(row=0, column=1)
            customtkinter.CTkLabel(info_frame, text=f"{size}", width=150).grid(row=0, column=2)
    
    # Metodo que gera a lista de pastas (aparece apos clickar em mover)
    def create_foldersList(self):
        
        # Instanciando a lista de pastas 
        self.folder_list = self.dir.find_node("user_"+self.username).children
        
        # Destruindo a lista de pastas que existia antes
        for widget in self.move.list_frame.winfo_children():
            widget.destroy()
        
        # Criando o header da lista
        folderList_header = customtkinter.CTkFrame(self.move.list_frame)
        folderList_header.pack(fill="x")
        customtkinter.CTkLabel(folderList_header, text="Nome do diretorio", width=460).pack(side="left")
        
        # Gerando os itens da lista
        for node in self.folder_list:
            
            # Instanciando os dados do item
            name = getattr(node, 'name', 'Unknown')
            file_type = getattr(node, 'type', 'Unknown')
            
            # Adiciona um botão apenas se for uma pasta de arquivos e não a pasta atualmente selecionada
            if file_type == "Pasta de arquivos" and self.current_selected.name != name:
                new_info_frame = customtkinter.CTkFrame(self.move.list_frame, fg_color="transparent")
                new_info_frame.pack(fill="x")
                customtkinter.CTkButton(new_info_frame,text=f"{name}",width=460,corner_radius=0 , hover_color="#300D51", fg_color="transparent",command=lambda n=node: self.button_move(n)).grid(row=0, column=0)
            
    # Metodo que pega o item clickado na lista de pastas da aba "mover"
    def button_move(self, node):
        
        self.current_selected.parent = node
        self.create_mainFileList() # Gerando a nova lista da main
        self.current_selected = None # Resetando o item selecionado
        self.current_selected_option.configure(text=f"  {'Selecione um arquivo ou diretorio.'}") # Resetando frame do item selecionado
        self.move.destroy()
        
    # Metodo que cria um novo arquivo
    def window_createFile(self):
        
        # Configuracoes base do interface de criacao de arquivo: Definindo e configurando as informacoes estaticas do interface 
        self.crtf = customtkinter.CTk()
        self.crtf.title("Preencha as informações do arquivo que deseja criar")
        self.crtf.geometry("500x400")
        self.crtf.iconbitmap('images/ajllslogo.ico')
        self.crtf.resizable(False, False)
        self.crtf.protocol("WM_DELETE_WINDOW", self.crtf.destroy)
        
        # Configurando input do nome do arquivo
        self.crtf.filename = customtkinter.CTkEntry(master=self.crtf, placeholder_text="Nome do arquivo", font=("Bahnschrift",14), width=350)
        self.crtf.filename.place(x=20, y=20)
        
        # Configurando o frame do textbox 
        self.crtf.text_frame = customtkinter.CTkFrame(master=self.crtf, width=460, height=250)
        self.crtf.text_frame.place(x=20, y=70)
        
        # Configurando o textbox
        self.crtf.text = customtkinter.CTkTextbox(master=self.crtf.text_frame, width=460, height=250, font=("Bahnschrift", 12))
        self.crtf.text.place(x=0, y=0)
        
        # Configurando o switch button
        self.crtf.radiobutton_frame = customtkinter.CTkFrame(master=self.crtf, width=460, height=50)
        self.crtf.radiobutton_frame.place(x=20, y=330)
        self.crtf.radio_var = tkinter.IntVar(value=0)
        self.crtf.contradio_btn = customtkinter.CTkRadioButton(master=self.crtf.radiobutton_frame, text="Alocação Contígua", font=("Bahnschrift", 12), variable=self.crtf.radio_var, value=0, fg_color="#58168d", hover_color="#300d51")
        self.crtf.contradio_btn.place(x=80, y=10)
        self.crtf.encaradio_btn = customtkinter.CTkRadioButton(master=self.crtf.radiobutton_frame, text="Alocação Encadeada", font=("Bahnschrift", 12), variable=self.crtf.radio_var, value=1, fg_color="#58168d", hover_color="#300d51")
        self.crtf.encaradio_btn.place(x=250, y=10)
        
        # Configurando o botao de salvar
        self.crtf.filesave_btn = customtkinter.CTkButton(master=self.crtf, text="Salvar", font=("Bahnschrift SemiBold",14), width=100, fg_color="#58168d", hover_color="#300d51", command=lambda: menagement_loggedInterface.create_file(self))
        self.crtf.filesave_btn.place(x=380, y=20)

        # Adicionando a interface no looping principal
        self.crtf.mainloop()

    # Metodo que cria uma nova pasta
    def window_createFolder(self):
        
        # Configuracoes base do interface de criacao de pasta: Definindo e configurando as informacoes estaticas do interface 
        self.crtd = customtkinter.CTk()
        self.crtd.title("Digite o nome da pasta que deseja criar")
        self.crtd.geometry("510x70")
        self.crtd.iconbitmap('images/ajllslogo.ico')
        self.crtd.resizable(False, False)
        self.crtd.protocol("WM_DELETE_WINDOW", self.crtd.destroy)
        
        # Configurando o input do nome da pasta
        self.crtd.direname = customtkinter.CTkEntry(master=self.crtd, placeholder_text="Nome da pasta", font=("Bahnschrift",14), width=350)
        self.crtd.direname.place(x=25, y=20)
        self.crtd.diresave = customtkinter.CTkButton(master=self.crtd, text="Salvar", font=("Bahnschrift SemiBold",14), width=100, fg_color="#58168d", hover_color="#300d51", command=lambda: menagement_loggedInterface.create_folder(self))
        self.crtd.diresave.place(x=385, y=20)
        
        # Adicionando a interface no looping principal
        self.crtd.mainloop()
    
    # Metodo que abre o item selecionado
    def window_open(self):
        
        # Verificando se existem item selecionado
        if self.current_selected:
            
            # Verificando o tipo do item selecionado
            if self.current_selected.type == "Arquivo":
                
                # Configuracoes base do interface de vizualizacao: Definindo e configurando as informacoes estaticas do interface  
                self.open_file = customtkinter.CTk()
                self.open_file.title("Preencha as informações do arquivo que deseja criar")
                self.open_file.geometry("500x400")
                self.open_file.iconbitmap('images/ajllslogo.ico')
                self.open_file.resizable(False, False)
                self.open_file.protocol("WM_DELETE_WINDOW", self.open_file.destroy)
                
                # Definidno o frame com o nome do arquivo
                self.open_file.directory_title = customtkinter.CTkLabel(master=self.open_file, width=100,text=f"Nome do arquivo:",font=("Bahnschrift SemiBold", 18), anchor="w")
                self.open_file.directory_title.place(x=20, y=10)
                self.open_file.directory_text = customtkinter.CTkLabel(master=self.open_file, width=100, text=f"{self.current_selected.name}.txt", font=("Bahnschrift", 16), anchor="w")
                self.open_file.directory_text.place(x=170,y=11)
                
                # Defindo o frame para o textbox com o conteudo do arquivo que pode ser alterado
                self.open_file.text_frame = customtkinter.CTkFrame(master=self.open_file, width=460, height=280)
                self.open_file.text_frame.place(x=20, y=53)
                self.open_file.text = customtkinter.CTkTextbox(master=self.open_file.text_frame, width=460, height=280, font=("Bahnschrift", 12))
                self.open_file.text.place(x=0, y=0)
                self.open_file.text.insert("1.0", self.current_selected.text)
                
                # Defindo o botao para salvar as alteracoes no arquivo
                self.open_file.savebtn = customtkinter.CTkButton(master=self.open_file, text="Salvar alteracoes", font=("Bahnschrift SemiBold",14), width=460, fg_color="#58168d", hover_color="#300d51", command=lambda: menagement_loggedInterface.file_save(self))
                self.open_file.savebtn.place(x=20,y=353)
                
                self.open_file.mainloop()
                
            else:
                
                # Chamando a funcao para abrir a pasta
                menagement_loggedInterface.folder_open(self)
                
        else:
            
            # Gerando o popup de erro caso nao haja nada selecionado
            messagebox.showerror("Erro ao renomear","Selecione algo")
            
    # Metodo para abrir a janela de renomear item
    def window_rename(self):
        
        # Verificando se existe item selecionado
        if self.current_selected:
        
            # Configuracoes base do interface de renomeacao: Definindo e configurando as informacoes estaticas do interface  
            self.rnm = customtkinter.CTk()
            self.rnm.title("Remoneie o arquivo ou diretorio selecionado")
            self.rnm.geometry("510x70")
            self.rnm.iconbitmap('images/ajllslogo.ico')
            self.rnm.resizable(False, False)
            self.rnm.protocol("WM_DELETE_WINDOW", self.rnm.destroy)
            
            # Definindo o input que recebe o novo nome do item
            self.rnm.direname = customtkinter.CTkEntry(master=self.rnm, placeholder_text="Novo nome", font=("Bahnschrift",14), width=350)
            self.rnm.direname.place(x=25, y=20)
            
            # Definindo o botao para salvar o novo nome
            self.rnm.diresave = customtkinter.CTkButton(master=self.rnm, text="Salvar", font=("Bahnschrift SemiBold",14), width=100, fg_color="#58168d", hover_color="#300d51", command=lambda: menagement_loggedInterface.rename(self))
            self.rnm.diresave.place(x=385, y=20)
            
            self.rnm.mainloop()
        else:
            
            # Gerando pop de erro 
            messagebox.showerror("Erro ao renomear","Selecione algo")
    
    
    # Metodo para abrir a janela de movimentar item
    def window_move(self):
        
        # Verificando se existe item selecionado
        if self.current_selected:
            
            # Configuracoes base do interface de movimentacao: Definindo e configurando as informacoes estaticas do interface  
            self.move = customtkinter.CTk()
            self.move.title("Selecione para onde deseja mover o arquivo ou diretorio")
            self.move.geometry("510x300")
            self.move.iconbitmap('images/ajllslogo.ico')
            self.move.resizable(False, False)
            self.move.protocol("WM_DELETE_WINDOW", self.move.destroy)
            
            # Definindo frame da lista de pastas do sistema
            self.move.list_frame = customtkinter.CTkFrame(master=self.move, width=460, height=200)
            self.move.list_frame.place(x=25, y=20)
            
            # Criando a lista de pastas
            self.create_foldersList()
            
            self.move.mainloop()
        else:
            
            # Gerando popup de error
            messagebox.showerror("Erro ao renomear","Selecione algo")
        
    # Metodo para abrir janela de vizualizacao da memoria
    def window_displayMemory(self):
        
        # Configuracoes base do interface de movimentacao: Definindo e configurando as informacoes estaticas do interface  
        self.mmr = customtkinter.CTk()
        self.mmr.title("Estado atual da memoria")
        self.mmr.geometry("600x500")
        self.mmr.iconbitmap('images/ajllslogo.ico')
        self.mmr.resizable(False, False)
        self.mmr.protocol("WM_DELETE_WINDOW", self.mmr.destroy)
        
        # Defindo o frame que compoem as informacoes da memoria
        self.mmr.text_frame = customtkinter.CTkFrame(master=self.mmr, width=560, height=450)
        self.mmr.text_frame.place(x=20, y=20)
        self.mmr.text = customtkinter.CTkTextbox(master=self.mmr.text_frame, width=560, height=450, font=("Bahnschrift", 12))
        self.mmr.text.place(x=0, y=0)
        
        # Chamando a funcao que printa a memoria 
        menagement_loggedInterface.display_memory(self)
        self.mmr.mainloop()
        
    # Metodo que define a aparencia do sistema
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
