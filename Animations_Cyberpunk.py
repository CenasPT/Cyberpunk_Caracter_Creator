import os # Used to clear the console (screen)
import time # Used in the animated title function (and in the stop() function of the main)
from colorama import Fore, Style # Modifies the color and style of the text

# Function to get the terminal size
def obtain_terminal_size():
    try:
        columns, rows = os.get_terminal_size(0) # Gets the terminal size, a tuple of two values, height and width
    except OSError:
        columns, rows = os.get_terminal_size(1) # If there is any error, the size reverts to the original.
    return columns

# Function to center the text
def center_text(text):
    columns = obtain_terminal_size() # Gets the width of the terminal
    string_list = text.split('\n') # If the text contains "\n", we split it to form a list of strings
    centered_rows = [] # List to accumulate the centered rows
    for string in string_list: # for loop applies the .center() method to each of the strings in the list
        centered_line = string.strip().center(columns) # Removes whitespace before and after the string, and the .center(columns) method centers the string within the specified space (columns), adding spaces to the right and left.
        centered_rows.append(centered_line) # Adds the centered line to the list
    centered_text = '\n'.join(centered_rows) # .join() rejoins the strings using "\n" as the separator   
    return centered_text

# Animated title for the main menu
def animated_title():
        os.system('cls')        
        cyberpunk_art1 = """
|         _-_-_-_     _-_-_-  _-_-_- _-_-_  _-_-_  -    _ _   - _  __|
/ ____\ \   / /  _ \|  ____|   __ \|  __ \| |  | | \ | | |/ /
        | |    \ \_/ /| |_) | |__  | |_) | |__) | |  ||  \| | '/ 
| |     \   / |  _ <| __| |  _  /|  ___/| |  | | . ` |  <  
      | |____  | |  | |_) | |____| | \ \| |    | |__| | |\  | . \ 
\_-_-_|  |_| |_-__/|_ -_-_-|_|  \_\_|    \_-_-/|-| \_|_|\_\ 
                                                                
                             ̅ ̅    N  D                           
"""
        print(Fore.GREEN+center_text(cyberpunk_art1))
        time.sleep(0.1) 
        os.system('cls')
        cyberpunk_art2 = """
|       _-_-_-_     _-_-_-  _-_-_- _-_-_  _-_-_  -    _ _   - _  __  |
|/ ____\ \   / /  _ \|  ____|  __ \|  __ \| |  | | \ | | |/ /        |
       | |    \ \_/ /| |_) | |__  | |__) | |__) | |  | |  \| | ' / 
 | |     \   / |  _ <|  __| |  _  /|  ___/| |  | | . ` |  <  
       | |____  | |  | |_) | |____| | \ \| |    | |__| | |\  | . \ 
\_-_-_|  |_|  |_-__/|_-_-_-|_|  \_\_|     \_-_-/|-| \_|_|\_\ 
                                                                
                           E̅C̅   M̅ E̅ ̅A ̅LE̅   D̅                           
"""
        print(Fore.GREEN+center_text(cyberpunk_art2))
        time.sleep(0.1)        
        os.system('cls')
        cyberpunk_art3 = """
|      _-___-_     ___-__  ____-_ __-_-  __-__  _    _ _   _ _  __   |
|/ ____\ \   / /  _ \|  ____|  __ \|  __ \| |  | | \ | | |/ /        |
|     | |    \ \_/ /| |_) | |__  | |__) | |__) | |  | |  \| | ' /    |
  | |     \   / |  _ <|  __| |  _  /|  ___/| |  | | . ` |  <  
      | |____  | |  | |_) | |____| | \ \| |    | |__| | |\  | . \ 
 \_-___|  |_|  |__-_/|-_-_-_|_|  \_\_|     \-_-_/|_| \_|_|\_\ 
                                                                
                           B̅E̅  O̅ M ̅A̅ ̅L E̅G̅  D̅                           
"""
        print(Fore.GREEN+center_text(cyberpunk_art3))
        time.sleep(0.1)
        os.system('cls')
        cyberpunk_art4 = """
|     _______     ______  ______ _____  _____  _    _ _   _ _  __    |
|  / ____\ \   / /  _ \|  ____|  __ \|  __ \| |  | | \ | | |/ /      |
|     | |    \ \_/ /| |_) | |__  | |__) | |__) | |  | |  \| | ' /    |
|   | |     \   / |  _ <|  __| |  _  /|  ___/| |  | | . ` |  <       |
     | |____  | |  | |_) | |____| | \ \| |    | |__| | |\  | . \ 
  \_____|  |_|  |____/|______|_|  \_\_|     \____/|_| \_|_|\_\ 

                           B̅E O̅ E̅ ̅A̅ ̅LE̅ EN̅                           
"""
        print(Fore.GREEN+center_text(cyberpunk_art4))
        time.sleep(0.1)
        os.system('cls')
        cyberpunk_art5 = """
|     _______     ______  ______ _____  _____  _    _ _   _ _  __    |
|    / ____\ \   / /  _ \|  ____|  __ \|  __ \| |  | | \ | | |/ /    |
|    | |    \ \_/ /| |_) | |__  | |__) | |__) | |  | |  \| | ' /     |
|    | |     \   / |  _ <|  __| |  _  /|  ___/| |  | | . ` |  <      |
|    | |____  | |  | |_) | |____| | \ \| |    | |__| | |\  | . \     |
|    \_____|  |_|  |____/|______|_|  \_\_|     \____/|_| \_|_|\_\    |
|                                                                    |
                           B̅E̅C̅O̅M̅E̅ ̅A̅ ̅L̅E̅G̅E̅N̅D̅                           
"""
        print(Fore.GREEN+Style.BRIGHT+center_text(cyberpunk_art5)+Style.RESET_ALL)
        time.sleep(0.5)

