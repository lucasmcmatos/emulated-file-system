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
    ├── AJLLS.png  
    ├── ajllslogo.ico  
    └── ajllslogo.png  
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

- Copy code at terminal: `git clone https://github.com/yourusername/Emulated File System.git`
- Copy code at terminal: `cd Emulated File System`

2. Create and activate a virtual environment:

- Copy code at terminal: `python -m venv venv`
- Copy code at terminal: `venv\Scripts\activate` (Windows)

3. Install the dependencies:

- Copy code at terminal: `pip install -r requirements.txt`

## Usage
To start the system, run the main.py file:

- Copy code at terminal: `python main.py`

## License

