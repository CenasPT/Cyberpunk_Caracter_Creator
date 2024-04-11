from Animations_Cyberpunk import * # Contains animations and other functions related to text

# Definition of the parent class "Character"
class Character:  
    def __init__(self,name,initial_level,max_level): # Constructor
        self.name=name        
        self.initial_level=initial_level 
        self.max_level=max_level    
        self.occupation="-"
        self.gang="-"

    def set_cybernetic_implant(self,cybernetic_implant): # Método que define o/os implantes cibernéticos
        self.implante_cibernetico=cybernetic_implant 
    
    def get_implante_cibernetico(self): # Método que obtém a implantes cibernéticos        
        print(Fore.GREEN+Style.BRIGHT+"\nImplante Cibernético de destaque"+Style.RESET_ALL+f"\n{self.implante_cibernetico}")

    def set_info_adicional(self,infoadicional): # Método que define informação adicional do objeto
        self.info_adicional=infoadicional 
    
    def get_info_adicional(self): # Método que obtém informação adicional do objeto
        print(Fore.GREEN+Style.BRIGHT+f"\nSobre {self.name}"+Style.RESET_ALL+f"\n{self.info_adicional}\n")

    def get_name_centrado(self): # Método que exibe name do objeto como título
        print(Fore.BLUE+Style.BRIGHT+center_text(f"{self.name.upper()}")+Style.RESET_ALL)
    
    def get_descricao(self): # Método que descreve o personagem fazendo uso dos atributos da classe
        print(Fore.BLUE+Style.BRIGHT+center_text(f"Inicializará o jogo no nível {self.initial_level} podendo atingir no máximo {self.max_level}.")+Style.RESET_ALL)        

# Definição da classe "Corpo" (Filha da Classe Pai "Personagem")
class Corpo(Character):    
    def __init__(self,name,initial_level,max_level):        
        super().__init__(name,initial_level,max_level) # Inicialização dos atributos da classe Pai "Personagem" 
        self.occupation="Corpo"
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+center_text(f"{self.name} é Corporativo.\nInicializará o jogo no nível {self.initial_level} podendo atingir no máximo {self.max_level}.")+Style.RESET_ALL)

# Definição da classe "Rockerboy" (Filha da Classe Pai "Personagem")
class Rockerboy(Character):    
    def __init__(self,name,initial_level,max_level):        
        super().__init__(name,initial_level,max_level) # Inicialização dos atributos da classe Pai "Personagem" 
        self.occupation="Rockerboy"
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+center_text(f"Rebelde Rockerboy!\nInicializará o jogo no nível {self.initial_level} podendo atingir no máximo {self.max_level}.")+Style.RESET_ALL)

# Definição da classe "Gangster" (Filha da Classe Pai "Personagem")
class Gangster(Character):    
    def __init__(self,name,initial_level,max_level,gang):        
        super().__init__(name,initial_level,max_level) # Inicialização dos atributos da classe Pai "Personagem" 
        self.occupation="Gangster"       
        self.gang=gang
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+center_text(f"Pertence ao gang {self.gang}.\nInicializará o jogo no nível {self.initial_level} podendo atingir no máximo {self.max_level}.")+Style.RESET_ALL)
    
# Definição da classe "Polícia" (Filha da Classe Pai "Personagem")
class Policia(Character):    
    def __init__(self,name,initial_level,max_level):        
        super().__init__(name,initial_level,max_level) # Inicialização dos atributos da classe Pai "Personagem" 
        self.occupation="Polícia"
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+center_text(f"Oficial da polícia.\nInicializará o jogo no nível {self.initial_level} podendo atingir no máximo {self.max_level}.")+Style.RESET_ALL)

# Definição da classe "Solo" (Filha da Classe Pai "Personagem")
class Solo(Character):    
    def __init__(self,name,initial_level,max_level):        
        super().__init__(name,initial_level,max_level) # Inicialização dos atributos da classe Pai "Personagem" 
        self.occupation="Solo"
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+center_text(f"Gosta de trabalhar Solo.\nInicializará o jogo no nível {self.initial_level} podendo atingir no máximo {self.max_level}.")+Style.RESET_ALL)

# Definição da classe "Netrunner" (Filha da Classe Pai "Personagem")
class Netrunner(Character):    
    def __init__(self,name,initial_level,max_level):        
        super().__init__(name,initial_level,max_level) # Inicialização dos atributos da classe Pai "Personagem" 
        self.occupation="Netrunner"
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+center_text(f"{self.name} é Netrunner.\nInicializará o jogo no nível {self.initial_level} podendo atingir no máximo {self.max_level}.")+Style.RESET_ALL)

# Definição da classe "Techie" (Filha da Classe Pai "Personagem")
class Techie(Character):    
    def __init__(self,name,initial_level,max_level):        
        super().__init__(name,initial_level,max_level) # Inicialização dos atributos da classe Pai "Personagem" 
        self.occupation="Techie"
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+center_text(f"{self.name} é Techie.\nInicializará o jogo no nível {self.initial_level} podendo atingir no máximo {self.max_level}.")+Style.RESET_ALL)

# Definição da classe "Media" (Filha da Classe Pai "Personagem")
class Media(Character):    
    def __init__(self,name,initial_level,max_level):        
        super().__init__(name,initial_level,max_level) # Inicialização dos atributos da classe Pai "Personagem" 
        self.occupation="Media"
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+center_text(f"Faz parte dos Media.\nInicializará o jogo no nível {self.initial_level} podendo atingir no máximo {self.max_level}.")+Style.RESET_ALL)

# Definição da classe "Fixer" (Filha da Classe Pai "Personagem")
class Fixer(Character):    
    def __init__(self,name,initial_level,max_level):        
        super().__init__(name,initial_level,max_level) # Inicialização dos atributos da classe Pai "Personagem" 
        self.occupation="Fixer"
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+center_text(f"Respeitado e influente Fixer.\nInicializará o jogo no nível {self.initial_level} podendo atingir no máximo {self.max_level}.")+Style.RESET_ALL)

# Definição da classe "Nomad" (Filha da Classe Pai "Personagem")
class Nomad(Character):    
    def __init__(self,name,initial_level,max_level,pack):        
        super().__init__(name,initial_level,max_level) # Inicialização dos atributos da classe Pai "Personagem" 
        self.occupation="Nomad"
        self.pack=pack # Atributo específico da classe filha "Nomad"
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+center_text(f"Nomad, faz parte do pack {self.pack}.\nInicializará o jogo no nível {self.initial_level} podendo atingir no máximo {self.max_level}.")+Style.RESET_ALL)
