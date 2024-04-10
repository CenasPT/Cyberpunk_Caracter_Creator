import os # Utilizado para limpar a consola(ecra)
import time # Utilizado na função titulo_animado (e stop() do main)
from colorama import Fore, Style # Modifica cor e estilo do texto.

# Função para obter o tamanho do terminal
def obter_tamanho_terminal():
    try:
        colunas, linhas = os.get_terminal_size(0) # Obtem o tamanho do terminal, uma tupla de dois valores, altura e largura
    except OSError:
        colunas, linhas = os.get_terminal_size(1) # Se existir algum erro, o tamanho reverte ao original
    return colunas

# Função para centrar o texto
def centrar_texto(texto):
    colunas = obter_tamanho_terminal() # Obtem a largura do terminal
    lista_strings = texto.split('\n') # Caso o texto tenha \n dividimos o mesmo para formar uma lista de strings
    linhas_centradas = [] # Lista para acumular as linhas centralizadas
    for string in lista_strings: # for aplica o método .center() a cada uma das strings na lista
        linha_centrada = string.strip().center(colunas) # Remove espaços em branco antes e depois da string e Método .center(colunas) centraliza a string dentro do espaço indicado (colunas), adicionando espaços à direita e esquerda
        linhas_centradas.append(linha_centrada) # Adiciona a linha centralizada à lista
    texto_centralizado = '\n'.join(linhas_centradas) # .join() volta a juntar as strings utilizando o \n como separador    
    return texto_centralizado

# Titulo animado do menu principal
def titulo_animado():
        os.system('cls')
        cyberpunk_art1 = '''
|         _-_-_-_     _-_-_-  _-_-_- _-_-_  _-_-_  -    _ _   - _  __|
/ ____\ \   / /  _ \|  ____|   __ \|  __ \| |  | | \ | | |/ /
        | |    \ \_/ /| |_) | |__  | |_) | |__) | |  ||  \| | '/ 
| |     \   / |  _ <| __| |  _  /|  ___/| |  | | . ` |  <  
      | |____  | |  | |_) | |____| | \ \| |    | |__| | |\  | . \ 
\_-_-_|  |_| |_-__/|_ -_-_-|_|  \_\_|    \_-_-/|-| \_|_|\_\ 
                                                                
                             ̅ ̅    N  D                           
'''
        print(Fore.GREEN+centrar_texto(cyberpunk_art1))
        time.sleep(0.1) 
        os.system('cls')
        cyberpunk_art2 = '''
|       _-_-_-_     _-_-_-  _-_-_- _-_-_  _-_-_  -    _ _   - _  __  |
|/ ____\ \   / /  _ \|  ____|  __ \|  __ \| |  | | \ | | |/ /        |
       | |    \ \_/ /| |_) | |__  | |__) | |__) | |  | |  \| | ' / 
 | |     \   / |  _ <|  __| |  _  /|  ___/| |  | | . ` |  <  
       | |____  | |  | |_) | |____| | \ \| |    | |__| | |\  | . \ 
\_-_-_|  |_|  |_-__/|_-_-_-|_|  \_\_|     \_-_-/|-| \_|_|\_\ 
                                                                
                           E̅C̅   M̅ E̅ ̅A ̅LE̅   D̅                           
'''
        print(Fore.GREEN+centrar_texto(cyberpunk_art2))
        time.sleep(0.1)        
        os.system('cls')
        cyberpunk_art3 = '''
|      _-___-_     ___-__  ____-_ __-_-  __-__  _    _ _   _ _  __   |
|/ ____\ \   / /  _ \|  ____|  __ \|  __ \| |  | | \ | | |/ /        |
|     | |    \ \_/ /| |_) | |__  | |__) | |__) | |  | |  \| | ' /    |
  | |     \   / |  _ <|  __| |  _  /|  ___/| |  | | . ` |  <  
      | |____  | |  | |_) | |____| | \ \| |    | |__| | |\  | . \ 
 \_-___|  |_|  |__-_/|-_-_-_|_|  \_\_|     \-_-_/|_| \_|_|\_\ 
                                                                
                           B̅E̅  O̅ M ̅A̅ ̅L E̅G̅  D̅                           
'''
        print(Fore.GREEN+centrar_texto(cyberpunk_art3))
        time.sleep(0.1)
        os.system('cls')
        cyberpunk_art4 = '''
|     _______     ______  ______ _____  _____  _    _ _   _ _  __    |
|  / ____\ \   / /  _ \|  ____|  __ \|  __ \| |  | | \ | | |/ /      |
|     | |    \ \_/ /| |_) | |__  | |__) | |__) | |  | |  \| | ' /    |
|   | |     \   / |  _ <|  __| |  _  /|  ___/| |  | | . ` |  <       |
     | |____  | |  | |_) | |____| | \ \| |    | |__| | |\  | . \ 
  \_____|  |_|  |____/|______|_|  \_\_|     \____/|_| \_|_|\_\ 

                           B̅E O̅ E̅ ̅A̅ ̅LE̅ EN̅                           
'''
        print(Fore.GREEN+centrar_texto(cyberpunk_art4))
        time.sleep(0.1)
        os.system('cls')
        cyberpunk_art5 = '''
|     _______     ______  ______ _____  _____  _    _ _   _ _  __    |
|    / ____\ \   / /  _ \|  ____|  __ \|  __ \| |  | | \ | | |/ /    |
|    | |    \ \_/ /| |_) | |__  | |__) | |__) | |  | |  \| | ' /     |
|    | |     \   / |  _ <|  __| |  _  /|  ___/| |  | | . ` |  <      |
|    | |____  | |  | |_) | |____| | \ \| |    | |__| | |\  | . \     |
|    \_____|  |_|  |____/|______|_|  \_\_|     \____/|_| \_|_|\_\    |
|                                                                    |
                           B̅E̅C̅O̅M̅E̅ ̅A̅ ̅L̅E̅G̅E̅N̅D̅                           
'''
        print(Fore.GREEN+Style.BRIGHT+centrar_texto(cyberpunk_art5)+Style.RESET_ALL)
        time.sleep(0.5)

