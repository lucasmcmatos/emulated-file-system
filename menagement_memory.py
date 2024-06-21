# Implementação da simulação dos blocos na memória

# Importando metodos e bibliotecas necessarios para o sistema
from datetime import datetime

# Classe que representa o Bloco na memória (Será instanciada para cada bloco na memória)
class MemoryBlock:

    # Cosntrutor da classe 'MemoryBlock', serve para  inicializar o bloco
    def __init__(self):
        self.is_free = True # Setando o bloco como livre
        self.value = None # Setando o valor armazenado no bloco como None (Nada)
        self.next_block = None  #Para o caso alocação com lista encadeada, ponteiro que aponta para o próximo bloco na memória

    # Método para alocar o bloco (Marca como 'Ocupado' e armazena o valor nele)
    def allocate(self, value):
        self.is_free = False # Setando o bloco como Ocupado
        self.value = value # Armazenando o valor no bloco

    # Método para desalocar o bloco
    def deallocate(self):
        self.is_free = True # Setando o bloco como livre
        self.value = None # Removendo o valor armazenado
        self.next_block = None  # Resetando o ponteiro para o próximo bloco

    # Método para apresentar o bloco no formato de uma string (Mostra as informações necessárias do bloco)
    def __repr__(self):
        return f"{'Livre' if self.is_free else f'Ocupado: {self.value}'}" # String com as informações do bloco

# Classe para gerenciar a memória, ou seja, realizar a alocação e desalocação dos blocos propriamente dita
class MemoryManager:

    # Construtor da classe, ele é chamado quando um novo objeto "MemoryManager" é criado
    def __init__(self, total_blocks=50): # Simulando uma memória com apenas 50 blocos
        self.blocks = [MemoryBlock() for _ in range(total_blocks)] # Criando os blocos da memória de acordo com a quantidade recebida

    # Metodo para alocacar um arquivo na memória de acordo com o tipo de alocaçãoo (o padrão é alocacao contígua)
    def allocate(self, file, allocation_type='contiguous'):
        needed_blocks = file['size'] # Determina a quantidade de blocos necessários de acordo com o tamanho do arquivo

        # Verificando o tipo de alocação
        if allocation_type == 'contiguous': # Caso seja alocação contígua
            return self.allocate_contiguous(file, needed_blocks)
        elif allocation_type == 'linked': # Caso seja alocação encadeada
            return self.allocate_linked(file, needed_blocks)
        else: # Caso receba algum tipo desconhecido de alocação
            print("Error: Tipo de alocacao desconhecido. ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            return None

    # Método que realiza a alocação contígua de blocos na memória
    def allocate_contiguous(self, file, needed_blocks):

        # Incializando o index do primeiro bloco como -1 (número que nao consta nos índices dos blocos)
        start_index = -1

        # Pesquisando pela sequência de blocos livres que possam acomodar o tamanho solicitado
        for i in range(len(self.blocks) - needed_blocks + 1):

            # Caso encontre espaço suficiente para alocação do arquivo, atribui o index do primeiro bloco nas sua instância
            if all(self.blocks[j].is_free for j in range(i, i + needed_blocks)) :
                start_index = i
                break

        # Caso acabe o looping e o index inicial continue como -1 sigifica que nâo foi encontrado espaço para alocar o arquivo
        if start_index == -1:

            # Retorno do erro que não encontrou-se espaço
            print("Error: Nao ha memoria livre suficiente para alocar o arquivo. ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            return None

        # Marcar cada bloco encontrado para armazenamento com o nome do arquivo que está armazenado nele
        for i in range(start_index, start_index + needed_blocks):
            self.blocks[i].allocate(file['name'])

        # O método retorna o index do primeiro bloco que armazena o arquivo
        return start_index

    # Método que realiza a alocação encadeada de blocos na memória
    def allocate_linked(self, file, needed_blocks):
        allocated_indices = [] # Incializando a lista que armazena os índices alocados
        count = 0 # Inicializando a variável contadora

        # Pesquisando pela quantidade de blocos necessários livres na memória (Podem nao estar em sequência)
        for i in range(len(self.blocks)):
            if self.blocks[i].is_free: # Verificando se o bloco está livre
                self.blocks[i].allocate(file['name']) # Alocando cada bloco para o arquivo em questão
                allocated_indices.append(i) # Armazenando os índices dos blocos na lista
                count += 1 # Incrementando o contador
                if count == needed_blocks: # Caso o contador atinja o mesmo valor que a quantidade de blocos necessários, termina o looping pois o arquivo já foi todo armazenado
                    break

        # Caso o arquivo não tenha sido totalmente armazenado, ou seja, o contador não seja menor que a quantidade de blocos necessários
        if count < needed_blocks:
            print("Error: Nao ha memoria suficiente para alocar. ", datetime.now().strftime("%Y-%m-%d %H:%M:%S")) # Retorna o a mensagem de erro que nao tem memoria suficiente para alocar o arquivo

            # Looping para fazer a desalocação dos blocos que haviam sido alocados
            for index in allocated_indices:
                self.blocks[index].deallocate() # Desalocando cada bloco
            return None

        # Linkando cada bloco alocado um com o outro
        for i in range(len(allocated_indices) - 1):
            self.blocks[allocated_indices[i]].next_block = allocated_indices[i + 1] # Atribuindo o índice do próximo bloco ao 'next_block' do bloco atual

        return allocated_indices[0] # Retornando o índice do primeiro bloco alocado para o arquivo

    # Método que desaloca o arquivo da memória
    def deallocate(self, start_index, size, allocation_type='contiguous'):

        # Verificando se a alocação é contígua
        if allocation_type == 'contiguous':

            # Percorrendo os blocos a partir do 'start_index' e desalocando até o último bloco
            for i in range(start_index, start_index + size):
                if i < len(self.blocks):
                    self.blocks[i].deallocate()

        # Verificando se a alocação é encadeada
        elif allocation_type == 'linked':

            # Iniciando a variável que armazena o index atual (current_index), recebendo o index inicial (start_index)
            current_index = start_index

            # Lopping que percorre os blocos encadeados e desaloca eles ate o ultimo bloco (Verifica se o tamanho do arquivo eh maior que 0)
            while current_index is not None and size > 0:
                next_index = self.blocks[current_index].next_block # Setando a variavel 'next_index' com o index do proximo bloco a ser analisado
                self.blocks[current_index].deallocate() # Desalocando o bloco atual
                current_index = next_index # Setando o index do bloco atual (proximo bloxo a ser desalocado) com o 'next_index'
                size -= 1 # Decrementando o tamanho do arquivo a cada bloco removido

    # Metodo para mostar o estado da memoria
    def display_memory(self):
        memory_info = "------------------------------------\n\nMEMORIA \n\n"
        for i, block in enumerate(self.blocks):
            memory_info  += f"Bloco {i}: {block}\n"
        memory_info += "\n--------------------------------------"
        return memory_info
        