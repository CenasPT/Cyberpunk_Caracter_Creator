import random  # Used to randomly define the levels of characters.
import pygame  # Utilized in the functions play_music and stop_music
import pandas as pd  # Reading and writing csv files and creating dataframes
from InquirerPy import inquirer, get_style  # Allows the user to choose menu options using only the keyboard arrows
from Classes_Cyberpunk import *  # Imports classes from another file
from Animations_Cyberpunk import *  # Imports animation file for the project
from Lore_Cyberpunk import *  # Information about the Cyberpunk universe
from Characters_Cyberpunk import *  # Predefined characters for the project
from Universe_Cyberpunk import *  # Access the cyberpunk_universe function and other necessary functions for it

def stop():
    """
    To pause the program for 3 seconds
    """
    for i in range(3,0,-1):
        print(f"{i}...", end=' ',flush=True) # end forces the print to end with a space instead of \n, and flush clears the buffer.
        time.sleep(1)

# Play music
def play_music(music_file):
    music_path = os.path.join(os.path.dirname(__file__), music_file)
    pygame.mixer.init() # Initialize the mixer
    pygame.mixer.music.load(music_path) # Fetches the music according to the provided path
    pygame.mixer.music.play(loops=-1, fade_ms=10000) # Start playing, repeat infinitely, gradually increase volume over 10 seconds

# Stop the music currently playing
def stop_music():
    pygame.mixer.music.fadeout(3000) # Gradually decrease the volume of the music until it stops completely

# Implementation of a choice menu (using the keyboard), takes lists as input and returns the user's choice
def menu_choices(choice,message):
    style = get_style({"question": "bold lightblue"}, style_override=False) # Change the color of the message
    # Exibe o menu utilizando inquirerPY e devolve (return) a choice
    return inquirer.select(
        style=style, # Implement color change
        message=message, # Message or question displayed before the menu      
        choices=choice, # List of choices available to the user
        qmark="", # Symbol "?" that appears before the message.
        amark="", # Symbol that appears before the response when it becomes visible on the screen
        show_cursor=False, # Don't show the cursor in the terminal
        transformer=lambda result:"", # Do not display the option selected by the user on the screen after it has been selected
        border=True, # Display border around the menu
        max_height=100 # Height of the menu (this option is dynamic)
    ).execute()

# Receives a CSV file and returns a dataframe
# Create CSV file if it doesn't exist
def load_dataframe(file):    
    header = ['                Name','|  Initial Level','|   Maximum Level','|       Occupation','|    Gang/Pack','|       Cybernetic Implant','Additional Information']   
    # Confirm if the file exists
    try:
        # Try to read the CSV file
        dataframe=pd.read_csv(file,encoding='utf-8')                
    except FileNotFoundError:        
        # Create a new DataFrame if the file does not exist        
        dataframe=pd.DataFrame(columns=header)
        dataframe.to_csv(file, encoding='utf-8',index=False)
        insert_data_file(Johnny.name,Johnny.initial_level,Johnny.max_level,Johnny.occupation,Johnny.gang,Johnny.cybernetic_implant,Johnny.additional_info) 
        insert_data_file(Morgan.name,Morgan.initial_level,Morgan.max_level,Morgan.occupation,Morgan.gang,Morgan.cybernetic_implant,Morgan.additional_info)
        insert_data_file(Alt.name,Alt.initial_level,Alt.max_level,Alt.occupation,Alt.gang,Alt.cybernetic_implant,Alt.additional_info) 
        insert_data_file(Saburo.name,Saburo.initial_level,Saburo.max_level,Saburo.occupation,Saburo.gang,Saburo.cybernetic_implant,Saburo.additional_info) 
        insert_data_file(Smasher.name,Smasher.initial_level,Smasher.max_level,Smasher.occupation,Smasher.gang,Smasher.cybernetic_implant,Smasher.additional_info) 
        insert_data_file(Rogue.name,Rogue.initial_level,Rogue.max_level,Rogue.occupation,Rogue.gang,Rogue.cybernetic_implant,Rogue.additional_info) 
        insert_data_file(Bartmoss.name,Bartmoss.initial_level,Bartmoss.max_level,Bartmoss.occupation,Bartmoss.gang,Bartmoss.cybernetic_implant,Bartmoss.additional_info) 
        dataframe=pd.read_csv(file,encoding='utf-8') 
    return dataframe

