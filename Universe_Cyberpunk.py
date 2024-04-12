import os # Used to clear the console.
from Lore_Cyberpunk import * # Information about the Cyberpunk universe.
from Main_Cyberpunk import menu_choices, stop
from Animations_Cyberpunk import center_text # Centers the text

# This module contains various functions related to presenting information about the world of Cyberpunk.

# Function cyberpunk_universe, Main Menu (for the user to discover more about the universe)
def cyberpunk_universe():
    # User chooses the topic
    while(True):
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+center_text("\nCYBERPUNK UNIVERSE")+Style.RESET_ALL)        
        print(Fore.BLUE+Style.BRIGHT+center_text("Discover more about the Cyberpunk universe.")+Style.RESET_ALL)
        # Menu options list
        choices = [            
            "The World of Cyberpunk",
            "Cybernetic Implants",
            "Occupations / Roles in Society",
            "Gangs",
            "Nomad Packs",
            "Back to Main Menu"
        ]
        # Display the menu using the menu_choices() function.
        option = menu_choices(choices,"Choose the theme:")        
        if option == "Back to Main Menu":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nCYBERPUNK UNIVERSE")+Style.RESET_ALL)        
            print(Fore.BLUE+Style.BRIGHT+center_text("Explore more about the Cyberpunk universe")+Style.RESET_ALL)
            print("Going back to the main menu.")
            stop()
            return
        elif option == "The World of Cyberpunk":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nTHE WORLD OF CYBERPUNK")+Style.RESET_ALL)
            print(get_cyberpunk_lore(option))
            choices = [            
            "Cyberpunk universe",
            "Back to Main Menu"
            ]
            option = menu_choices(choices,"")
            if option == "Cyberpunk universe":
                pass
            elif option == "Back to Main Menu":
                os.system('cls')
                print(Fore.BLUE+Style.BRIGHT+center_text("\nTHE WORLD OF CYBERPUNK")+Style.RESET_ALL)
                print("Going back to the main menu.")
                stop()
                return
        elif option == "Cybernetic Implants":
            resultado = cybernetic_implants_info("cyberpunk_universe")
            if resultado == "continue":
                continue
            elif resultado == "menu":
                return 
        elif option == "Occupations / Roles in Society":
            resultado = info_occupations("cyberpunk_universe")
            if resultado == "continue":
                continue
            elif resultado == "menu":
                return 
        elif option == "Gangs":
            resultado = info_gangs("cyberpunk_universe")
            if resultado == "continue":
                continue
            elif resultado == "menu":
                return 
        elif option == "Nomad Packs":
            resultado = info_nomad_packs("cyberpunk_universe")
            if resultado == "continue":
                continue
            elif resultado == "menu":
                return         

# Display info about cybernetic implants
def cybernetic_implants_info(context):
    while (True):
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+center_text("\nCYBERNETIC IMPLANTS")+Style.RESET_ALL)
        print(get_cyberpunk_lore("Cybernetic Implants"))
        if context == "cyberpunk_universe":
            choices = [ 
            "Sandevistan",
            "Monowire",
            "Gorilla Arms",
            "Cybernetic Chrome Arm",
            "Interface Links",
            "Samson frame",
            "Cybernetic Vision",           
            "Cyberpunk universe",
            "Back to Main Menu"
            ] 
        elif context == "Create_Character":
            choices = [ 
            "Sandevistan",
            "Monowire",
            "Gorilla Arms",
            "Cybernetic Chrome Arm",
            "Interface Links",
            "Samson frame",
            "Cybernetic Vision",           
            "Back to character creator",
            "Back to Main Menu"
            ]           
        option = menu_choices(choices,"Cybernetic Implants Info")
        if option == "Cyberpunk universe" or option == "Back to character creator":
            return "continue"
        elif option == "Back to Main Menu":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nCYBERNETIC IMPLANTS")+Style.RESET_ALL)
            print("Going back to the main menu.")            
            stop()
            return "menu"
        else:
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nCYBERNETIC IMPLANTS")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+center_text(option)+Style.RESET_ALL)
            print(get_implant_description(option))
            if context == "cyberpunk_universe":
                choices = [ 
                "Cybernetic Implants",           
                "Cyberpunk universe",
                "Back to Main Menu"
                ]
            elif context == "Create_Character":
                choices = [ 
                "Cybernetic Implants",           
                "Back to character creator",
                "Back to Main Menu"
                ]            
            option = menu_choices(choices,"")
            if option == "Cyberpunk universe" or option == "Back to character creator":
                return "continue"
            elif option == "Back to Main Menu":
                os.system('cls')
                print(Fore.BLUE+Style.BRIGHT+center_text("\nCYBERNETIC IMPLANTS")+Style.RESET_ALL)
                print("Going back to the main menu.")                
                stop()
                return "menu"
            elif option == "Cybernetic Implants":
                pass

