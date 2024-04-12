import random # Utilizado para definir os níveis dos personagens aleatoriamente
import pygame # Utilizado nas funções tocar_musica e parar_musica
import pandas as pd # Leitura e escrita de ficheiros csv e criação de dataframes
from InquirerPy import inquirer, get_style # Permite ao utilizador escolher as opções dos menus apenas utilizando as setas do teclado
from Classes_Cyberpunk import * # Importa classes de outro ficheiro
from Animations_Cyberpunk import * # Importa ficheiro de animações para o projeto
from Lore_Cyberpunk import * # Informações sobre o universo Cyberpunk
from Personagens_Cyberpunk import * # Personagens predefinidos do projeto
from Univero_Cyberpunk import * # Aceder à função universo_cyberpunk e outras funções necessárias para a mesma

# Parar o programa durante 5 segundos
def stop():
    for i in range(3,0,-1):
        print(f"{i}...", end=' ',flush=True) # end obriga a terminar o print com um espaço em vez de \n, flush limpa o buffer
        time.sleep(1)

# Tocar música
def tocar_musica(caminho_musica):
    pygame.mixer.init() # Inicializa o mixer
    pygame.mixer.music.load(caminho_musica) # Vai buscar a música consoante o caminho fornecido
    pygame.mixer.music.play(loops=-1, fade_ms=10000) # Começa a tocar, repete infinito, vai aumentando volume durante 10 segundos

# Parar música a tocar no momento
def parar_musica():
    pygame.mixer.music.fadeout(3000) # Começa a diminuir o volume da música até que para por completo

# Implementação de menu de escolha (utilizando o teclado), recebe listas e devolve a escolha do utilizador
def menu_escolhas(escolha,mensagem):
    style = get_style({"question": "bold lightblue"}, style_override=False) # Altera a cor da message
    # Exibe o menu utilizando inquirerPY e devolve (return) a escolha
    return inquirer.select(
        style=style, # Implementa a mudança de cor
        message=mensagem, # Mensagem ou pergunta que aparece antes do menu        
        choices=escolha, # Lista de escolhas disponíveis para o utilizador
        qmark="", # Símbolo de "?" que aparece antes da message.
        amark="", # Símbolo que aparece antes da resposta quando a mesma se torna visível no ecrã
        show_cursor=False, # Não mostrar o cursor no terminal
        transformer=lambda result:"", # Não mostrar a opção selecionada pelo utilizador no ecrã depois de a mesma ser selecionada
        border=True, # Mostrar border à volta do menu
        max_height=100 # Altura do menu (esta opção é dinâmica)
    ).execute()

# Recebe ficheiro CSV e retorna uma dataframe
# Cria ficheiro CSV caso não exista
def carregar_dataframe(ficheiro):    
    cabecalho = ['                name','|  Nível Inicial','|   Nível Máximo','|       Ocupação','|    gang/Pack','|       Implante Cibernético','Informação Adicional']   
    # Confirmar se o ficheiro existe
    try:
        # Tentar ler o ficheiro CSV
        dataframe=pd.read_csv(ficheiro,encoding='utf-8')                
    except FileNotFoundError:        
        # Criar novo DataFrame caso ficheiro não exista         
        dataframe=pd.DataFrame(columns=cabecalho)
        dataframe.to_csv(ficheiro, encoding='utf-8',index=False)
        inserir_dados_ficheiro(Johnny.name,Johnny.initial_level,Johnny.max_level,Johnny.occupation,Johnny.gang,Johnny.cybernetic_implant,Johnny.additional_info) 
        inserir_dados_ficheiro(Morgan.name,Morgan.initial_level,Morgan.max_level,Morgan.occupation,Morgan.gang,Morgan.cybernetic_implant,Morgan.additional_info)
        inserir_dados_ficheiro(Alt.name,Alt.initial_level,Alt.max_level,Alt.occupation,Alt.gang,Alt.cybernetic_implant,Alt.additional_info) 
        inserir_dados_ficheiro(Saburo.name,Saburo.initial_level,Saburo.max_level,Saburo.occupation,Saburo.gang,Saburo.cybernetic_implant,Saburo.additional_info) 
        inserir_dados_ficheiro(Smasher.name,Smasher.initial_level,Smasher.max_level,Smasher.occupation,Smasher.gang,Smasher.cybernetic_implant,Smasher.additional_info) 
        inserir_dados_ficheiro(Rogue.name,Rogue.initial_level,Rogue.max_level,Rogue.occupation,Rogue.gang,Rogue.cybernetic_implant,Rogue.additional_info) 
        inserir_dados_ficheiro(Bartmoss.name,Bartmoss.initial_level,Bartmoss.max_level,Bartmoss.occupation,Bartmoss.gang,Bartmoss.cybernetic_implant,Bartmoss.additional_info) 
        dataframe=pd.read_csv(ficheiro,encoding='utf-8') 
    return dataframe