# Receives a dataframe, text1, and text2
# Display text1, text2, and all data from this dataframe except the last column
def display_limited_dataframe(dataframe,text1,text2):
    print(Fore.BLUE+Style.BRIGHT+center_text(text1)+Style.RESET_ALL)
    print(Fore.BLUE+Style.BRIGHT+center_text(text2)+Style.RESET_ALL)
    limited_dataframe=dataframe[['                Name','|  Initial Level','|   Maximum Level','|       Occupation','|    Gang/Pack','|       Cybernetic Implant']] # Cuts last column (Additional Information)
    print(Fore.GREEN+Style.BRIGHT+limited_dataframe.to_string(index=False)+Style.RESET_ALL+"\n")

# Insert data into the CSV file (constant variable)
def insert_data_file(name,initial_lvl,max_lvl,occupation,gang_pack,implant,additional_info):
    CSV_FILE = 'CyberChar.csv'
    dataframe = load_dataframe(CSV_FILE)           
    # Introduction of new data into the DataFrame              
    new_line = {'                Name':name,'|  Initial Level':initial_lvl,'|   Maximum Level':max_lvl,'|       Occupation':occupation,'|    Gang/Pack':gang_pack,'|       Cybernetic Implant':implant,'Additional Information':additional_info}
    dataframe.loc[len(dataframe)] = new_line    
    # Write New Data to File
    dataframe.to_csv(CSV_FILE, encoding='utf-8',index=False)