# Display info about occupations / roles in society
def info_occupations(context):   
    while (True):
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+center_text("\nOCCUPATIONS/ROLES IN SOCIETY")+Style.RESET_ALL)
        if context == "cyberpunk_universe":
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
            "Cyberpunk universe",
            "Back to Main Menu"
            ]
        elif context == "Create_Character":
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
            "Back to character creator",
            "Back to Main Menu"
            ]          
        option = menu_choices(choices,"Information About Occupations")
        if option == "Cyberpunk universe" or option == "Back to character creator":
            return "continue"
        elif option == "Back to Main Menu":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nOCCUPATIONS/ROLES IN SOCIETY")+Style.RESET_ALL)
            print("Going back to the main menu.")
            stop()
            return "menu"
        else:
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nOCCUPATIONS/ROLES IN SOCIETY")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+center_text(option)+Style.RESET_ALL)
            print(get_class_description(option))
            print(get_description_class_ability(option))
            if context == "cyberpunk_universe":
                choices = [ 
                "Occupations / Roles in Society",           
                "Cyberpunk universe",
                "Back to Main Menu"
                ]
            elif context == "Create_Character":
                choices = [ 
                "Occupations / Roles in Society",           
                "Back to character creator",
                "Back to Main Menu"
                ]       
            option = menu_choices(choices,"")
            if option == "Cyberpunk universe" or option == "Back to character creator":
                return "continue"
            elif option == "Back to Main Menu":
                os.system('cls')
                print(Fore.BLUE+Style.BRIGHT+center_text("\nOCCUPATIONS/ROLES IN SOCIETY")+Style.RESET_ALL)
                print("Going back to the main menu.")
                stop()
                return "menu"
            elif option == "Occupations / Roles in Society":
                pass

# Display info about occupations / roles in society
def info_gangs(context):
    while (True):
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+center_text("\nGANGS")+Style.RESET_ALL)
        if context == "cyberpunk_universe":
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
            "Cyberpunk universe",
            "Back to Main Menu"
            ] 
        elif context == "Create_Character": 
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
            "Back to character creator",
            "Back to Main Menu"
            ]           
        option = menu_choices(choices,"Info About Gangs")
        if option == "Cyberpunk universe" or option == "Back to character creator":
            return "continue"
        elif option == "Back to Main Menu":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nGANGS")+Style.RESET_ALL)
            print("Going back to the main menu.")
            stop()
            return "menu"
        else:
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nGANGS")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+center_text(option)+Style.RESET_ALL)
            print(get_gang_description(option))
            if context == "cyberpunk_universe":
                choices = [ 
                "Gangs",           
                "Cyberpunk universe",
                "Back to Main Menu"
                ] 
            elif context == "Create_Character":
                choices = [ 
                "Gangs",           
                "Back to character creator",
                "Back to Main Menu"
                ]            
            option = menu_choices(choices,"")
            if option == "Cyberpunk universe" or option == "Back to character creator":
                return "continue"
            elif option == "Back to Main Menu":
                os.system('cls')
                print(Fore.BLUE+Style.BRIGHT+center_text("\nGANGS")+Style.RESET_ALL)
                print("Going back to the main menu.")
                stop()
                return "menu"
            elif option == "Gangs":
                pass

# Display info about Nomad Packs
def info_nomad_packs(context):
    while (True):
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+center_text("\nNOMAD PACKS")+Style.RESET_ALL)
        if context == "cyberpunk_universe":
            choices = [ 
            "Wraiths",
            "Aldecaldos",         
            "Cyberpunk universe",
            "Back to Main Menu"
            ] 
        elif context == "Create_Character":
            choices = [ 
            "Wraiths",
            "Aldecaldos",         
            "Back to character creator",
            "Back to Main Menu"
            ]                       
        option = menu_choices(choices,"Info About Nomad Packs")
        if option == "Cyberpunk universe" or option == "Back to character creator":
            return "continue"
        elif option == "Back to Main Menu":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nNOMAD PACKS")+Style.RESET_ALL)
            print("Going back to the main menu.")
            stop()
            return "menu"
        else:
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nNOMAD PACKS")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+center_text(option)+Style.RESET_ALL)
            print(get_pack_description(option))
            if context == "cyberpunk_universe":
                choices = [ 
                "Nomad Packs",           
                "Cyberpunk universe",
                "Back to Main Menu"
                ] 
            elif context == "Create_Character": 
                choices = [ 
                "Nomad Packs",           
                "Back to character creator",
                "Back to Main Menu"
                ]           
            option = menu_choices(choices,"")
            if option == "Cyberpunk universe" or option == "Back to character creator":
                return "continue"
            elif option == "Back to Main Menu":
                os.system('cls')
                print(Fore.BLUE+Style.BRIGHT+center_text("\nNOMAD PACKS")+Style.RESET_ALL)
                print("Going back to the main menu.")                
                stop()
                return "menu"
            elif option == "Nomad Packs":
                pass