# Recebe uma dataframe, text1 e text2 
# Exibe o text 1, text 2 e todos os dados desse dataframe excepto a última coluna
def exibir_dataframe_limitada(dataframe,text1,text2):
    print(Fore.BLUE+Style.BRIGHT+center_text(text1)+Style.RESET_ALL)
    print(Fore.BLUE+Style.BRIGHT+center_text(text2)+Style.RESET_ALL)
    dataframe_limitada=dataframe[['                name','|  Nível Inicial','|   Nível Máximo','|       Ocupação','|    gang/Pack','|       Implante Cibernético']] # Cortar a última coluna (informacao_adicional)
    print(Fore.GREEN+Style.BRIGHT+dataframe_limitada.to_string(index=False)+Style.RESET_ALL+"\n")

# Insere dados no ficheiro CSV (variavel constante)
def inserir_dados_ficheiro(name,nivelinicial,nivelmax,occupation,gangue_pack,implante,additional_info):
    FICHEIRO_CSV = 'CyberChar.csv'
    dataframe = carregar_dataframe(FICHEIRO_CSV)           
    # Introdução de novos dados no DataFrame               
    nova_linha = {'                name':name,'|  Nível Inicial':nivelinicial,'|   Nível Máximo':nivelmax,'|       Ocupação':occupation,'|    gang/Pack':gangue_pack,'|       Implante Cibernético':implante,'Informação Adicional':additional_info}
    dataframe.loc[len(dataframe)] = nova_linha    
    # Escrever Dados Novos no Ficheiro
    dataframe.to_csv(FICHEIRO_CSV, encoding='utf-8',index=False)

