from Animations_Cyberpunk import * # Contains animations and other functions related to text

# Definition of the parent class "Character"
class Character:  
    def __init__(self,name,initial_level,max_level): # Constructor
        self.name=name        
        self.initial_level=initial_level 
        self.max_level=max_level    
        self.occupation="-"
        self.gang="-"

    def set_cybernetic_implant(self,cybernetic_implant): # The method defining cybernetic implants.
        self.cybernetic_implant=cybernetic_implant 
    
    def get_cybernetic_implant(self): # Method that retrieves cybernetic implants        
        print(Fore.GREEN+Style.BRIGHT+"\nProminent Cybernetic Implant"+Style.RESET_ALL+f"\n{self.cybernetic_implant}")

    def set_additional_info(self,additional_info): # Method that defines additional information of the object
        self.additional_info=additional_info 
    
    def get_additional_info(self): # Method that retrieves additional information of the object
        print(Fore.GREEN+Style.BRIGHT+f"About {self.name}"+Style.RESET_ALL+f"\n{self.additional_info}\n")

    def get_centered_name(self): # Method that displays the object's name as a title
        print(Fore.BLUE+Style.BRIGHT+center_text(f"{self.name.upper()}")+Style.RESET_ALL)
    
    def get_description(self): # Method that describes the character using the class attributes
        print(Fore.BLUE+Style.BRIGHT+center_text(f"Will initialize the game at level {self.initial_level}, with the potential to reach a maximum of {self.max_level}.")+Style.RESET_ALL)        

# Definition of the "Corpo" class (Child of the Parent Class "Character")
class Corpo(Character):    
    def __init__(self,name,initial_level,max_level):        
        super().__init__(name,initial_level,max_level) # Initialization of the attributes of the Parent Class "Character"
        self.occupation="Corpo"
    def get_description(self): # Unique description exclusive to this class using an overridden method
        print(Fore.BLUE+Style.BRIGHT+center_text(f"A calculating Corporate.\nWill initialize the game at level {self.initial_level}, with the potential to reach a maximum of {self.max_level}.")+Style.RESET_ALL)

# Definition of the "Rockerboy" class (Child of the Parent Class "Character")
class Rockerboy(Character):    
    def __init__(self,name,initial_level,max_level):        
        super().__init__(name,initial_level,max_level) # initialization of the Parent Class's attributes
        self.occupation="Rockerboy"
    def get_description(self): # Unique description exclusive to this class using an overridden method
        print(Fore.BLUE+Style.BRIGHT+center_text(f"Rebel Rockerboy!\nWill initialize the game at level {self.initial_level}, with the potential to reach a maximum of {self.max_level}.")+Style.RESET_ALL)

# Definition of the "Gangster" class (Child of the Parent Class "Character")
class Gangster(Character):    
    def __init__(self,name,initial_level,max_level,gang):        
        super().__init__(name,initial_level,max_level) # initialization of the Parent Class's attributes
        self.occupation="Gangster"       
        self.gang=gang
    def get_description(self): # Unique description exclusive to this class using an overridden method
        print(Fore.BLUE+Style.BRIGHT+center_text(f"Belongs to the {self.gang} gang.\nWill initialize the game at level {self.initial_level}, with the potential to reach a maximum of {self.max_level}.")+Style.RESET_ALL)
    
# Definition of the "Cop" class (Child of the Parent Class "Character")
class Cop(Character):    
    def __init__(self,name,initial_level,max_level):        
        super().__init__(name,initial_level,max_level) # initialization of the Parent Class's attributes
        self.occupation="Cop"
    def get_description(self): # Unique description exclusive to this class using an overridden method
        print(Fore.BLUE+Style.BRIGHT+center_text(f"Police Officer.\nWill initialize the game at level {self.initial_level}, with the potential to reach a maximum of {self.max_level}.")+Style.RESET_ALL)

# Definition of the "Solo" class (Child of the Parent Class "Character")
class Solo(Character):    
    def __init__(self,name,initial_level,max_level):        
        super().__init__(name,initial_level,max_level) # initialization of the Parent Class's attributes
        self.occupation="Solo"
    def get_description(self): # Unique description exclusive to this class using an overridden method
        print(Fore.BLUE+Style.BRIGHT+center_text(f"Prefers to work Solo.\nWill initialize the game at level {self.initial_level}, with the potential to reach a maximum of {self.max_level}.")+Style.RESET_ALL)

# Definition of the "Netrunner" class (Child of the Parent Class "Character")
class Netrunner(Character):    
    def __init__(self,name,initial_level,max_level):        
        super().__init__(name,initial_level,max_level) # initialization of the Parent Class's attributes
        self.occupation="Netrunner"
    def get_description(self): # Unique description exclusive to this class using an overridden method
        print(Fore.BLUE+Style.BRIGHT+center_text(f"A Skilled Netrunner.\nWill initialize the game at level {self.initial_level}, with the potential to reach a maximum of {self.max_level}.")+Style.RESET_ALL)

# Definition of the "Techie" class (Child of the Parent Class "Character")
class Techie(Character):    
    def __init__(self,name,initial_level,max_level):        
        super().__init__(name,initial_level,max_level) # initialization of the Parent Class's attributes
        self.occupation="Techie"
    def get_description(self): # Unique description exclusive to this class using an overridden method
        print(Fore.BLUE+Style.BRIGHT+center_text(f"Resourceful Techie.\nWill initialize the game at level {self.initial_level}, with the potential to reach a maximum of {self.max_level}.")+Style.RESET_ALL)

# Definition of the "Media" class (Child of the Parent Class "Character")
class Media(Character):    
    def __init__(self,name,initial_level,max_level):        
        super().__init__(name,initial_level,max_level) # initialization of the Parent Class's attributes
        self.occupation="Media"
    def get_description(self): # Unique description exclusive to this class using an overridden method
        print(Fore.BLUE+Style.BRIGHT+center_text(f"Part of the Media.\nWill initialize the game at level {self.initial_level}, with the potential to reach a maximum of {self.max_level}.")+Style.RESET_ALL)

# Definition of the "Fixer" class (Child of the Parent Class "Character")
class Fixer(Character):    
    def __init__(self,name,initial_level,max_level):        
        super().__init__(name,initial_level,max_level) # initialization of the Parent Class's attributes
        self.occupation="Fixer"
    def get_description(self): # Unique description exclusive to this class using an overridden method
        print(Fore.BLUE+Style.BRIGHT+center_text(f"Respected and influential Fixer.\nWill initialize the game at level {self.initial_level}, with the potential to reach a maximum of {self.max_level}.")+Style.RESET_ALL)

# Definition of the "Nomad" class (Child of the Parent Class "Character")
class Nomad(Character):    
    def __init__(self,name,initial_level,max_level,pack):        
        super().__init__(name,initial_level,max_level) # initialization of the Parent Class's attributes
        self.occupation="Nomad"
        self.pack=pack # Specific attribute of the child class "Nomad"
    def get_description(self): # Unique description exclusive to this class using an overridden method
        print(Fore.BLUE+Style.BRIGHT+center_text(f"Nomad, part of the {self.pack} pack.\nWill initialize the game at level {self.initial_level}, with the potential to reach a maximum of {self.max_level}.")+Style.RESET_ALL)