# Animated title displayed after character creation
def animated_character_created_text():
        os.system('cls')
        cyberpunk_art ="""
             _      _    _          _             _   _                  
            | \  _   \         |    _| __   _  \   |
       |                  |_) |                  | |_) |     |
  |                      / __        |  _ <      |
            _         _    _    _/    _        \_|     |    
          /        _ \|    _   _|      _ \      
|                                            _| |          
               | |_|  _        /             __| |_|             |
                                  __     _              
"""
        print(Fore.GREEN+center_text(cyberpunk_art))
        time.sleep(0.1) 
        os.system('cls')
        cyberpunk_art1 ="""
        ____ _      _    _    ____      _    ___  _____ ____       |
        /      | \  _   \  / \    |    _| __   _  \   |
       |                  |_) |  / _ \|          | |_) |     |
  |         |    | __ \      / __        |  _ <      |
   |            _         _    _    _/    _        \_|     |    
          /        _ \|    _   _|      _ \      
|                               /    _ \ | | |  _| |          |
               | |_|  _        /             __| |_|             |
    |                \__ \_   /_       __     _              |
"""
        print(Fore.GREEN+center_text(cyberpunk_art1))
        time.sleep(0.1) 
        os.system('cls')
        cyberpunk_art2 ="""
        ____ _      _    _    ____      _    ___  _____ ____       |
        / ___| | \  _   \  / \  __|    _| __   _  \   |
       |                  |_) |  / _ \|      | | | |_) |     |
  |         |    | __ \      / __     _ _|  _ <      |
   |        \____         _    _    _/_  \_  \_|_| \_|     |    
          / ___  | _ \| _\|_   _|      _ \      
|                          _|   /    _ \ | | |  _| |          |
               | |_|  _ <| |___ /           |___| |_|             |
    |                \__ \_\__/_       ____|___              |
"""
        print(Fore.GREEN+center_text(cyberpunk_art2))
        time.sleep(0.1)        
        os.system('cls')
        cyberpunk_art3 ="""
|         ____ _   _    _    ____      _    ___    _ _____ ____       |
   |        / ___| | \  _ \  / \  __|_   _| __   _  \   |
       | | |    | / _ \ | |_) |  / _ \| |      | | |  _| | |_) |     |
  |         |    | __ \      / __ |___  | | | _ _|  _ <      |
   |        \____  |_| |_/_/___\_ _|_\_|/_/_  \_  \____|_|_|_|_____|_| \_|     |    
          / ___  | _ \| ____|    \|_   _| ___  _ \          |
|                  | |   |_)    _|   / _ \ | | |  _| | | | |             |
               | |_|  _ <| |___ /  ___ \| | | |___| |_|             |
    |                \__ \_\_____/_       \_\_|_____|___              |
"""
        print(Fore.GREEN+center_text(cyberpunk_art3))
        time.sleep(0.1)
        os.system('cls')
        cyberpunk_art4 ="""
|         ____ _   _    _    ____      _    ____ _____ _____ ____       |
|        / ___| | | |  \  _ \  / \  / ___|_   _| ____|  _ \   |
       | |   |     | / _ \ | |_) |  / _ \| |     | | |  _| | |_) |     |
|         |    |  _  __ \    _ <  / __ \ |___  | | | |___|  _ <      |
|        \____  |_| |_/_/___\_\_|_\_|/_/_  \_\____|_|_|_|_____|_| \_|     |    
          / ___|  _ \| ____|  / \|_   _| ___  _ \              |
|                  | |   | |_) |  _|   / _ \ | | |  _| | | | |             |
|               | |___|  _ <| |___ / ___ \| | | |___| |_| |             |
|                \__ \_\_____/_/   \_\_| |_____|___              |
"""
        print(Fore.GREEN+center_text(cyberpunk_art4))
        time.sleep(0.1)
        os.system('cls')
        cyberpunk_art5 ="""
|         ____ _   _    _    ____      _    ____ _____ _____ ____       |
|        / ___| | | |  / \  |  _ \    / \  / ___|_   _| ____|  _ \      |
|       | |   | |_| | / _ \ | |_) |  / _ \| |     | | |  _| | |_) |     |
|       | |___|  _  |/ ___ \|  _ <  / ___ \ |___  | | | |___|  _ <      |
|        \____|_| |_/_/___\_\_|_\_|/_/_  \_\____|_|_|_|_____|_| \_|     |
|                / ___|  _ \| ____|  / \|_   _| ____|  _ \              |
|               | |   | |_) |  _|   / _ \ | | |  _| | | | |             |
|               | |___|  _ <| |___ / ___ \| | | |___| |_| |             |
|                \____|_| \_\_____/_/   \_\_| |_____|____/              |
"""
        print(Fore.GREEN+Style.BRIGHT+center_text(cyberpunk_art5)+Style.RESET_ALL)
        time.sleep(0.5)