# Criação de personagem
def criar_personagem():  
    # Gerar e atribuir números aleatórios para níveis do personagem  
    nivelinicial = random.randint(1,10)
    nivelmax = random.randint(15,20) 
    # Iniciação obrigatória de variável que será utilizada mais à frente 
    opcao = ""
    # Carrega ficheiro csv para de seguida extrair os names dos personagens
    FICHEIRO_CSV = 'CyberChar.csv' 
    dataframe = carregar_dataframe(FICHEIRO_CSV)
    # Guardar todos os names presentes no ficheiro csv numa lista (com caracteres pequenos)
    lista_names = dataframe['                name'].str.lower().values 
    # Definir o name do personagem
    while(True):
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+center_text("\nCRIAR NOVO PERSONAGEM")+Style.RESET_ALL)
        print(Fore.BLUE+Style.BRIGHT+center_text("digita 'cancelar' ou pressiona 'Enter' com name em branco para voltar ao menu principal\n")+Style.RESET_ALL)
        if opcao == "invalida":                                        
            print(Fore.RED+Style.BRIGHT+center_text("Erro ao digitar name")+Style.RESET_ALL) 
        elif opcao == "existe":                                        
            print(Fore.RED+Style.BRIGHT+center_text("name já existe")+Style.RESET_ALL) 
        try:       
            name=(input("Digita o name do personagem (até 15 caracteres): ").strip()) # .strip() retira espaços em branco no inicio e fim da string
        except ValueError:
            pass 
        if name.strip().lower() == "cancelar" or name.strip().lower() == '':
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nCRIAR NOVO PERSONAGEM")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+center_text("digita 'cancelar' ou pressiona 'Enter' com name em branco para voltar ao menu principal\n")+Style.RESET_ALL)
            print("Operação Cancelada. Voltando ao menu principal.")
            stop()
            return
        elif name.strip().lower() in lista_names:
            opcao = "existe"
        elif len(name) <= 15 and name.lower() not in lista_names: # Verifica se a string possui menos de 16 caracteres e se o name não é repetido
            break                     
        else:
            opcao = "invalida" 
    # Definir a ocupação do personagem 
    while(True):        
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+center_text("\nOCUPAÇÃO DO PERSONAGEM")+Style.RESET_ALL)
        print(Fore.BLUE+Style.BRIGHT+center_text("opção 'cancelar' volta ao menu principal\n")+Style.RESET_ALL)
        # Lista que contém opções do menu
        escolhas = [            
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
        "Indefinido",
        "Info sobre Ocupações/Papéis",
        "Cancelar"
        ]
        # Exibir o menu utilizando a função menu_escolhas()
        occupation = menu_escolhas(escolhas,"Escolhe a ocupação / papel na sociedade:")
        if occupation == "Cancelar":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nOCUPAÇÃO DO PERSONAGEM")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+center_text("opção 'cancelar' volta ao menu principal\n")+Style.RESET_ALL) 
            print("Operação Cancelada. Voltando ao menu principal.")
            stop()
            return 
        elif occupation == "Corpo":        
            personagem = Corpo(name,nivelinicial,nivelmax)
            break
        elif occupation == "Rockerboy":        
            personagem = Rockerboy(name,nivelinicial,nivelmax)
            break
        elif occupation == "Gangster":
            # Escolha do gang a que o personagem gangster pertence
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nGANGUE DO PERSONAGEM")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+center_text("opção 'cancelar' volta ao menu principal\n")+Style.RESET_ALL)
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
            "Indefinido",
            "Info sobre Gangues",
            "Cancelar"
            ]
            gang = menu_escolhas(escolhas,"Escolhe a gang:")
            if gang == "Cancelar":
                os.system('cls')
                print(Fore.BLUE+Style.BRIGHT+center_text("\nGANGUE DO PERSONAGEM")+Style.RESET_ALL)
                print(Fore.BLUE+Style.BRIGHT+center_text("opção 'cancelar' volta ao menu principal\n")+Style.RESET_ALL)
                print("Operação Cancelada. Voltando ao menu principal.")
                stop()
                return 
            elif gang == "Indefinido":
                gang = "-"
                personagem = Gangster(name,nivelinicial,nivelmax,gang) 
                break
            elif gang == "Info sobre Gangues":
                resultado = info_gangues("Criar_Personagem")
                if resultado == "continuar":
                    continue
                elif resultado == "menu":                    
                    return                          
            else:                             
                personagem = Gangster(name,nivelinicial,nivelmax,gang) 
                break
        elif occupation == "Cop":        
            personagem = Cop(name,nivelinicial,nivelmax)
            break
        elif occupation == "Solo":        
            personagem = Solo(name,nivelinicial,nivelmax)
            break
        elif occupation == "Netrunner":        
            personagem = Netrunner(name,nivelinicial,nivelmax)
            break
        elif occupation == "Techie":        
            personagem = Techie(name,nivelinicial,nivelmax)
            break
        elif occupation == "Media":        
            personagem = Media(name,nivelinicial,nivelmax)
            break
        elif occupation == "Fixer":        
            personagem = Fixer(name,nivelinicial,nivelmax)
            break
        elif occupation == "Nomad":
            # Escolha do pack a que o personagem nomad pertence
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nPACK DO PERSONAGEM")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+center_text("opção 'cancelar' volta ao menu principal\n")+Style.RESET_ALL)
            escolhas = [            
            "Wraiths",
            "Aldecaldos",
            "Indefinido",
            "Info sobre Packs",
            "Cancelar"
            ]
            pack = menu_escolhas(escolhas,"Escolhe o pack nómada:")
            if pack == "Cancelar":
                os.system('cls')
                print(Fore.BLUE+Style.BRIGHT+center_text("\nPACK DO PERSONAGEM")+Style.RESET_ALL)
                print(Fore.BLUE+Style.BRIGHT+center_text("opção 'cancelar' volta ao menu principal\n")+Style.RESET_ALL) 
                print("Operação Cancelada. Voltando ao menu principal.")
                stop()
                return
            elif pack == "Indefinido":
                pack = "-"
                personagem = Nomad(name,nivelinicial,nivelmax,pack)
                break
            elif pack == "Info sobre Packs":
                resultado = info_nomad_packs("Criar_Personagem")
                if resultado == "continuar":
                    continue
                elif resultado == "menu":
                    return 
            else:     
                personagem = Nomad(name,nivelinicial,nivelmax,pack)
                break
        elif occupation == "Indefinido":
            occupation = "-"                    
            personagem = Character(name,nivelinicial,nivelmax)
            break
        elif occupation == "Info sobre Ocupações/Papéis":
            resultado = info_ocupacoes("Criar_Personagem")
            if resultado == "continuar":
                continue
            elif resultado == "menu":
                return  
            
    # Escolha do implante cibernético de destaque 
    while(True):                 
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+center_text("\nIMPLANTE CIBERNÉTICO DO PERSONAGEM")+Style.RESET_ALL)
        print(Fore.BLUE+Style.BRIGHT+center_text("opção 'cancelar' volta ao menu principal\n")+Style.RESET_ALL)
        escolhas = [            
        "Sandevistan",
        "Monowire",
        "Gorilla Arms",
        "Braço cibernético Cromado",
        "Ligações de Interface",
        "Samson frame",
        "Visão Cibernética",
        "Indefinido",
        "Info sobre Implantes Cibernéticos",
        "Cancelar"
        ]
        implante = menu_escolhas(escolhas,"Escolhe o Implante Cibernético de Destaque:")
        if implante == "Cancelar":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nIMPLANTE CIBERNÉTICO DO PERSONAGEM")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+center_text("opção 'cancelar' volta ao menu principal\n")+Style.RESET_ALL)
            print("Operação Cancelada. Voltando ao menu principal.")
            stop()
            return
        elif implante == "Indefinido":
            implante = "-"
            personagem.set_cybernetic_implant(implante)
            break 
        elif implante == "Info sobre Implantes Cibernéticos":
            resultado = info_implantes_ciberneticos("Criar_Personagem")
            if resultado == "continuar":
                continue
            elif resultado == "menu":
                return 
        else:
            personagem.set_cybernetic_implant(implante)            
            break    

    # Inserir informação adicional sobre o personagem em forma de text
    opcao = ""
    while(True):        
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+center_text("\nINFO SOBRE PERSONAGEM")+Style.RESET_ALL)
        print(Fore.BLUE+Style.BRIGHT+center_text("digita 'cancelar' a qualquer momento para voltar ao menu principal\n")+Style.RESET_ALL)  
        if opcao == "invalida":                                                      
            print(Fore.RED+Style.BRIGHT+center_text("Deve conter alguma informação")+Style.RESET_ALL) 
        try:     
            additional_info=(input("Digita um pequeno text que contenha informação adicional sobre o personagem:\n").strip())
        except ValueError:
            pass 
        if additional_info.strip().lower() == "cancelar":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+center_text("\nINFO SOBRE PERSONAGEM")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+center_text("digita 'cancelar' a qualquer momento para voltar ao menu principal\n")+Style.RESET_ALL) 
            print("Operação Cancelada. Voltando ao menu principal.")
            stop()
            return
        elif additional_info != "": 
                personagem.set_additional_info(additional_info)               
                break                   
        else:
            opcao = "invalida"
    if isinstance(personagem,Nomad):
        inserir_dados_ficheiro(personagem.name,personagem.initial_level,personagem.max_level,personagem.occupation,personagem.pack,personagem.cybernetic_implant,personagem.additional_info)
    else:
        inserir_dados_ficheiro(personagem.name,personagem.initial_level,personagem.max_level,personagem.occupation,personagem.gang,personagem.cybernetic_implant,personagem.additional_info) 
    animated_character_created_text()  
    # Conteúdo da função stop() escrito diretamente porque neste caso específico, o text fica centrado no terminal
    for i in range(3,0,-1):
        print("\r",end=" ",flush=True) # \r move o cursor para o início da linha (se não o fizer, center_text distorce o posicionamento do print)
        print(Fore.GREEN+Style.BRIGHT+center_text(f"{i}")+Style.RESET_ALL)
        time.sleep(1) 

