import os # Utilizado para limpar a consola
from Lore_Cyberpunk import * # Informações sobre o universo Cyberpunk
from Main_Cyberpunk import menu_escolhas, stop

# Este módulo contém várias funções relacionadas com a apresentação de infomação sobre o mundo de Cyberpunk

# Função universo_cyberpunk, Menu Principal (para o utilizador descobrir mais sobre o universo)
def universo_cyberpunk():
    # Utilizador escolhe o tema
    while(True):
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nUNIVERSO CYBERPUNK")+Style.RESET_ALL)        
        print(Fore.BLUE+Style.BRIGHT+centrar_texto("Descobre mais sobre o universo Cyberpunk")+Style.RESET_ALL)
        # Lista que contém opções do menu
        escolhas = [            
            "O mundo de Cyberpunk",
            "Implantes Cibernéticos",
            "Ocupações / Papéis na sociedade",
            "Gangues",
            "Nomad Packs",
            "Voltar ao Menu Principal"
        ]
        # Exibir o menu utilizando a função menu_escolhas()
        opcao = menu_escolhas(escolhas,"Escolhe o tema:")        
        if opcao == "Voltar ao Menu Principal":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nUNIVERSO CYBERPUNK")+Style.RESET_ALL)        
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("Descobre mais sobre o universo Cyberpunk")+Style.RESET_ALL)
            print("Voltando ao menu principal.")
            stop()
            return
        elif opcao == "O mundo de Cyberpunk":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nO MUNDO DE CYBERPUNK")+Style.RESET_ALL)
            print(get_lore_cyberpunk(opcao))
            escolhas = [            
            "Universo Cyberpunk",
            "Voltar ao Menu Principal"
            ]
            opcao = menu_escolhas(escolhas,"")
            if opcao == "Universo Cyberpunk":
                pass
            elif opcao == "Voltar ao Menu Principal":
                os.system('cls')
                print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nO MUNDO DE CYBERPUNK")+Style.RESET_ALL)
                print("Voltando ao menu principal.")
                stop()
                return
        elif opcao == "Implantes Cibernéticos":
            resultado = info_implantes_ciberneticos("Universo_Cyberpunk")
            if resultado == "continuar":
                continue
            elif resultado == "menu":
                return 
        elif opcao == "Ocupações / Papéis na sociedade":
            resultado = info_ocupacoes("Universo_Cyberpunk")
            if resultado == "continuar":
                continue
            elif resultado == "menu":
                return 
        elif opcao == "Gangues":
            resultado = info_gangues("Universo_Cyberpunk")
            if resultado == "continuar":
                continue
            elif resultado == "menu":
                return 
        elif opcao == "Nomad Packs":
            resultado = info_nomad_packs("Universo_Cyberpunk")
            if resultado == "continuar":
                continue
            elif resultado == "menu":
                return         