# Titulo animado exibido após criação de personagem
def texto_personagem_criado_animado():
        os.system('cls')
        cyberpunk_art ='''
  _                     _              _                                           _                _    
                     \       /              /          |             |    /   __  __            /      \        
        |     |           _                     _  _       |                 |                 |   |     
      _               \                       \      |                            /                           |
           _     |    _       _   |                          |          |  _     |           /    _                
  _                                    _      _       |               \               _                               
'''
        print(Fore.GREEN+centrar_texto(cyberpunk_art))
        time.sleep(0.1) 
        os.system('cls')
        cyberpunk_art1 ='''
  _                     _      _     _   _          __    _          __          _ _   _  _   _          __      ____  
     _               \ /      / __    \      /    /     |             |    /   __|  __       _|   /\   |  __ \        
        | |    |           _ |      |        /  \ | |   _| |_   | \  / |                 |  |               |   |     
 |  _ _    _           \          |           /  \       |  __    |\ |            |  _  /               |           | |
   |       _     |   \ _   ) | |_   |                      |_   |      |   |  _     |           /    _                |
  _          _         _ _ _/ \_     _| \_/_/     _\ _  _|_   __  |  | |    \_           \               ___     _                          
'''
        print(Fore.GREEN+centrar_texto(cyberpunk_art1))
        time.sleep(0.1) 
        os.system('cls')
        cyberpunk_art2 ='''
  _   _  _   __ _       _      _     _   _          __    _      __  __      ___ _ _   _  _   _          __      ____  
 |   _ \|            \ / _ __|/ __ \| \      /\   / ____|         \   |    /   __|  __ \|_   _|   /\   |  __ \        
   | _) | |    |    ) |    _ | |    |        /  \ | |   _| |_   | \  / |            |__) | | |    /  \       | | |     
 |  _ _    _           \          |           /  \       |  __|   |\ |            |  _  /               |           | |
   |       _   | |   \ _   ) | |_   |                      |_   |      |   |  _     |     _| |_ /    _ \| |    |      |
  _     |_   _         _ _ _/ \_     _| \_/_/     _\__  _|_   __|_|  | |    \_     _|  \_\__   /_/    \_\___    \_                          
'''
        print(Fore.GREEN+centrar_texto(cyberpunk_art2))
        time.sleep(0.1)        
        os.system('cls')
        cyberpunk_art3 ='''
  _   _  _   __ _       _      _     _   _          __    _      __  __      ___ _ _   _  _   _          __      ____  
 |   _ \|     _|  __ \ / _ __|/ __ \| \      /\   / ____|         \   |    /   __|  __ \|_   _|   /\   |  __ \        
   | _) | |    |    ) |    _ | |    |        /  \ | |   _| |_   | \  / |            |__) | | |    /  \       | | |     
 |  _ _    _   |  _    \          |   . ` | / /  \| | |_ |  __|   |\ | |   | |    |  _  /  | |      \ \ |      |    | |
   |    | |_   | |   \ _   ) | |_   |             \ |__|   |_   |      |   |  _     | \ \ _| |_ /    _ \| |    |      |
  _     |_   _      \_\_ _ _/ \_  _/|_| \_/_/     _\__  _|_   __|_|  |_|    \_  __|_|  \_\__   /_/    \_\___    \_                          
'''
        print(Fore.GREEN+centrar_texto(cyberpunk_art3))
        time.sleep(0.1)
        os.system('cls')
        cyberpunk_art4 ='''
  _   _  _   __ _       _      ____  _   _          __    _      __  __      ___ _ _   _  _   _          __      ____  
 |  __ \|  ____|  __ \ / _ __|/ __ \| \ | |   /\   / ____|         \   |    /   __|  __ \|_   _|   /\   |  __ \ / __ \ 
 | | _) | |__  | | _) | (___ | |  | |  \| |  /  \ | |   _| |_   | \  / |            |__) | | |    /  \  | |  | | |  | |
 |  _ _/|  _   |  _    \  _ \|    |   . ` | / /  \| | |_ |  __|   |\ | |   | |    |  _  /  | |   / /\ \ |      |    | |
 | |    | |_   | |   \ ____) | |__| | |\          \ |__|   |____|    | |   |  ____| | \ \ _| |_ / ____ \| |__| | |__| |
 |_|    |_   _      \_\_ _ _/ \_  _/|_| \_/_/     _\__  _|_   __|_|  |_|    \_  __|_|  \_\__   /_/    \_\___    \_                          
'''
        print(Fore.GREEN+centrar_texto(cyberpunk_art4))
        time.sleep(0.1)
        os.system('cls')
        cyberpunk_art5 ='''
  _____  ______ _____   _____  ____  _   _          _____ ______ __  __      _____ _____  _____          _____   ____  
 |  __ \|  ____|  __ \ / ____|/ __ \| \ | |   /\   / ____|  ____|  \/  |    / ____|  __ \|_   _|   /\   |  __ \ / __ \ 
 | |__) | |__  | |__) | (___ | |  | |  \| |  /  \ | |  __| |__  | \  / |   | |    | |__) | | |    /  \  | |  | | |  | |
 |  ___/|  __| |  _  / \___ \| |  | | . ` | / /\ \| | |_ |  __| | |\/| |   | |    |  _  /  | |   / /\ \ | |  | | |  | |
 | |    | |____| | \ \ ____) | |__| | |\  |/ ____ \ |__| | |____| |  | |   | |____| | \ \ _| |_ / ____ \| |__| | |__| |
 |_|    |______|_|  \_\_____/ \____/|_| \_/_/    \_\_____|______|_|  |_|    \_____|_|  \_\_____/_/    \_\_____/ \____/                      
'''
        print(Fore.GREEN+Style.BRIGHT+centrar_texto(cyberpunk_art5)+Style.RESET_ALL)
        time.sleep(0.5)