# Submenu que apresenta lista de personagens e apresenta algumas opções ao utilizador
def listar_personagens():
    # Iniciação obrigatória de variável que será utilizada mais à frente
    opcao = ""
    while(True):        
        os.system('cls') 
        FICHEIRO_CSV = 'CyberChar.csv'
        text1 = "LISTA DE PERSONAGENS"
        text2 = "digita 'cancelar' ou pressiona 'Enter' com name em branco para voltar ao menu principal\n"
        dataframe = carregar_dataframe(FICHEIRO_CSV)
        exibir_dataframe_limitada(dataframe,text1,text2)
        if opcao == "invalida":                                        
            print(Fore.RED+Style.BRIGHT+center_text("Personagem não encontrado")+Style.RESET_ALL)       
        name_personagem = input("Digita o name de qualquer personagem para ver mais informações: ")
        # Tirar espaços (no início e fim) e uppercase da string
        name_personagem_final = name_personagem.strip().lower()
        # Transferir names da dataframe para uma series
        # Tirar espaços (no início e fim) e uppercase da dataframe
        series_names_dataframe = dataframe['                name'].str.strip().str.lower()
        # Comparação de strings. name_personagem_final existe ou não dentro da series
        name_combina = series_names_dataframe.str.contains(name_personagem_final)  
                        
        if name_personagem_final.strip().lower() == 'cancelar' or name_personagem_final.strip().lower() == '':
            print("\nVoltando ao menu principal.")
            stop()
            return 
        elif any(name_combina):
            resultado = exibir_info_personagem(dataframe,name_combina,text1,text2)
            if resultado == "lista":
                continue
            elif resultado == "menu":
                return            
        else:
            opcao = "invalida"               