# Character Creation
def create_character():  
    # Generate and assign random numbers for character levels
    initial_lvl = random.randint(1,10)
    max_lvl = random.randint(15,20) 
    # Mandatory initialization of a variable that will be used later on
    option = ""
    # Load CSV file to then extract the names of the characters
    CSV_FILE = 'CyberChar.csv' 
    dataframe = load_dataframe(CSV_FILE)
    # Save all the names present in the CSV file into a list (in lowercase characters)
    names_list = dataframe['                Name'].str.lower().values 
    # Define the name of the character
    while(True):
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+center_text("\nCREATE NEW CHARACTER")+Style.RESET_ALL)
        print(Fore.BLUE+Style.BRIGHT+center_text("Type 'cancel' or press 'Enter' with a blank name to go back to the Main Menu\n")+Style.RESET_ALL)
        if option == "invalid":                                        
            print(Fore.RED+Style.BRIGHT+center_text("Error when typing name")+Style.RESET_ALL) 
        elif option == "exists":                                        
            print(Fore.RED+Style.BRIGHT+center_text("Name already exists")+Style.RESET_ALL) 
        try:       
            name=(input("Enter the character's name (up to 15 characters): ").strip()) # .strip() removes whitespace at the beginning and end of the string
        except ValueError:
            pass 
        if name.strip().lower() == "cancel" or name.strip().lower() == '':
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nCREATE NEW CHARACTER")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+center_text("Type 'cancel' or press 'Enter' with a blank name to go back to the Main Menu\n")+Style.RESET_ALL)
            print("Operation Cancelled. Going back to the main menu.")
            stop()
            return
        elif name.strip().lower() in names_list:
            option = "exists"
        elif len(name) <= 15 and name.lower() not in names_list: # Check if the string has less than 16 characters and if the name is not repeated
            break                     
        else:
            option = "invalid" 
    # Define the character's occupation 
    while(True):        
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+center_text("\nCHARACTER'S OCCUPATION")+Style.RESET_ALL)
        print(Fore.BLUE+Style.BRIGHT+center_text("Option 'cancel' returns to the main menu\n")+Style.RESET_ALL)
        # List containing menu options
        choices = [            
        "Corpo",
        "Rockerboy",
        "Gangster",
        "Cop",
        "Solo",
        "Netrunner",
        "Techie",
        "Media",
        "Fixer",
        "Nomad",
        "Undefined",
        "Info about Occupations/Roles",
        "Cancel"
        ]
        # Display the menu using the menu_choices() function
        occupation = menu_choices(choices,"Choose the occupation / role in society:")
        if occupation == "Cancel":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nCHARACTER'S OCCUPATION")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+center_text("Option 'cancel' returns to the main menu\n")+Style.RESET_ALL) 
            print("Operation Cancelled. Going back to the main menu.")
            stop()
            return 
        elif occupation == "Corpo":        
            character = Corpo(name,initial_lvl,max_lvl)
            break
        elif occupation == "Rockerboy":        
            character = Rockerboy(name,initial_lvl,max_lvl)
            break
        elif occupation == "Gangster":
            # Choose the gang that the gangster character belongs to
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nCHARACTER'S GANG")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+center_text("Option 'cancel' returns to the main menu\n")+Style.RESET_ALL)
            choices = [            
            "Maelstrom",
            "Valentinos",
            "6th Street",
            "VooDoo Boys",
            "Animals",
            "Tyger Claws",
            "Moxes",
            "Scavengers",
            "Barguest",
            "Undefined",
            "Info about Gangs",
            "Cancel"
            ]
            gang = menu_choices(choices,"Choose the gang:")
            if gang == "Cancel":
                os.system('cls')
                print(Fore.BLUE+Style.BRIGHT+center_text("\nCHARACTER'S GANG")+Style.RESET_ALL)
                print(Fore.BLUE+Style.BRIGHT+center_text("Option 'cancel' returns to the main menu\n")+Style.RESET_ALL)
                print("Operation Cancelled. Going back to the main menu.")
                stop()
                return 
            elif gang == "Undefined":
                gang = "-"
                character = Gangster(name,initial_lvl,max_lvl,gang) 
                break
            elif gang == "Info about Gangs":
                result = info_gangs("Create_Character")
                if result == "continue":
                    continue
                elif result == "menu":                    
                    return                          
            else:                             
                character = Gangster(name,initial_lvl,max_lvl,gang) 
                break
        elif occupation == "Cop":        
            character = Cop(name,initial_lvl,max_lvl)
            break
        elif occupation == "Solo":        
            character = Solo(name,initial_lvl,max_lvl)
            break
        elif occupation == "Netrunner":        
            character = Netrunner(name,initial_lvl,max_lvl)
            break
        elif occupation == "Techie":        
            character = Techie(name,initial_lvl,max_lvl)
            break
        elif occupation == "Media":        
            character = Media(name,initial_lvl,max_lvl)
            break
        elif occupation == "Fixer":        
            character = Fixer(name,initial_lvl,max_lvl)
            break
        elif occupation == "Nomad":
            # Choose the pack that the nomad character belongs to
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nCHARACTER'S PACK")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+center_text("Option 'cancel' returns to the main menu\n")+Style.RESET_ALL)
            choices = [            
            "Wraiths",
            "Aldecaldos",
            "Undefined",
            "Info about Packs",
            "Cancel"
            ]
            pack = menu_choices(choices,"Choose the nomad pack:")
            if pack == "Cancel":
                os.system('cls')
                print(Fore.BLUE+Style.BRIGHT+center_text("\nCHARACTER'S PACK")+Style.RESET_ALL)
                print(Fore.BLUE+Style.BRIGHT+center_text("Option 'cancel' returns to the main menu\n")+Style.RESET_ALL) 
                print("Operation Cancelled. Going back to the main menu.")
                stop()
                return
            elif pack == "Undefined":
                pack = "-"
                character = Nomad(name,initial_lvl,max_lvl,pack)
                break
            elif pack == "Info about Packs":
                result = info_nomad_packs("Create_Character")
                if result == "continue":
                    continue
                elif result == "menu":
                    return 
            else:     
                character = Nomad(name,initial_lvl,max_lvl,pack)
                break
        elif occupation == "Undefined":
            occupation = "-"                    
            character = Character(name,initial_lvl,max_lvl)
            break
        elif occupation == "Info about Occupations/Roles":
            result = info_occupations("Create_Character")
            if result == "continue":
                continue
            elif result == "menu":
                return  
            
    # Choose the standout cybernetic implant
    while(True):                 
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+center_text("\nCHARACTER'S CYBERNETIC IMPLANT")+Style.RESET_ALL)
        print(Fore.BLUE+Style.BRIGHT+center_text("Option 'cancel' returns to the main menu\n")+Style.RESET_ALL)
        choices = [            
        "Sandevistan",
        "Monowire",
        "Gorilla Arms",
        "Cybernetic Chrome Arm",
        "Interface Links",
        "Samson frame",
        "Cybernetic Vision",
        "Undefined",
        "Info about Cybernetic Implants",
        "Cancel"
        ]
        implant = menu_choices(choices,"Choose the Standout Cybernetic Implant:")
        if implant == "Cancel":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nCHARACTER'S CYBERNETIC IMPLANT")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+center_text("Option 'cancel' returns to the main menu\n")+Style.RESET_ALL)
            print("Operation Cancelled. Going back to the main menu.")
            stop()
            return
        elif implant == "Undefined":
            implant = "-"
            character.set_cybernetic_implant(implant)
            break 
        elif implant == "Info about Cybernetic Implants":
            result = cybernetic_implants_info("Create_Character")
            if result == "continue":
                continue
            elif result == "menu":
                return 
        else:
            character.set_cybernetic_implant(implant)            
            break    

    # Insert additional information about the character in text form
    option = ""
    while(True):        
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+center_text("\nCHARACTER INFORMATION")+Style.RESET_ALL)
        print(Fore.BLUE+Style.BRIGHT+center_text("type 'cancel' at any time to go back to the Main Menu\n")+Style.RESET_ALL)  
        if option == "invalid":                                                      
            print(Fore.RED+Style.BRIGHT+center_text("It should contain some information")+Style.RESET_ALL) 
        try:     
            additional_info=(input("Enter a short text containing additional information about the character:\n").strip())
        except ValueError:
            pass 
        if additional_info.strip().lower() == "cancel":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nCHARACTER INFORMATION")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+center_text("type 'cancel' at any time to go back to the Main Menu\n")+Style.RESET_ALL) 
            print("Operation Cancelled. Going back to the main menu.")
            stop()
            return
        elif additional_info != "": 
                character.set_additional_info(additional_info)               
                break                   
        else:
            option = "invalid"
    if isinstance(character,Nomad):
        insert_data_file(character.name,character.initial_level,character.max_level,character.occupation,character.pack,character.cybernetic_implant,character.additional_info)
    else:
        insert_data_file(character.name,character.initial_level,character.max_level,character.occupation,character.gang,character.cybernetic_implant,character.additional_info) 
    animated_character_created_text()  
    # Content of the stop() function written directly because in this specific case, the text is centered in the terminal
    for i in range(3,0,-1):
        print("\r",end=" ",flush=True) # "\r" moves the cursor to the beginning of the line (if not done, center_text distorts the print positioning)
        print(Fore.GREEN+Style.BRIGHT+center_text(f"{i}")+Style.RESET_ALL)
        time.sleep(1) 

