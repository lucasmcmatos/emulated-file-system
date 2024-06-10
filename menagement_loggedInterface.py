import os
from tkinter import messagebox
import math
from anytree import Node, RenderTree



def list_files(dir, path):
    parent_path, node_name =  path.rsplit('/', 1) if '/' in path else parent_path.rsplit('\\', 1)
    children = dir.find_node(node_name, parent_path).children
    return children

def create_file(self):
    
    file_name = self.crtf.filename.get()
    file_text = self.crtf.text.get("1.0", "end-1c")
    file_allocation = self.crtf.radio_var.get()
    current_dir = self.current_dir
    dir = self.dir
    memory = self.memory
    
    if file_name=="" or file_text=="":
        messagebox.showerror("Criar arquivo","Preencha todos os campos")
    else:
        
        size = math.ceil(len(file_text) / 10)
        if file_allocation==0:
            allocation = "contiguous"
        else:   
            allocation = "linked"
        
        file = {
            'name':file_name,
            'size': size
        }
        
        start_index = memory.allocate(file,allocation)
        
        if start_index is not None:
            
            status = dir.add_node(file_name,current_dir,file_size=size, allocation=allocation,start_index=start_index,type="Arquivo", text=file_text)
            
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
        

def create_folder(self):
    folder_name = self.crtd.direname.get()
    current_dir = self.current_dir
    dir = self.dir
    
    status = dir.add_node(folder_name,current_dir, type="Pasta de arquivos")
            
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
    
def delete(self):
    dir = self.dir
    current_dir = self.current_dir
    memory = self.memory
    current_selected = self.current_selected
    
    if current_selected:
        
        if current_selected.type == "Arquivo":
            start_index = current_selected.start_index
            size = current_selected.file_size
            allocation_type = current_selected.allocation
            
            status = dir.remove_node(current_selected.name,current_dir)
            
            if status == 0:
                messagebox.showerror("Erro ao deletar","Arquivo  nao encontrada no diretorio")
            elif status == 1:
                
                memory.deallocate(start_index=start_index,size=size,allocation_type=allocation_type)
                messagebox.showinfo("Delete completo", "Arquivo deletado com sucesso com sucesso")
                self.current_selected = None
                self.current_selected_option.configure(text=f"  {'Selecione um arquivo ou diretorio.'}")
                self.create_mainFileList()
            else:
                messagebox.showerror("Erro ao deletar","O diretorio nao foi encontrado") 
        else:
            status = dir.remove_node(current_selected.name, current_dir)
            if status == 0:
                messagebox.showerror("Erro ao deletar","Pasta nao encontrada no diretorio")
            elif status == 1:
                messagebox.showinfo("Delete completo", "Pasta deletada com sucesso com sucesso")
                self.current_selected = None
                self.current_selected_option.configure(text=f"  {'Selecione um arquivo ou diretorio.'}")
                self.create_mainFileList()
            else:
                messagebox.showerror("Erro ao deletar","O diretorio nao foi encontrado") 
    else: 
        messagebox.showerror("Erro ao deletar","Selecione algo")

def rename(self):
    current_selected = self.current_selected
    
    for name in self.current_files:
        if name.name == self.rnm.direname.get():
            messagebox.showerror("Erro ao renomear", "Ja existe um arquivo ou pasta com esse nome")
            self.current_selected = None
            self.current_selected_option.configure(text=f"  {'Selecione um arquivo ou diretorio.'}")
            self.rnm.destroy()
            return self.create_mainFileList()
    
            
    current_selected.name = self.rnm.direname.get()
    messagebox.showinfo("Renomear", "Arquivo ou pasta renomeado(a) com sucesso")
    self.create_mainFileList()
    self.rnm.destroy()
    
def file_save(self):
    
    if self.open_file.text.get("1.0", "end-1c") == self.current_selected.text:
        self.current_selected = None
        self.current_selected_option.configure(text=f"  {'Selecione um arquivo ou diretorio.'}")
        messagebox.showinfo("Alteracoes", "Arquivo salvo (sem novas alteracoes)")
        self.open_file.destroy()
    else:
        self.current_selected.text = self.open_file.text.get("1.0", "end-1c")
        self.current_selected = None
        self.current_selected_option.configure(text=f"  {'Selecione um arquivo ou diretorio.'}")
        messagebox.showinfo("Alteracoes", "Alterecoes realizadas com sucesso.")
        self.open_file.destroy()
    
def folder_open(self):
    new_dir = self.current_dir+f"/{self.current_selected.name}"
    self.current_dir = new_dir
    self.current_selected = None
    self.current_selected_option.configure(text=f"  {'Selecione um arquivo ou diretorio.'}")
    self.create_mainFileList()
    self.directory_label.configure(text=f"  {self.current_dir}")

def parent_dir(self):
    if self.current_dir == "C:/users/user_"+self.username:
        messagebox.showerror("Erro", "Voce nao tem acesso ao diretorio pai atual")
    else:
        self.current_dir = os.path.dirname(self.current_dir)
        self.current_selected = None
        self.current_selected_option.configure(text=f"  {'Selecione um arquivo ou diretorio.'}")
        self.create_mainFileList()
        self.directory_label.configure(text=f"  {self.current_dir}")
        
        

    
def display_memory(self):
    memory_info = self.memory.display_memory()
    self.mmr.text.insert("1.0",memory_info)
    self.mmr.text.configure(state="disabled")

 