# Exibir info sobre implantes cibernéticos
def info_implantes_ciberneticos(contexto):
    while (True):
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nIMPLANTES CIBERNÉTICOS")+Style.RESET_ALL)
        print(get_lore_cyberpunk("Implantes Cibernéticos"))
        if contexto == "Universo_Cyberpunk":
            escolhas = [ 
            "Sandevistan",
            "Monowire",
            "Gorilla Arms",
            "Braço cibernético Cromado",
            "Ligações de Interface",
            "Samson frame",
            "Visão Cibernética",           
            "Universo Cyberpunk",
            "Voltar ao Menu Principal"
            ] 
        elif contexto == "Criar_Personagem":
            escolhas = [ 
            "Sandevistan",
            "Monowire",
            "Gorilla Arms",
            "Braço cibernético Cromado",
            "Ligações de Interface",
            "Samson frame",
            "Visão Cibernética",           
            "Voltar ao criador de personagem",
            "Voltar ao Menu Principal"
            ]           
        opcao = menu_escolhas(escolhas,"Info Sobre Implantes Cibernéticos")
        if opcao == "Universo Cyberpunk" or opcao == "Voltar ao criador de personagem":
            return "continuar"
        elif opcao == "Voltar ao Menu Principal":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nIMPLANTES CIBERNÉTICOS")+Style.RESET_ALL)
            print("Voltando ao menu principal.")            
            stop()
            return "menu"
        else:
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nIMPLANTES CIBERNÉTICOS")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+centrar_texto(opcao)+Style.RESET_ALL)
            print(get_descricao_implante(opcao))
            if contexto == "Universo_Cyberpunk":
                escolhas = [ 
                "Implantes Cibernéticos",           
                "Universo Cyberpunk",
                "Voltar ao Menu Principal"
                ]
            elif contexto == "Criar_Personagem":
                escolhas = [ 
                "Implantes Cibernéticos",           
                "Voltar ao criador de personagem",
                "Voltar ao Menu Principal"
                ]            
            opcao = menu_escolhas(escolhas,"")
            if opcao == "Universo Cyberpunk" or opcao == "Voltar ao criador de personagem":
                return "continuar"
            elif opcao == "Voltar ao Menu Principal":
                os.system('cls')
                print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nIMPLANTES CIBERNÉTICOS")+Style.RESET_ALL)
                print("Voltando ao menu principal.")                
                stop()
                return "menu"
            elif opcao == "Implantes Cibernéticos":
                pass

# Exibir info sobre ocupações / papéis na sociedade
def info_ocupacoes(contexto):   
    while (True):
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nOCUPAÇÕES/PAPÉIS NA SOCIEDADE")+Style.RESET_ALL)
        if contexto == "Universo_Cyberpunk":
            escolhas = [ 
            "Corpo",
            "Rockerboy",
            "Gangster",
            "Polícia",
            "Solo",
            "Netrunner",
            "Techie",
            "Media",
            "Fixer",
            "Nomad",           
            "Universo Cyberpunk",
            "Voltar ao Menu Principal"
            ]
        elif contexto == "Criar_Personagem":
            escolhas = [ 
            "Corpo",
            "Rockerboy",
            "Gangster",
            "Polícia",
            "Solo",
            "Netrunner",
            "Techie",
            "Media",
            "Fixer",
            "Nomad",           
            "Voltar ao criador de personagem",
            "Voltar ao Menu Principal"
            ]          
        opcao = menu_escolhas(escolhas,"Info Sobre Ocupações")
        if opcao == "Universo Cyberpunk" or opcao == "Voltar ao criador de personagem":
            return "continuar"
        elif opcao == "Voltar ao Menu Principal":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nOCUPAÇÕES/PAPÉIS NA SOCIEDADE")+Style.RESET_ALL)
            print("Voltando ao menu principal.")
            stop()
            return "menu"
        else:
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nOCUPAÇÕES/PAPÉIS NA SOCIEDADE")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+centrar_texto(opcao)+Style.RESET_ALL)
            print(get_descricao_classe(opcao))
            print(get_descricao_habilidade_classe(opcao))
            if contexto == "Universo_Cyberpunk":
                escolhas = [ 
                "Ocupações / Papéis na sociedade",           
                "Universo Cyberpunk",
                "Voltar ao Menu Principal"
                ]
            elif contexto == "Criar_Personagem":
                escolhas = [ 
                "Ocupações / Papéis na sociedade",           
                "Voltar ao criador de personagem",
                "Voltar ao Menu Principal"
                ]       
            opcao = menu_escolhas(escolhas,"")
            if opcao == "Universo Cyberpunk" or opcao == "Voltar ao criador de personagem":
                return "continuar"
            elif opcao == "Voltar ao Menu Principal":
                os.system('cls')
                print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nOCUPAÇÕES/PAPÉIS NA SOCIEDADE")+Style.RESET_ALL)
                print("Voltando ao menu principal.")
                stop()
                return "menu"
            elif opcao == "Ocupações / Papéis na sociedade":
                pass