# Apresentar Informações sobre personagem específico
def exibir_info_personagem(dataframe,name_combina,text1,text2):    
    dataframe_personagem = dataframe[name_combina].head(1)
    name = dataframe_personagem['                name'].values[0] # Extrair informação (name) da Dataframe
    # Iniciação obrigatória de variável que será utilizada mais à frente
    opcao = ""
    while(True):
        os.system('cls')
        exibir_dataframe_limitada(dataframe,text1,text2)
        # Lista que contém opções do menu
        escolhas = [            
            "Sim",
            "Escolher outro personagem"
        ]
        # Exibir o menu utilizando a função menu_escolhas()
        opcao = menu_escolhas(escolhas,(f"Ver informação sobre '{name}'?"))          
        if opcao == "Sim":                    
            # Extrair restante informação da Dataframe                        
            initial_level = dataframe_personagem['|  Nível Inicial'].values[0]
            max_level = dataframe_personagem['|   Nível Máximo'].values[0]
            occupation = dataframe_personagem['|       Ocupação'].values[0]
            gangue_pack = dataframe_personagem['|    gang/Pack'].values[0]
            implante = dataframe_personagem['|       Implante Cibernético'].values[0]
            additional_info = dataframe_personagem['Informação Adicional'].values[0]
            # Instânciar o personagem de uma forma dinâmica com os dados extraidos e apresentar os dados            
            while(True): 
                os.system('cls')
                # Procurar "occupation" em todas as variáveis, funções e classes globais
                class_ocupacao = globals().get(occupation)

                if occupation == "Gangster":
                    personagem = class_ocupacao(name,initial_level,max_level,gangue_pack)
                    personagem.get_centered_name()
                    personagem.get_description()
                    personagem.set_cybernetic_implant(implante)
                    personagem.get_cybernetic_implant()
                    personagem.set_additional_info(additional_info)
                    personagem.get_additional_info()

                    escolhas = [ 
                    "Info sobre Ocupação",
                    "Info sobre Implante",
                    "Info sobre Habilidade Especial",
                    "Info sobre gang",
                    "Escolher outro personagem",
                    "Voltar ao menu principal"
                    ] 
                    
                elif occupation == "Nomad":
                    personagem = class_ocupacao(name,initial_level,max_level,gangue_pack)
                    personagem.get_centered_name()
                    personagem.get_description()
                    personagem.set_cybernetic_implant(implante)
                    personagem.get_cybernetic_implant()
                    personagem.set_additional_info(additional_info)
                    personagem.get_additional_info()

                    escolhas = [ 
                    "Info sobre Ocupação",
                    "Info sobre Implante",
                    "Info sobre Habilidade Especial",
                    "Info sobre Pack",
                    "Escolher outro personagem",
                    "Voltar ao menu principal"
                    ] 

                elif occupation == "-":
                    personagem = Character(name,initial_level,max_level)
                    personagem.get_centered_name()
                    personagem.get_description()
                    personagem.set_cybernetic_implant(implante)
                    personagem.get_cybernetic_implant()
                    personagem.set_additional_info(additional_info)
                    personagem.get_additional_info()

                    escolhas = [ 
                    "Info sobre Ocupação",
                    "Info sobre Implante",
                    "Info sobre Habilidade Especial",
                    "Escolher outro personagem",
                    "Voltar ao menu principal"
                    ] 

                else:
                    personagem = class_ocupacao(name,initial_level,max_level)
                    personagem.get_centered_name()
                    personagem.get_description()
                    personagem.set_cybernetic_implant(implante)
                    personagem.get_cybernetic_implant()
                    personagem.set_additional_info(additional_info)
                    personagem.get_additional_info() 

                    escolhas = [ 
                    "Info sobre Ocupação",
                    "Info sobre Implante",
                    "Info sobre Habilidade Especial",
                    "Escolher outro personagem",
                    "Voltar ao menu principal"
                    ]

                opcao = menu_escolhas(escolhas,"") 

                if opcao == "Voltar ao menu principal":
                    print("\nVoltando ao menu principal.")
                    stop()
                    return "menu"
                elif opcao == "Escolher outro personagem":
                    return "lista"   
                elif opcao == "Info sobre Ocupação":
                    os.system('cls')
                    personagem.get_centered_name()
                    personagem.get_description()
                    print(get_class_description(occupation))
                    escolhas = [
                    f"Voltar a {name}",
                    "Escolher outro personagem",
                    "Voltar ao menu principal"
                    ]
                    opcao = menu_escolhas(escolhas,"")
                    if opcao == "Voltar ao menu principal":
                        print("\nVoltando ao menu principal.")
                        stop()
                        return "menu"
                    elif opcao == "Escolher outro personagem":
                        return "lista" 
                    elif opcao == f"Voltar a {name}":
                        continue 
                elif opcao == "Info sobre Implante":
                    os.system('cls')
                    personagem.get_centered_name()
                    personagem.get_description()
                    print(get_implant_description(implante))
                    escolhas = [
                    f"Voltar a {name}",
                    "Escolher outro personagem",
                    "Voltar ao menu principal"
                    ]
                    opcao = menu_escolhas(escolhas,"")
                    if opcao == "Voltar ao menu principal":
                        print("\nVoltando ao menu principal.")
                        stop()
                        return "menu"
                    elif opcao == "Escolher outro personagem":
                        return "lista" 
                    elif opcao == f"Voltar a {name}":
                        continue 
                elif opcao == "Info sobre Habilidade Especial":
                    os.system('cls')
                    personagem.get_centered_name()
                    personagem.get_description()
                    print(get_description_habilidade_classe(occupation))
                    escolhas = [
                    f"Voltar a {name}",
                    "Escolher outro personagem",
                    "Voltar ao menu principal"
                    ]
                    opcao = menu_escolhas(escolhas,"")
                    if opcao == "Voltar ao menu principal":
                        print("\nVoltando ao menu principal.")
                        stop()
                        return "menu"
                    elif opcao == "Escolher outro personagem":
                        return "lista" 
                    elif opcao == f"Voltar a {name}":
                        continue 
                elif opcao == "Info sobre gang":
                    os.system('cls')
                    personagem.get_centered_name()
                    personagem.get_description()
                    print(get_description_gangue(gangue_pack))
                    escolhas = [
                    f"Voltar a {name}",
                    "Escolher outro personagem",
                    "Voltar ao menu principal"
                    ]
                    opcao = menu_escolhas(escolhas,"")
                    if opcao == "Voltar ao menu principal":
                        print("\nVoltando ao menu principal.")
                        stop()
                        return "menu"
                    elif opcao == "Escolher outro personagem":
                        return "lista" 
                    elif opcao == f"Voltar a {name}":
                        continue 
                elif opcao == "Info sobre Pack":
                    os.system('cls')
                    personagem.get_centered_name()
                    personagem.get_description()
                    print(get_description_pack(gangue_pack))
                    escolhas = [
                    f"Voltar a {name}",
                    "Escolher outro personagem",
                    "Voltar ao menu principal"
                    ]
                    opcao = menu_escolhas(escolhas,"")
                    if opcao == "Voltar ao menu principal":
                        print("\nVoltando ao menu principal.")
                        stop()
                        return "menu"
                    elif opcao == "Escolher outro personagem":
                        return "lista" 
                    elif opcao == f"Voltar a {name}":
                        continue 
                
        elif opcao == "Escolher outro personagem":
            return "lista"