# Submenu that presents a list of characters and provides some options to the user
def list_characters():
    # Mandatory initialization of a variable that will be used later on
    option = ""
    while(True):        
        os.system('cls') 
        CSV_FILE = 'CyberChar.csv'
        text1 = "CHARACTERS'S LIST"
        text2 = "Type 'cancel' or press 'Enter' with a blank name to go back to the Main Menu\n"
        dataframe = load_dataframe(CSV_FILE)
        display_limited_dataframe(dataframe,text1,text2)
        if option == "invalid":                                        
            print(Fore.RED+Style.BRIGHT+center_text("Character not found")+Style.RESET_ALL)       
        character_name = input("Enter the name of any character to see more information: ")
        # Remove spaces (at the beginning and end) and convert the string to uppercase
        final_character_name = character_name.strip().lower()
        # Transfer names from the dataframe to a series
        # Remove spaces (at the beginning and end) and convert to uppercase the dataframe
        series_names_dataframe = dataframe['                Name'].str.strip().str.lower()
        # Strings Comparison. Does final_character_name exist within the series?
        name_matches = series_names_dataframe.str.contains(final_character_name)  
                        
        if final_character_name.strip().lower() == 'cancel' or final_character_name.strip().lower() == '':
            print("\nGoing back to the Main Menu.")
            stop()
            return 
        elif any(name_matches):
            result = display_character_info(dataframe,name_matches,text1,text2)
            if result == "list":
                continue
            elif result == "menu":
                return            
        else:
            option = "invalid"               

