# Emulated File System

This project was developed for the Operating Systems course (P3). The "File Manager" system emulates a computer's file system, including memory management.

## Features
- Creation and deletion of files and directories.
- Writing and reading data in files.
- Hierarchical directory structure.
- Memory space management for file storage.
- Graphical user interface for interacting with the system.
- Simulation of a basic file system with typical file manipulation operations.

## Libraries Used
- datetime: Date and time manipulation.
- tkinter: Graphical user interface.
- customtkinter: Custom components for tkinter.
- PIL (Pillow): Image manipulation.
- anytree: Creation and manipulation of trees.
- os: Interaction with the operating system.
- math: Mathematical functions.

## Project Structure
FileManagerSystem/  
├── images/  
├── auth.py  
├── README.md  
├── interface_logged.py  
├── interface_login.py  
├── main.py  
├── menagement_diretory.py  
├── menagement_logged.py  
├── menagement_memory.py  
└── requirements.txt/  

- `images/`: Folder containing image assets.
- `auth.py`: Handles authentication-related functionalities.
- `README.md`: Project documentation.
- `interface_logged.py`: Implementation of the logged-in user interface.
- `interface_login.py`: Implementation of the login interface.
- `main.py`: Entry point of the system.
- `menagement_directory.py`: Implementation of directory management functionalities.
- `menagement_logged.py`: Implementation of logged-in user management functionalities.
- `menagement_memory.py`: Implementation of memory management functionalities.
- `requirements.txt`: List of project dependencies.

## Installation
1. Clone the repository:

- Copy code at terminal: `git clone https://github.com/lucasmcmatos/emulated-file-system.git`
- Copy code at terminal: `cd emulated-file-system`

2. Create and activate a virtual environment:

- Copy code at terminal: `python -m venv venv`
- Copy code at terminal: `venv\Scripts\activate` (Windows)

3. Install the dependencies:

- Copy code at terminal: `pip install -r requirements.txt`

## Usage
To start the system, run the main.py file:

- Copy code at terminal: `python main.py`

## License

Reconhecimentos e Direitos Autorais @autor: ANTONIO LUCAS DA SILVA VALE, JOSE NUNES DE SOUSA NETO, LUCAS MARTINS CAMPOS MATOS, LUCKA PEREIRA DE LIMA, SAVIO RODRIGUES JEREMIAS DE SOUSA @data última versão: 30/05/2024 @versão: 1.0 @Agradecimentos: Universidade Federal do Maranhão (UFMA), Professor Doutor Thales Levi Azevedo Valente, e colegas de curso. @Copyright/License Este material é resultado de um trabalho acadêmico para a disciplina SISTEMAS_OPERACIONAIS, sobre a orientação do professor Dr. THALES LEVI AZEVEDO VALENTE, semestre letivo 2024.1, curso Engenharia da Computação, na Universidade Federal do Maranhão (UFMA). Todo o material sob esta licença é software livre: pode ser usado para fins acadêmicos e comerciais sem nenhum custo. Não há papelada, nem royalties, nem restrições de "copyleft" do tipo GNU. Ele é licenciado sob os termos da licença MIT reproduzida abaixo e, portanto, é compatível com GPL e também se qualifica como software de código aberto. É de domínio público. Os detalhes legais estão abaixo. O espírito desta licença é que você é livre para usar este material para qualquer finalidade, sem nenhum custo. O único requisito é que, se você usá-los, nos dê crédito. Copyright © 2024 Educational Material Este material está licenciado sob a Licença MIT. É permitido o uso, cópia, modificação, e distribuição deste material para qualquer fim, desde que acompanhado deste aviso de direitos autorais. O MATERIAL É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU IMPLÍCITA, INCLUINDO, MAS NÃO SE LIMITANDO ÀS GARANTIAS DE COMERCIALIZAÇÃO, ADEQUAÇÃO A UM DETERMINADO FIM E NÃO VIOLAÇÃO. EM HIPÓTESE ALGUMA OS AUTORES OU DETENTORES DE DIREITOS AUTORAIS SERÃO RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTRA RESPONSABILIDADE, SEJA EM UMA AÇÃO DE CONTRATO, ATO ILÍCITO OU DE OUTRA FORMA, DECORRENTE DE, OU EM CONEXÃO COM O MATERIAL OU O USO OU OUTRAS NEGOCIAÇÕES NO MATERIAL. Para mais informações sobre a Licença MIT: A tecnologia não é nada. O que é importante é que você tenha fé de que as pessoas sejam basicamente boas e inteligentes. Se você lhes fornecer ferramentas, elas farão coisas maravilhosas..

