# Implementacao da interface de login do sistema

# Importacao dos metodos e bibliotecas necessarias para o sistema
import customtkinter
from tkinter import messagebox
from auth import Auth
from PIL import Image

# Setando a aparencia do sistema
customtkinter.set_appearance_mode("system") 

# Definicao da classe que armazena todos os metodos da pagina de login
class Login(customtkinter.CTk):
    
    # Definicao do construtor da classe "App"
    def __init__(self, dir, memory):
        
        # Intanciando o diretorio e a memoria
        self.dir = dir
        self.memory = memory
        
        # Intanciando a variavel que indica se o usuario esta logado ou nao
        self.user_logged_in = False
        
        # Iniciando a interface
        super().__init__()    
        
        #Configurando o titulo da janela de login
        self.title("Login")
        
        #Configurando o tamanha da janela de login
        self.geometry(f"{800}x{600}")
        
        #Configurando a proporcao da janela de login para que nao possa ser alterada
        self.resizable(False, False)
        
        #Definido o incone da janela de login
        self.iconbitmap('images/ajllslogo.ico')
        
        #Configurando a imagem principal da janela de login
        self.side_image = customtkinter.CTkImage(dark_image=Image.open('images/AJLLS.png'), size=(400,600))
        self.side_label = customtkinter.CTkLabel(self, text="", image=self.side_image)
        self.side_label.place(x=0, y=1)      
        
        #Configurando o frame que contem o formulario de logim propriamente dito
        self.frame = customtkinter.CTkFrame(self, width=390, height=590)
        self.frame.place(x=405, y=5)
        
        #Definido o titulo do frame de login
        self.label = customtkinter.CTkLabel(master=self.frame, text="Fazer Login", font=("Bahnschrift SemiBold", 25), text_color="#F78AFC" )
        self.label.place(x=130, y=150)
        
        #Criando os inputs de "username" e "password" do formulario de login
        self.entry_user = customtkinter.CTkEntry(master=self.frame, placeholder_text="Nome de usuário", width=300, font=("Bahnschrift", 14))
        self.entry_user.place(x=50, y=200)
        self.entry_password = customtkinter.CTkEntry(master=self.frame, placeholder_text="Senha", width=300, font=("Bahnschrift", 14), show="*")
        self.entry_password.place(x=50, y=250)
        
        #Criando e configurando o botao de login
        self.login_btn = customtkinter.CTkButton(master=self.frame, text="Login", font=("Bahnschrift SemiBold", 12), width=200, fg_color="#9128E2", hover_color="#58168d", command=self.login_authentication)
        self.login_btn.place(x=100, y=300)
        
        #Criando e configurando o texto de cadastro do sistema
        self.label_register = customtkinter.CTkLabel(master=self.frame, text="Ainda não possui sua conta?", font=("Bahnschrift", 14))
        self.label_register.place(x=110, y=350)
        
        #Criando e configurando o botao de cadastro no sistema
        self.register_btn = customtkinter.CTkButton(master=self.frame, text="Cadastre-se", font=("Bahnschrift SemiBold", 12), text_color="white", width=100, fg_color="#58168d", hover_color="#300d51", command=self.register_user)
        self.register_btn.place(x=150, y=380)
        
        #Aplicando o tema selecionado pelo usuario
        self.appearance_mode_label = customtkinter.CTkLabel(master=self.frame, text="Tema:", anchor="w")
        self.appearance_mode_label.place(x=80, y=550)
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.frame, values=["Dark", "Light", "System"], command=self.change_appearance_mode_event, fg_color="#9128e2", button_color="#9128e2",
                                                                        button_hover_color="#58168d", font=("Bahnschrift",14), dropdown_font=("Bahnschrift",14))
        self.appearance_mode_optionemenu.place(x=130, y=550)
    
    #Metodo que gera a janela de cadastro no sistema
    def register_user(self):
        
        # Defindo a variavel que armazena a ajanela no sistema de forma global
        global rgstr
        
        # Definindo as caracterisiticas da janela 
        rgstr = customtkinter.CTk()
        
        # Configurando o titulo da janela de cadastro
        rgstr.title("Cadastro")
        
        #Configurando a dimensao da janela 
        rgstr.geometry("400x270")
        
        # Definindo a imagem do logo da janela 
        rgstr.iconbitmap('images/ajllslogo.ico')
        
        # Configurando a proporcao da janela de login para que nao possa ser alterada
        rgstr.resizable(False, False)
        
        # Configurando o frame de caddastro dentro da janela
        rgstr.frame = customtkinter.CTkFrame(master=rgstr, width=390, height=290)
        rgstr.frame.place(x=5, y=5)
        
        # Configurando a area de cadastro
        rgstr.label_title = customtkinter.CTkLabel(master=rgstr.frame, text="Faça seu cadastro abaixo", font=("Bahnschrift SemiBold", 18))
        rgstr.label_title.place(x=100, y=20)
        
        # Configurando o input de "Nome de usuario"      
        rgstr.username = customtkinter.CTkEntry(master=rgstr, placeholder_text="Nome de usuário", width=250, font=("Bahnschrift", 14))
        rgstr.username.place(x=80, y=70)
        rgstr.label_username = customtkinter.CTkLabel(master=rgstr.frame, text="*Utilize apenas letras e números*", font=("Bahnschrift", 10))
        rgstr.label_username.place(x=80, y=90)
        
        # Configurando o input de "Senha"
        rgstr.password = customtkinter.CTkEntry(master=rgstr, placeholder_text="Senha", width=250, font=("Bahnschrift", 14))
        rgstr.password.place(x=80, y=130)
        rgstr.label_password = customtkinter.CTkLabel(master=rgstr.frame, text="*Cuidado ao colocar a senha*", font=("Bahnschrift", 10))
        rgstr.label_password.place(x=80, y=150)
        rgstr.label_password.place(x=80, y=150)
        
        # Configurando o botao de cadastro
        rgstr.btn_register = customtkinter.CTkButton(master=rgstr.frame, text="Cadastrar", width=130, font=("Bahnschrift SemiBold", 14), fg_color="#9128E2", hover_color="#58168d", command=self.register_new_user)
        rgstr.btn_register.place(x=130, y=200)
        
        rgstr.mainloop()
   
    # Metodo que realiza o cadastro de um novo usuario no sitema
    def register_new_user(self):
        
        # Definindo as variaveis utilizadas no metodo
        username = rgstr.username.get()
        password = rgstr.password.get()
        register = Auth.register(username,password, self.dir)
        
        # Verificando se o cadastro foi realizado com sucesso
        if register:
            
            # Retorno caso seja sucesso
            messagebox.showinfo('Cadastro', 'Usuario cadastrado com sucesso.')
            rgstr.destroy()
            
        else:
            
            # Retorno caso de erro no cadastro
            messagebox.showerror('Cadastro', 'Usuario ja cadastrado na plataforma.')
        
    # Metodo pare realizacao do login de um novo usuario no sistema
    def login_authentication(self):
        
        # Definicao das variaveis necessarios para o metodo
        username = self.entry_user.get()
        password = self.entry_password.get()
        user = Auth.login(username,password, self.dir)
        
        # Verificando se o login foi realizado com sucesso
        if user:
            
            # Retorno caso o seja sucesso
            print("Usuario logado com sucesso.")
            self.user_logged_in = True
            self.username = username
            if self.user_logged_in:
                self.destroy()
        else:
            
            # Retorno caso de erro no login
            messagebox.showerror('Login', 'Usuario ou senha incorreto(os).')
        
    # Metodo para mudanca da aparencia do sistema 
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    

    
 