# Display information about specific character
def display_character_info(dataframe,name_matches,text1,text2):    
    character_dataframe = dataframe[name_matches].head(1)
    name = character_dataframe['                Name'].values[0] # Extract information (name) from the DataFrame
    # Mandatory initialization of a variable that will be used later on
    option = ""
    while(True):
        os.system('cls')
        display_limited_dataframe(dataframe,text1,text2)
        # List containing menu options
        choices = [            
            "Yes",
            "Choose another character"
        ]
        # Display the menu using the menu_choices() function
        option = menu_choices(choices,(f"View information about '{name}'?"))          
        if option == "Yes":                    
            # Extract remaining information from the DataFrame                       
            initial_level = character_dataframe['|  Initial Level'].values[0]
            max_level = character_dataframe['|   Maximum Level'].values[0]
            occupation = character_dataframe['|       Occupation'].values[0]
            gang_pack = character_dataframe['|    Gang/Pack'].values[0]
            implant = character_dataframe['|       Cybernetic Implant'].values[0]
            additional_info = character_dataframe['Additional Information'].values[0]
            # Instantiate the character dynamically with the extracted data and display the data            
            while(True): 
                os.system('cls')
                # Search for "occupation" in all global variables, functions, and classes
                occupation_class = globals().get(occupation)

                if occupation == "Gangster":
                    character = occupation_class(name,initial_level,max_level,gang_pack)
                    character.get_centered_name()
                    character.get_description()
                    character.set_cybernetic_implant(implant)
                    character.get_cybernetic_implant()
                    character.set_additional_info(additional_info)
                    character.get_additional_info()

                    choices = [ 
                    "Info about Occupation",
                    "Info about Implant",
                    "Info about Special Skill",
                    "Info about gang",
                    "Choose another character",
                    "Back to Main Menu"
                    ] 
                    
                elif occupation == "Nomad":
                    character = occupation_class(name,initial_level,max_level,gang_pack)
                    character.get_centered_name()
                    character.get_description()
                    character.set_cybernetic_implant(implant)
                    character.get_cybernetic_implant()
                    character.set_additional_info(additional_info)
                    character.get_additional_info()

                    choices = [ 
                    "Info about Occupation",
                    "Info about Implant",
                    "Info about Special Skill",
                    "Info about Pack",
                    "Choose another character",
                    "Back to Main Menu"
                    ] 

                elif occupation == "-":
                    character = Character(name,initial_level,max_level)
                    character.get_centered_name()
                    character.get_description()
                    character.set_cybernetic_implant(implant)
                    character.get_cybernetic_implant()
                    character.set_additional_info(additional_info)
                    character.get_additional_info()

                    choices = [ 
                    "Info about Occupation",
                    "Info about Implant",
                    "Info about Special Skill",
                    "Choose another character",
                    "Back to Main Menu"
                    ] 

                else:
                    character = occupation_class(name,initial_level,max_level)
                    character.get_centered_name()
                    character.get_description()
                    character.set_cybernetic_implant(implant)
                    character.get_cybernetic_implant()
                    character.set_additional_info(additional_info)
                    character.get_additional_info() 

                    choices = [ 
                    "Info about Occupation",
                    "Info about Implant",
                    "Info about Special Skill",
                    "Choose another character",
                    "Back to Main Menu"
                    ]

                option = menu_choices(choices,"") 

                if option == "Back to Main Menu":
                    print("\nGoing back to the Main Menu.")
                    stop()
                    return "menu"
                elif option == "Choose another character":
                    return "list"   
                elif option == "Info about Occupation":
                    os.system('cls')
                    character.get_centered_name()
                    character.get_description()
                    print(get_class_description(occupation))
                    choices = [
                    f"Return to {name}",
                    "Choose another character",
                    "Back to Main Menu"
                    ]
                    option = menu_choices(choices,"")
                    if option == "Back to Main Menu":
                        print("\nGoing back to the Main Menu.")
                        stop()
                        return "menu"
                    elif option == "Choose another character":
                        return "list" 
                    elif option == f"Return to {name}":
                        continue 
                elif option == "Info about Implant":
                    os.system('cls')
                    character.get_centered_name()
                    character.get_description()
                    print(get_implant_description(implant))
                    choices = [
                    f"Return to {name}",
                    "Choose another character",
                    "Back to Main Menu"
                    ]
                    option = menu_choices(choices,"")
                    if option == "Back to Main Menu":
                        print("\nGoing back to the Main Menu.")
                        stop()
                        return "menu"
                    elif option == "Choose another character":
                        return "list" 
                    elif option == f"Return to {name}":
                        continue 
                elif option == "Info about Special Skill":
                    os.system('cls')
                    character.get_centered_name()
                    character.get_description()
                    print(get_description_class_ability(occupation))
                    choices = [
                    f"Return to {name}",
                    "Choose another character",
                    "Back to Main Menu"
                    ]
                    option = menu_choices(choices,"")
                    if option == "Back to Main Menu":
                        print("\nGoing back to the Main Menu.")
                        stop()
                        return "menu"
                    elif option == "Choose another character":
                        return "list" 
                    elif option == f"Return to {name}":
                        continue 
                elif option == "Info about gang":
                    os.system('cls')
                    character.get_centered_name()
                    character.get_description()
                    print(get_gang_description(gang_pack))
                    choices = [
                    f"Return to {name}",
                    "Choose another character",
                    "Back to Main Menu"
                    ]
                    option = menu_choices(choices,"")
                    if option == "Back to Main Menu":
                        print("\nGoing back to the Main Menu.")
                        stop()
                        return "menu"
                    elif option == "Choose another character":
                        return "list" 
                    elif option == f"Return to {name}":
                        continue 
                elif option == "Info about Pack":
                    os.system('cls')
                    character.get_centered_name()
                    character.get_description()
                    print(get_pack_description(gang_pack))
                    choices = [
                    f"Return to {name}",
                    "Choose another character",
                    "Back to Main Menu"
                    ]
                    option = menu_choices(choices,"")
                    if option == "Back to Main Menu":
                        print("\nGoing back to the Main Menu.")
                        stop()
                        return "menu"
                    elif option == "Choose another character":
                        return "list" 
                    elif option == f"Return to {name}":
                        continue 
                
        elif option == "Choose another character":
            return "list"

