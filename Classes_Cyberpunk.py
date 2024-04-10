from Animations_Cyberpunk import * # Contém animações e outras funções relacionadas com texto

# Definição da classe Pai "Personagem"
class Personagem:  
    def __init__(self,nome,nivel_inicial,nivel_max): # Construtor
        self.nome=nome        
        self.nivel_inicial=nivel_inicial 
        self.nivel_max=nivel_max    
        self.ocupacao="-"
        self.gangue="-"

    def set_implante_cibernetico(self,implantecibernetico): # Método que define o/os implantes cibernéticos
        self.implante_cibernetico=implantecibernetico 
    
    def get_implante_cibernetico(self): # Método que obtém a implantes cibernéticos        
        print(Fore.GREEN+Style.BRIGHT+"\nImplante Cibernético de destaque"+Style.RESET_ALL+f"\n{self.implante_cibernetico}")

    def set_info_adicional(self,infoadicional): # Método que define informação adicional do objeto
        self.info_adicional=infoadicional 
    
    def get_info_adicional(self): # Método que obtém informação adicional do objeto
        print(Fore.GREEN+Style.BRIGHT+f"\nSobre {self.nome}"+Style.RESET_ALL+f"\n{self.info_adicional}\n")

    def get_nome_centrado(self): # Método que exibe nome do objeto como título
        print(Fore.BLUE+Style.BRIGHT+centrar_texto(f"{self.nome.upper()}")+Style.RESET_ALL)
    
    def get_descricao(self): # Método que descreve o personagem fazendo uso dos atributos da classe
        print(Fore.BLUE+Style.BRIGHT+centrar_texto(f"Inicializará o jogo no nível {self.nivel_inicial} podendo atingir no máximo {self.nivel_max}.")+Style.RESET_ALL)        

# Definição da classe "Corpo" (Filha da Classe Pai "Personagem")
class Corpo(Personagem):    
    def __init__(self,nome,nivel_inicial,nivel_max):        
        super().__init__(nome,nivel_inicial,nivel_max) # Inicialização dos atributos da classe Pai "Personagem" 
        self.ocupacao="Corpo"
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+centrar_texto(f"{self.nome} é Corporativo.\nInicializará o jogo no nível {self.nivel_inicial} podendo atingir no máximo {self.nivel_max}.")+Style.RESET_ALL)

# Definição da classe "Rockerboy" (Filha da Classe Pai "Personagem")
class Rockerboy(Personagem):    
    def __init__(self,nome,nivel_inicial,nivel_max):        
        super().__init__(nome,nivel_inicial,nivel_max) # Inicialização dos atributos da classe Pai "Personagem" 
        self.ocupacao="Rockerboy"
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+centrar_texto(f"Rebelde Rockerboy!\nInicializará o jogo no nível {self.nivel_inicial} podendo atingir no máximo {self.nivel_max}.")+Style.RESET_ALL)

# Definição da classe "Gangster" (Filha da Classe Pai "Personagem")
class Gangster(Personagem):    
    def __init__(self,nome,nivel_inicial,nivel_max,gangue):        
        super().__init__(nome,nivel_inicial,nivel_max) # Inicialização dos atributos da classe Pai "Personagem" 
        self.ocupacao="Gangster"       
        self.gangue=gangue
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+centrar_texto(f"Pertence ao gangue {self.gangue}.\nInicializará o jogo no nível {self.nivel_inicial} podendo atingir no máximo {self.nivel_max}.")+Style.RESET_ALL)
    
# Definição da classe "Polícia" (Filha da Classe Pai "Personagem")
class Policia(Personagem):    
    def __init__(self,nome,nivel_inicial,nivel_max):        
        super().__init__(nome,nivel_inicial,nivel_max) # Inicialização dos atributos da classe Pai "Personagem" 
        self.ocupacao="Polícia"
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+centrar_texto(f"Oficial da polícia.\nInicializará o jogo no nível {self.nivel_inicial} podendo atingir no máximo {self.nivel_max}.")+Style.RESET_ALL)

# Definição da classe "Solo" (Filha da Classe Pai "Personagem")
class Solo(Personagem):    
    def __init__(self,nome,nivel_inicial,nivel_max):        
        super().__init__(nome,nivel_inicial,nivel_max) # Inicialização dos atributos da classe Pai "Personagem" 
        self.ocupacao="Solo"
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+centrar_texto(f"Gosta de trabalhar Solo.\nInicializará o jogo no nível {self.nivel_inicial} podendo atingir no máximo {self.nivel_max}.")+Style.RESET_ALL)

# Definição da classe "Netrunner" (Filha da Classe Pai "Personagem")
class Netrunner(Personagem):    
    def __init__(self,nome,nivel_inicial,nivel_max):        
        super().__init__(nome,nivel_inicial,nivel_max) # Inicialização dos atributos da classe Pai "Personagem" 
        self.ocupacao="Netrunner"
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+centrar_texto(f"{self.nome} é Netrunner.\nInicializará o jogo no nível {self.nivel_inicial} podendo atingir no máximo {self.nivel_max}.")+Style.RESET_ALL)

# Definição da classe "Techie" (Filha da Classe Pai "Personagem")
class Techie(Personagem):    
    def __init__(self,nome,nivel_inicial,nivel_max):        
        super().__init__(nome,nivel_inicial,nivel_max) # Inicialização dos atributos da classe Pai "Personagem" 
        self.ocupacao="Techie"
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+centrar_texto(f"{self.nome} é Techie.\nInicializará o jogo no nível {self.nivel_inicial} podendo atingir no máximo {self.nivel_max}.")+Style.RESET_ALL)

# Definição da classe "Media" (Filha da Classe Pai "Personagem")
class Media(Personagem):    
    def __init__(self,nome,nivel_inicial,nivel_max):        
        super().__init__(nome,nivel_inicial,nivel_max) # Inicialização dos atributos da classe Pai "Personagem" 
        self.ocupacao="Media"
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+centrar_texto(f"Faz parte dos Media.\nInicializará o jogo no nível {self.nivel_inicial} podendo atingir no máximo {self.nivel_max}.")+Style.RESET_ALL)

# Definição da classe "Fixer" (Filha da Classe Pai "Personagem")
class Fixer(Personagem):    
    def __init__(self,nome,nivel_inicial,nivel_max):        
        super().__init__(nome,nivel_inicial,nivel_max) # Inicialização dos atributos da classe Pai "Personagem" 
        self.ocupacao="Fixer"
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+centrar_texto(f"Respeitado e influente Fixer.\nInicializará o jogo no nível {self.nivel_inicial} podendo atingir no máximo {self.nivel_max}.")+Style.RESET_ALL)

# Definição da classe "Nomad" (Filha da Classe Pai "Personagem")
class Nomad(Personagem):    
    def __init__(self,nome,nivel_inicial,nivel_max,pack):        
        super().__init__(nome,nivel_inicial,nivel_max) # Inicialização dos atributos da classe Pai "Personagem" 
        self.ocupacao="Nomad"
        self.pack=pack # Atributo específico da classe filha "Nomad"
    def get_descricao(self): # Descrição exclusiva a esta classe usando um método sobreposto
        print(Fore.BLUE+Style.BRIGHT+centrar_texto(f"Nomad, faz parte do pack {self.pack}.\nInicializará o jogo no nível {self.nivel_inicial} podendo atingir no máximo {self.nivel_max}.")+Style.RESET_ALL)
