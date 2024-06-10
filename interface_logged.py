import tkinter
import customtkinter
from tkinter import messagebox
import menagement_loggedInterface
from PIL import Image

#TEMA DE ACORDO COM O SISTEMA
customtkinter.set_appearance_mode("system")

class Logged(customtkinter.CTk):
    def __init__(self, dir, memory, username):
        super().__init__()
        self.dir = dir
        self.memory = memory
        self.current_selected = None
        self.current_dir = "C:/users/user_" + username
        self.username = username
        self.create_widgets()
        
        
    def create_widgets(self):
        
        # AJUSTANDO JANELA
        self.title("Gerenciador de Arquivos AJLLS")
        self.geometry(f"{1285}x{550}")
        self.resizable(False, False)
        self.iconbitmap('images/ajllslogo.ico')

        # BARRA DE DIRETÓRIOS
        self.directory_frame = customtkinter.CTkFrame(master=self, height=30, width=662, corner_radius=5)
        self.directory_frame.place(x=160, y=26)
        self.directory_title = customtkinter.CTkLabel(master=self, width=100,text=f"Diretorio atual",font=("Bahnschrift SemiBold", 18), anchor="w")
        self.directory_title.place(x=30, y=25)
        self.directory_label = customtkinter.CTkLabel(master=self.directory_frame,font=("Bahnschrift", 12), width=662,text=f"  {self.current_dir}", anchor="w")
        self.directory_label.pack(fill="both", expand=True, padx=5)

        # Barra de selecionado
        self.current_selected_option_frame = customtkinter.CTkFrame(master=self, height=30, width=662, corner_radius=5)
        self.current_selected_option_frame.place(x=160, y=66)
        self.current_selected_option_title = customtkinter.CTkLabel(master=self, width=100,text=f"Selecionado",font=("Bahnschrift", 18), anchor="w")
        self.current_selected_option_title.place(x=30, y=65)
        self.current_selected_option = customtkinter.CTkLabel(self.current_selected_option_frame, text=f"  {'Selecione um arquivo ou diretorio.'}",fg_color="transparent" ,width=662 ,font=("Bahnschrift", 12),  anchor="w")
        self.current_selected_option.pack(fill="both", expand=True, padx=5)

        
        # LISTA DOS ARQUIVOS E PASTAS
        self.list_frame = customtkinter.CTkFrame(master=self, width=800, height=424)
        self.list_frame.place(x=30, y=106)
        
        self.create_mainFileList()
        
        # BOTÕES
        self.createfile_btn = customtkinter.CTkButton(master=self, width=200, height=30, text="Criar Arquivo", font=("Bahnschrift SemiBold", 14), fg_color="#9128E2", hover_color="#300D51",  command=self.window_createFile)
        self.createfile_btn.place(x=850, y=25)
        self.createdrctr_btn = customtkinter.CTkButton(master=self, width=200, height=30, text="Criar Pasta", font=("Bahnschrift SemiBold", 14), fg_color="#9128E2", hover_color="#300D51",  command=self.window_createFolder)
        self.createdrctr_btn.place(x=1060, y=25)
        self.open_btn = customtkinter.CTkButton(master=self, width=200, height=30, text="Abrir", font=("Bahnschrift SemiBold", 14), fg_color="#9128E2", hover_color="#300D51", command=self.window_open)
        self.open_btn.place(x=1060, y=105)
        self.rename_bnt = customtkinter.CTkButton(master=self, width=200, height=30, text="Renomear", font=("Bahnschrift SemiBold", 14), fg_color="#9128E2", hover_color="#300D51", command=self.window_rename)
        self.rename_bnt.place(x=1060, y=65)
        self.delete_bnt = customtkinter.CTkButton(master=self, width=200, height=30, text="Excluir", font=("Bahnschrift SemiBold", 14), fg_color="#9128E2", hover_color="#300D51",  command=lambda: menagement_loggedInterface.delete(self))
        self.delete_bnt.place(x=850, y=105)
        self.memory_bnt = customtkinter.CTkButton(master=self, width=200, height=30, text="Ver Memória", font=("Bahnschrift SemiBold", 14), fg_color="transparent", hover_color="#300D51", border_width=2,border_color="#9128E2" , text_color="#9128E2", command=self.window_displayMemory)
        self.memory_bnt.place(x=1060, y=145)
        self.comeback_bnt = customtkinter.CTkButton(master=self, width=200, height=30, text="Diretorio pai", font=("Bahnschrift SemiBold", 14), fg_color="transparent", hover_color="#300D51", border_width=2,border_color="#9128E2" , text_color="#9128E2", command=lambda: menagement_loggedInterface.parent_dir(self))
        self.comeback_bnt.place(x=850, y=145)
        self.move_bnt = customtkinter.CTkButton(master=self, width=200, height=30, text="Mover", font=("Bahnschrift SemiBold", 14), fg_color="#9128E2", hover_color="#300D51", command= self.window_move)
        self.move_bnt.place(x=850, y=65)
        
        # LOGOTIPO
        self.logo_image = customtkinter.CTkImage(dark_image=Image.open('images/ajllslogo.png'), size=(200,200))
        self.logo_label = customtkinter.CTkLabel(self, text="", image=self.logo_image)
        self.logo_label.place(x=945, y=230)
        
        # VERSÃO
        self.version = customtkinter.CTkLabel(master=self, text="app.version.Beta 1.0. Todos os direitos reservados.", font=("Bahnschrift",10))
        self.version.place(x=950, y=430)

        # TEMA DA APLICAÇÃO
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self, values=["Dark", "Light", "System"], command=self.change_appearance_mode_event, fg_color="#9128e2", button_color="#9128e2", button_hover_color="#58168d", font=("Bahnschrift",14), dropdown_font=("Bahnschrift",14))
        self.appearance_mode_optionemenu.place(x=1120, y=505)
    
    
        
    
    def button_click_handler(self, node):
        self.current_selected = node
        self.current_selected_option.configure(text=f"  {self.current_selected.name}")
    
    # Funcao para criar a lista de arquivos principal do sistema
    def create_mainFileList(self):
        
        self.current_files = menagement_loggedInterface.list_files(self.dir,self.current_dir)
        
        for widget in self.list_frame.winfo_children():
            widget.destroy()
            
        header_frame = customtkinter.CTkFrame(self.list_frame)
        header_frame.pack(fill="x")
        customtkinter.CTkLabel(header_frame, text="Nome", width=500).pack(side="left")
        customtkinter.CTkLabel(header_frame, text="Tipo", width=150).pack(side="left")
        customtkinter.CTkLabel(header_frame, text="Tamanho (blocos)", width=150).pack(side="left")
        
        for node in self.current_files:
            
            info_frame = customtkinter.CTkFrame(self.list_frame, fg_color="transparent")
            info_frame.pack(fill="x")
            
            name = getattr(node, 'name', 'Unknown')
            file_type = getattr(node, 'type', 'Unknown')
            
            if file_type == "Arquivo":
                size = getattr(node, 'file_size', 'Unknown')
            else:
                size = ""
            
            customtkinter.CTkButton(info_frame,text=f"{name}",width=500,corner_radius=0 , hover_color="#300D51", fg_color="transparent",command=lambda n=node: self.button_click_handler(n)).grid(row=0, column=0)
            customtkinter.CTkLabel(info_frame, text=f"{file_type}", width=150).grid(row=0, column=1)
            customtkinter.CTkLabel(info_frame, text=f"{size}", width=150).grid(row=0, column=2)
    
    def button_move(self, node):
        
        self.current_selected.parent = node
        self.create_mainFileList()
        self.current_selected = None
        self.current_selected_option.configure(text=f"  {'Selecione um arquivo ou diretorio.'}")
        self.move.destroy()
    
    def create_foldersList(self):
        
        self.folder_list = self.dir.find_node("user_"+self.username).children
        
        for widget in self.move.list_frame.winfo_children():
            widget.destroy()
            
        folderList_header = customtkinter.CTkFrame(self.move.list_frame)
        folderList_header.pack(fill="x")
        customtkinter.CTkLabel(folderList_header, text="Nome do diretorio", width=460).pack(side="left")
        
        for node in self.folder_list:
            
            name = getattr(node, 'name', 'Unknown')
            file_type = getattr(node, 'type', 'Unknown')
            
            # Adiciona um botão apenas se for uma pasta de arquivos e não a pasta atualmente selecionada
            if file_type == "Pasta de arquivos" and self.current_selected.name != name:
                new_info_frame = customtkinter.CTkFrame(self.move.list_frame, fg_color="transparent")
                new_info_frame.pack(fill="x")
                customtkinter.CTkButton(new_info_frame,text=f"{name}",width=460,corner_radius=0 , hover_color="#300D51", fg_color="transparent",command=lambda n=node: self.button_move(n)).grid(row=0, column=0)
            
    def window_createFile(self):
        self.crtf = customtkinter.CTk()
        self.crtf.title("Preencha as informações do arquivo que deseja criar")
        self.crtf.geometry("500x400")
        self.crtf.iconbitmap('images/ajllslogo.ico')
        self.crtf.resizable(False, False)
        self.crtf.protocol("WM_DELETE_WINDOW", self.crtf.destroy)
        self.crtf.filename = customtkinter.CTkEntry(master=self.crtf, placeholder_text="Nome do arquivo", font=("Bahnschrift",14), width=350)
        self.crtf.filename.place(x=20, y=20)
        self.crtf.text_frame = customtkinter.CTkFrame(master=self.crtf, width=460, height=250)
        self.crtf.text_frame.place(x=20, y=70)
        self.crtf.text = customtkinter.CTkTextbox(master=self.crtf.text_frame, width=460, height=250, font=("Bahnschrift", 12))
        self.crtf.text.place(x=0, y=0)
        self.crtf.radiobutton_frame = customtkinter.CTkFrame(master=self.crtf, width=460, height=50)
        self.crtf.radiobutton_frame.place(x=20, y=330)
        self.crtf.radio_var = tkinter.IntVar(value=0)
        self.crtf.contradio_btn = customtkinter.CTkRadioButton(master=self.crtf.radiobutton_frame, text="Alocação Contígua", font=("Bahnschrift", 12), variable=self.crtf.radio_var, value=0, fg_color="#58168d", hover_color="#300d51")
        self.crtf.contradio_btn.place(x=80, y=10)
        self.crtf.encaradio_btn = customtkinter.CTkRadioButton(master=self.crtf.radiobutton_frame, text="Alocação Encadeada", font=("Bahnschrift", 12), variable=self.crtf.radio_var, value=1, fg_color="#58168d", hover_color="#300d51")
        self.crtf.encaradio_btn.place(x=250, y=10)
        
        self.crtf.filesave_btn = customtkinter.CTkButton(master=self.crtf, text="Salvar", font=("Bahnschrift SemiBold",14), width=100, fg_color="#58168d", hover_color="#300d51", command=lambda: menagement_loggedInterface.create_file(self))
        self.crtf.filesave_btn.place(x=380, y=20)

        self.crtf.mainloop()

    def window_createFolder(self):
        
        self.crtd = customtkinter.CTk()
        self.crtd.title("Digite o nome da pasta que deseja criar")
        self.crtd.geometry("510x70")
        self.crtd.iconbitmap('images/ajllslogo.ico')
        self.crtd.resizable(False, False)
        self.crtd.protocol("WM_DELETE_WINDOW", self.crtd.destroy)
        self.crtd.direname = customtkinter.CTkEntry(master=self.crtd, placeholder_text="Nome da pasta", font=("Bahnschrift",14), width=350)
        self.crtd.direname.place(x=25, y=20)
        self.crtd.diresave = customtkinter.CTkButton(master=self.crtd, text="Salvar", font=("Bahnschrift SemiBold",14), width=100, fg_color="#58168d", hover_color="#300d51", command=lambda: menagement_loggedInterface.create_folder(self))
        self.crtd.diresave.place(x=385, y=20)
        
        self.crtd.mainloop()
    
    def window_open(self):
        if self.current_selected:
            
            if self.current_selected.type == "Arquivo":
                
                self.open_file = customtkinter.CTk()
                self.open_file.title("Preencha as informações do arquivo que deseja criar")
                self.open_file.geometry("500x400")
                self.open_file.iconbitmap('images/ajllslogo.ico')
                self.open_file.resizable(False, False)
                self.open_file.protocol("WM_DELETE_WINDOW", self.open_file.destroy)
                self.open_file.directory_title = customtkinter.CTkLabel(master=self.open_file, width=100,text=f"Nome do arquivo:",font=("Bahnschrift SemiBold", 18), anchor="w")
                self.open_file.directory_title.place(x=20, y=10)
                self.open_file.directory_text = customtkinter.CTkLabel(master=self.open_file, width=100, text=f"{self.current_selected.name}.txt", font=("Bahnschrift", 16), anchor="w")
                self.open_file.directory_text.place(x=170,y=11)
                self.open_file.text_frame = customtkinter.CTkFrame(master=self.open_file, width=460, height=280)
                self.open_file.text_frame.place(x=20, y=53)
                self.open_file.text = customtkinter.CTkTextbox(master=self.open_file.text_frame, width=460, height=280, font=("Bahnschrift", 12))
                self.open_file.text.place(x=0, y=0)
                self.open_file.text.insert("1.0", self.current_selected.text)
                self.open_file.savebtn = customtkinter.CTkButton(master=self.open_file, text="Salvar alteracoes", font=("Bahnschrift SemiBold",14), width=460, fg_color="#58168d", hover_color="#300d51", command=lambda: menagement_loggedInterface.file_save(self))
                self.open_file.savebtn.place(x=20,y=353)
                
                self.open_file.mainloop()
                
            else:
                menagement_loggedInterface.folder_open(self)
                
        else:
            messagebox.showerror("Erro ao renomear","Selecione algo")
            
    def window_rename(self):
        
        if self.current_selected:
            self.rnm = customtkinter.CTk()
            self.rnm.title("Remoneie o arquivo ou diretorio selecionado")
            self.rnm.geometry("510x70")
            self.rnm.iconbitmap('images/ajllslogo.ico')
            self.rnm.resizable(False, False)
            self.rnm.protocol("WM_DELETE_WINDOW", self.rnm.destroy)
            self.rnm.direname = customtkinter.CTkEntry(master=self.rnm, placeholder_text="Novo nome", font=("Bahnschrift",14), width=350)
            self.rnm.direname.place(x=25, y=20)
            self.rnm.diresave = customtkinter.CTkButton(master=self.rnm, text="Salvar", font=("Bahnschrift SemiBold",14), width=100, fg_color="#58168d", hover_color="#300d51", command=lambda: menagement_loggedInterface.rename(self))
            self.rnm.diresave.place(x=385, y=20)
            
            self.rnm.mainloop()
        else:
            messagebox.showerror("Erro ao renomear","Selecione algo")
    
    def window_move(self):
        if self.current_selected:
            self.move = customtkinter.CTk()
            self.move.title("Selecione para onde deseja mover o arquivo ou diretorio")
            self.move.geometry("510x300")
            self.move.iconbitmap('images/ajllslogo.ico')
            self.move.resizable(False, False)
            self.move.protocol("WM_DELETE_WINDOW", self.move.destroy)
            
            self.move.list_frame = customtkinter.CTkFrame(master=self.move, width=460, height=200)
            self.move.list_frame.place(x=25, y=20)
            
            self.create_foldersList()
            
            self.move.mainloop()
        else:
            messagebox.showerror("Erro ao renomear","Selecione algo")
        
    def window_displayMemory(self):
        self.mmr = customtkinter.CTk()
        self.mmr.title("Estado atual da memoria")
        self.mmr.geometry("600x500")
        self.mmr.iconbitmap('images/ajllslogo.ico')
        self.mmr.resizable(False, False)
        self.mmr.protocol("WM_DELETE_WINDOW", self.mmr.destroy)
        self.mmr.text_frame = customtkinter.CTkFrame(master=self.mmr, width=560, height=450)
        self.mmr.text_frame.place(x=20, y=20)
        self.mmr.text = customtkinter.CTkTextbox(master=self.mmr.text_frame, width=560, height=450, font=("Bahnschrift", 12))
        self.mmr.text.place(x=0, y=0)
        menagement_loggedInterface.display_memory(self)
        self.mmr.mainloop()
        
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