# Delete a character chosen by the user
def delete_character(): 
    # Mandatory initialization of a variable that will be used later on  
    option = ""    
    while True:
        os.system('cls')
        CSV_FILE = 'CyberChar.csv'
        text1 = "DELETE CHARACTER"
        text2 = "Type 'cancel' or press 'Enter' with a blank name to go back to the Main Menu\n"        
        # Display a list of characters
        dataframe = load_dataframe(CSV_FILE)
        display_limited_dataframe(dataframe,text1,text2)
        # Ask the user to type the name of the character to be deleted
        if option == "invalid":                                        
            print(Fore.RED+Style.BRIGHT+center_text("Character not found")+Style.RESET_ALL)
        if option == "Not allowed":                                        
            print(Fore.RED+Style.BRIGHT+center_text(f"Deletion not possible '{character_name}'.")+Style.RESET_ALL)
        try:   
            character_name = input("Enter the name of the character you want to delete: ").strip()
        except ValueError:
            pass 
        # Back to Main Menu
        if character_name.strip().lower() == "cancel" or character_name.strip().lower() == "":
            print("Operation Cancelled. Going back to the main menu.")
            stop()
            return
        # If it exists, proceed
        elif character_name in dataframe['                Name'].values:            
            # Confirm deletion
            while True: 
                # Check if the entered name is part of the predefined characters
                if character_name in predefined_characters:
                    option = "Not allowed"
                    break
                os.system('cls')
                display_limited_dataframe(dataframe,text1,text2)
                # List containing menu options
                choices = [            
                    "Yes",
                    "No"
                ]
                # Display the menu using the menu_choices() function
                option = menu_choices(choices,(f"Are you sure you want to delete '{character_name}'?"))
                if option == 'Yes':
                    # Delete the character from the DataFrame and rewrite the CSV file
                    new_data_df = dataframe[dataframe['                Name'] != character_name]
                    new_data_df.to_csv(CSV_FILE, encoding='utf-8', index=False)
                    print(f"Character '{character_name}' successfully deleted!")
                    input("\nPress Enter to continue.")
                    break
                elif option == 'No':
                    break                    
        else:
            if option != "Not allowed":
                option = "invalid"            

# Definition of Main
def main():
    load_dataframe('CyberChar.csv') 
    play_music('music1.mp3')   
    while(True):
        os.system('cls') 
        animated_title()  
        # List containing menu options
        choices = [            
            "Create Character",
            "List Characters",
            "Delete Character",
            "Cyberpunk universe",
            "Exit"
        ]
        # Display the menu using the function
        option = menu_choices(choices,"")

        if option == "Create Character": 
            create_character()             
        elif option == "List Characters":
            list_characters()
        elif option == "Delete Character":
            delete_character()
        elif option == "Cyberpunk universe":
            cyberpunk_universe()
        elif option == "Exit":
            stop_music()            
            print("\nYour journey in the Cyberpunk universe has concluded. Returning to your reality.")
            stop()
            exit()

# Run the Main Function
if __name__ == "__main__":
    main()   