# Exibir info sobre ocupações / papéis na sociedade
def info_gangues(contexto):
    while (True):
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nGANGUES")+Style.RESET_ALL)
        if contexto == "Universo_Cyberpunk":
            escolhas = [ 
            "Maelstrom",
            "Valentinos",
            "6th Street",
            "VooDoo Boys",
            "Animals",
            "Tyger Claws",
            "Moxes",
            "Scavengers",
            "Barguest",         
            "Universo Cyberpunk",
            "Voltar ao Menu Principal"
            ] 
        elif contexto == "Criar_Personagem": 
            escolhas = [ 
            "Maelstrom",
            "Valentinos",
            "6th Street",
            "VooDoo Boys",
            "Animals",
            "Tyger Claws",
            "Moxes",
            "Scavengers",
            "Barguest",         
            "Voltar ao criador de personagem",
            "Voltar ao Menu Principal"
            ]           
        opcao = menu_escolhas(escolhas,"Info Sobre Gangues")
        if opcao == "Universo Cyberpunk" or opcao == "Voltar ao criador de personagem":
            return "continuar"
        elif opcao == "Voltar ao Menu Principal":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nGANGUES")+Style.RESET_ALL)
            print("Voltando ao menu principal.")
            stop()
            return "menu"
        else:
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nGANGUES")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+centrar_texto(opcao)+Style.RESET_ALL)
            print(get_descricao_gangue(opcao))
            if contexto == "Universo_Cyberpunk":
                escolhas = [ 
                "Gangues",           
                "Universo Cyberpunk",
                "Voltar ao Menu Principal"
                ] 
            elif contexto == "Criar_Personagem":
                escolhas = [ 
                "Gangues",           
                "Voltar ao criador de personagem",
                "Voltar ao Menu Principal"
                ]            
            opcao = menu_escolhas(escolhas,"")
            if opcao == "Universo Cyberpunk" or opcao == "Voltar ao criador de personagem":
                return "continuar"
            elif opcao == "Voltar ao Menu Principal":
                os.system('cls')
                print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nGANGUES")+Style.RESET_ALL)
                print("Voltando ao menu principal.")
                stop()
                return "menu"
            elif opcao == "Gangues":
                pass

# Exibir info sobre nomad Packs
def info_nomad_packs(contexto):
    while (True):
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nNOMAD PACKS")+Style.RESET_ALL)
        if contexto == "Universo_Cyberpunk":
            escolhas = [ 
            "Wraiths",
            "Aldecaldos",         
            "Universo Cyberpunk",
            "Voltar ao Menu Principal"
            ] 
        elif contexto == "Criar_Personagem":
            escolhas = [ 
            "Wraiths",
            "Aldecaldos",         
            "Voltar ao criador de personagem",
            "Voltar ao Menu Principal"
            ]                       
        opcao = menu_escolhas(escolhas,"Info Sobre Nomad Packs")
        if opcao == "Universo Cyberpunk" or opcao == "Voltar ao criador de personagem":
            return "continuar"
        elif opcao == "Voltar ao Menu Principal":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nNOMAD PACKS")+Style.RESET_ALL)
            print("Voltando ao menu principal.")
            stop()
            return "menu"
        else:
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nNOMAD PACKS")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+centrar_texto(opcao)+Style.RESET_ALL)
            print(get_descricao_pack(opcao))
            if contexto == "Universo_Cyberpunk":
                escolhas = [ 
                "Nomad Packs",           
                "Universo Cyberpunk",
                "Voltar ao Menu Principal"
                ] 
            elif contexto == "Criar_Personagem": 
                escolhas = [ 
                "Nomad Packs",           
                "Voltar ao criador de personagem",
                "Voltar ao Menu Principal"
                ]           
            opcao = menu_escolhas(escolhas,"")
            if opcao == "Universo Cyberpunk" or opcao == "Voltar ao criador de personagem":
                return "continuar"
            elif opcao == "Voltar ao Menu Principal":
                os.system('cls')
                print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nNOMAD PACKS")+Style.RESET_ALL)
                print("Voltando ao menu principal.")                
                stop()
                return "menu"
            elif opcao == "Nomad Packs":
                pass