# Eliminar um personagem escolhido pelo utilizador
def eliminar_personagem(): 
    # Iniciação obrigatória de variável que será utilizada mais à frente   
    opcao = ""    
    while True:
        os.system('cls')
        FICHEIRO_CSV = 'CyberChar.csv'
        text1 = "ELIMINAR PERSONAGEM"
        text2 = "digita 'cancelar' ou pressiona 'Enter' com name em branco para voltar ao menu principal\n"        
        # Exibir uma lista dos personagens
        dataframe = carregar_dataframe(FICHEIRO_CSV)
        exibir_dataframe_limitada(dataframe,text1,text2)
        # Pedir ao utilizador para digitar o name do personagem a ser eliminado 
        if opcao == "invalida":                                        
            print(Fore.RED+Style.BRIGHT+center_text("Personagem não encontrado")+Style.RESET_ALL)
        if opcao == "Não permitido":                                        
            print(Fore.RED+Style.BRIGHT+center_text(f"Não é possível eliminar '{name_personagem}'.")+Style.RESET_ALL)
        try:   
            name_personagem = input("Digita o name do personagem que desejas eliminar: ").strip()
        except ValueError:
            pass 
        # Voltar ao menu principal
        if name_personagem.strip().lower() == "cancelar" or name_personagem.strip().lower() == "":
            print("Operação Cancelada. Voltando ao menu principal.")
            stop()
            return
        # Se existe prosseguir
        elif name_personagem in dataframe['                name'].values:            
            # Confirmar a eliminação
            while True: 
                # Verificar se o name digitado faz parte dos personagens predefinidos
                if name_personagem in personagens_predefinidos:
                    opcao = "Não permitido"
                    break
                os.system('cls')
                exibir_dataframe_limitada(dataframe,text1,text2)
                # Lista que contém opções do menu
                escolhas = [            
                    "Sim",
                    "Não"
                ]
                # Exibir o menu utilizando a função menu_escolhas()
                opcao = menu_escolhas(escolhas,(f"Tens a certeza que pretendes eliminar '{name_personagem}'?"))
                if opcao == 'Sim':
                    # Eliminar o personagem do DataFrame e reescrever o arquivo CSV
                    df_novos_dados = dataframe[dataframe['                name'] != name_personagem]
                    df_novos_dados.to_csv(FICHEIRO_CSV, encoding='utf-8', index=False)
                    print(f"Personagem '{name_personagem}' eliminado com sucesso!")
                    input("\nPressiona Enter para continuar.")
                    break
                elif opcao == 'Não':
                    break                    
        else:
            if opcao != "Não permitido":
                opcao = "invalida"            

# Definição do Main
def main():
    carregar_dataframe('CyberChar.csv') 
    tocar_musica('music1.mp3')   
    while(True):
        os.system('cls') 
        animated_title()  
        # Lista que contém opções do menu
        escolhas = [            
            "Criar Personagem",
            "Listar Personagens",
            "Eliminar Personagem",
            "Universo Cyberpunk",
            "Sair"
        ]
        # Exibir o menu utilizando a função 
        opcao = menu_escolhas(escolhas,"")

        if opcao == "Criar Personagem": 
            criar_personagem()             
        elif opcao == "Listar Personagens":
            listar_personagens()
        elif opcao == "Eliminar Personagem":
            eliminar_personagem()
        elif opcao == "Universo Cyberpunk":
            universo_cyberpunk()
        elif opcao == "Sair":
            parar_musica()            
            print("\nA tua jornada no universo Cyberpunk foi concluída. Voltando à tua realidade.")
            stop()
            exit()

# Correr o Programa Principal
if __name__ == "__main__":
    main()   
