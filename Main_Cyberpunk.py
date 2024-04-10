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
    cabecalho = ['                Nome','|  Nível Inicial','|   Nível Máximo','|       Ocupação','|    Gangue/Pack','|       Implante Cibernético','Informação Adicional']   
    # Confirmar se o ficheiro existe
    try:
        # Tentar ler o ficheiro CSV
        dataframe=pd.read_csv(ficheiro,encoding='utf-8')                
    except FileNotFoundError:        
        # Criar novo DataFrame caso ficheiro não exista         
        dataframe=pd.DataFrame(columns=cabecalho)
        dataframe.to_csv(ficheiro, encoding='utf-8',index=False)
        inserir_dados_ficheiro(Johnny.nome,Johnny.nivel_inicial,Johnny.nivel_max,Johnny.ocupacao,Johnny.gangue,Johnny.implante_cibernetico,Johnny.info_adicional) 
        inserir_dados_ficheiro(Morgan.nome,Morgan.nivel_inicial,Morgan.nivel_max,Morgan.ocupacao,Morgan.gangue,Morgan.implante_cibernetico,Morgan.info_adicional)
        inserir_dados_ficheiro(Alt.nome,Alt.nivel_inicial,Alt.nivel_max,Alt.ocupacao,Alt.gangue,Alt.implante_cibernetico,Alt.info_adicional) 
        inserir_dados_ficheiro(Saburo.nome,Saburo.nivel_inicial,Saburo.nivel_max,Saburo.ocupacao,Saburo.gangue,Saburo.implante_cibernetico,Saburo.info_adicional) 
        inserir_dados_ficheiro(Smasher.nome,Smasher.nivel_inicial,Smasher.nivel_max,Smasher.ocupacao,Smasher.gangue,Smasher.implante_cibernetico,Smasher.info_adicional) 
        inserir_dados_ficheiro(Rogue.nome,Rogue.nivel_inicial,Rogue.nivel_max,Rogue.ocupacao,Rogue.gangue,Rogue.implante_cibernetico,Rogue.info_adicional) 
        inserir_dados_ficheiro(Bartmoss.nome,Bartmoss.nivel_inicial,Bartmoss.nivel_max,Bartmoss.ocupacao,Bartmoss.gangue,Bartmoss.implante_cibernetico,Bartmoss.info_adicional) 
        dataframe=pd.read_csv(ficheiro,encoding='utf-8') 
    return dataframe

# Recebe uma dataframe, texto1 e texto2 
# Exibe o texto 1, texto 2 e todos os dados desse dataframe excepto a última coluna
def exibir_dataframe_limitada(dataframe,texto1,texto2):
    print(Fore.BLUE+Style.BRIGHT+centrar_texto(texto1)+Style.RESET_ALL)
    print(Fore.BLUE+Style.BRIGHT+centrar_texto(texto2)+Style.RESET_ALL)
    dataframe_limitada=dataframe[['                Nome','|  Nível Inicial','|   Nível Máximo','|       Ocupação','|    Gangue/Pack','|       Implante Cibernético']] # Cortar a última coluna (informacao_adicional)
    print(Fore.GREEN+Style.BRIGHT+dataframe_limitada.to_string(index=False)+Style.RESET_ALL+"\n")

# Insere dados no ficheiro CSV (variavel constante)
def inserir_dados_ficheiro(nome,nivelinicial,nivelmax,ocupacao,gangue_pack,implante,info_adicional):
    FICHEIRO_CSV = 'CyberChar.csv'
    dataframe = carregar_dataframe(FICHEIRO_CSV)           
    # Introdução de novos dados no DataFrame               
    nova_linha = {'                Nome':nome,'|  Nível Inicial':nivelinicial,'|   Nível Máximo':nivelmax,'|       Ocupação':ocupacao,'|    Gangue/Pack':gangue_pack,'|       Implante Cibernético':implante,'Informação Adicional':info_adicional}
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
    # Carrega ficheiro csv para de seguida extrair os nomes dos personagens
    FICHEIRO_CSV = 'CyberChar.csv' 
    dataframe = carregar_dataframe(FICHEIRO_CSV)
    # Guardar todos os nomes presentes no ficheiro csv numa lista (com caracteres pequenos)
    lista_nomes = dataframe['                Nome'].str.lower().values 
    # Definir o nome do personagem
    while(True):
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nCRIAR NOVO PERSONAGEM")+Style.RESET_ALL)
        print(Fore.BLUE+Style.BRIGHT+centrar_texto("digita 'cancelar' ou pressiona 'Enter' com nome em branco para voltar ao menu principal\n")+Style.RESET_ALL)
        if opcao == "invalida":                                        
            print(Fore.RED+Style.BRIGHT+centrar_texto("Erro ao digitar nome")+Style.RESET_ALL) 
        elif opcao == "existe":                                        
            print(Fore.RED+Style.BRIGHT+centrar_texto("Nome já existe")+Style.RESET_ALL) 
        try:       
            nome=(input("Digita o nome do personagem (até 15 caracteres): ").strip()) # .strip() retira espaços em branco no inicio e fim da string
        except ValueError:
            pass 
        if nome.strip().lower() == "cancelar" or nome.strip().lower() == '':
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nCRIAR NOVO PERSONAGEM")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("digita 'cancelar' ou pressiona 'Enter' com nome em branco para voltar ao menu principal\n")+Style.RESET_ALL)
            print("Operação Cancelada. Voltando ao menu principal.")
            stop()
            return
        elif nome.strip().lower() in lista_nomes:
            opcao = "existe"
        elif len(nome) <= 15 and nome.lower() not in lista_nomes: # Verifica se a string possui menos de 16 caracteres e se o nome não é repetido
            break                     
        else:
            opcao = "invalida" 
    # Definir a ocupação do personagem 
    while(True):        
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nOCUPAÇÃO DO PERSONAGEM")+Style.RESET_ALL)
        print(Fore.BLUE+Style.BRIGHT+centrar_texto("opção 'cancelar' volta ao menu principal\n")+Style.RESET_ALL)
        # Lista que contém opções do menu
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
        "Indefinido",
        "Info sobre Ocupações/Papéis",
        "Cancelar"
        ]
        # Exibir o menu utilizando a função menu_escolhas()
        ocupacao = menu_escolhas(escolhas,"Escolhe a ocupação / papel na sociedade:")
        if ocupacao == "Cancelar":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nOCUPAÇÃO DO PERSONAGEM")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("opção 'cancelar' volta ao menu principal\n")+Style.RESET_ALL) 
            print("Operação Cancelada. Voltando ao menu principal.")
            stop()
            return 
        elif ocupacao == "Corpo":        
            personagem = Corpo(nome,nivelinicial,nivelmax)
            break
        elif ocupacao == "Rockerboy":        
            personagem = Rockerboy(nome,nivelinicial,nivelmax)
            break
        elif ocupacao == "Gangster":
            # Escolha do gangue a que o personagem gangster pertence
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nGANGUE DO PERSONAGEM")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("opção 'cancelar' volta ao menu principal\n")+Style.RESET_ALL)
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
            gangue = menu_escolhas(escolhas,"Escolhe a gangue:")
            if gangue == "Cancelar":
                os.system('cls')
                print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nGANGUE DO PERSONAGEM")+Style.RESET_ALL)
                print(Fore.BLUE+Style.BRIGHT+centrar_texto("opção 'cancelar' volta ao menu principal\n")+Style.RESET_ALL)
                print("Operação Cancelada. Voltando ao menu principal.")
                stop()
                return 
            elif gangue == "Indefinido":
                gangue = "-"
                personagem = Gangster(nome,nivelinicial,nivelmax,gangue) 
                break
            elif gangue == "Info sobre Gangues":
                resultado = info_gangues("Criar_Personagem")
                if resultado == "continuar":
                    continue
                elif resultado == "menu":                    
                    return                          
            else:                             
                personagem = Gangster(nome,nivelinicial,nivelmax,gangue) 
                break
        elif ocupacao == "Polícia":        
            personagem = Policia(nome,nivelinicial,nivelmax)
            break
        elif ocupacao == "Solo":        
            personagem = Solo(nome,nivelinicial,nivelmax)
            break
        elif ocupacao == "Netrunner":        
            personagem = Netrunner(nome,nivelinicial,nivelmax)
            break
        elif ocupacao == "Techie":        
            personagem = Techie(nome,nivelinicial,nivelmax)
            break
        elif ocupacao == "Media":        
            personagem = Media(nome,nivelinicial,nivelmax)
            break
        elif ocupacao == "Fixer":        
            personagem = Fixer(nome,nivelinicial,nivelmax)
            break
        elif ocupacao == "Nomad":
            # Escolha do pack a que o personagem nomad pertence
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nPACK DO PERSONAGEM")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("opção 'cancelar' volta ao menu principal\n")+Style.RESET_ALL)
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
                print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nPACK DO PERSONAGEM")+Style.RESET_ALL)
                print(Fore.BLUE+Style.BRIGHT+centrar_texto("opção 'cancelar' volta ao menu principal\n")+Style.RESET_ALL) 
                print("Operação Cancelada. Voltando ao menu principal.")
                stop()
                return
            elif pack == "Indefinido":
                pack = "-"
                personagem = Nomad(nome,nivelinicial,nivelmax,pack)
                break
            elif pack == "Info sobre Packs":
                resultado = info_nomad_packs("Criar_Personagem")
                if resultado == "continuar":
                    continue
                elif resultado == "menu":
                    return 
            else:     
                personagem = Nomad(nome,nivelinicial,nivelmax,pack)
                break
        elif ocupacao == "Indefinido":
            ocupacao = "-"                    
            personagem = Personagem(nome,nivelinicial,nivelmax)
            break
        elif ocupacao == "Info sobre Ocupações/Papéis":
            resultado = info_ocupacoes("Criar_Personagem")
            if resultado == "continuar":
                continue
            elif resultado == "menu":
                return  
            
    # Escolha do implante cibernético de destaque 
    while(True):                 
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nIMPLANTE CIBERNÉTICO DO PERSONAGEM")+Style.RESET_ALL)
        print(Fore.BLUE+Style.BRIGHT+centrar_texto("opção 'cancelar' volta ao menu principal\n")+Style.RESET_ALL)
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
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nIMPLANTE CIBERNÉTICO DO PERSONAGEM")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("opção 'cancelar' volta ao menu principal\n")+Style.RESET_ALL)
            print("Operação Cancelada. Voltando ao menu principal.")
            stop()
            return
        elif implante == "Indefinido":
            implante = "-"
            personagem.set_implante_cibernetico(implante)
            break 
        elif implante == "Info sobre Implantes Cibernéticos":
            resultado = info_implantes_ciberneticos("Criar_Personagem")
            if resultado == "continuar":
                continue
            elif resultado == "menu":
                return 
        else:
            personagem.set_implante_cibernetico(implante)            
            break    

    # Inserir informação adicional sobre o personagem em forma de texto
    opcao = ""
    while(True):        
        os.system('cls')
        print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nINFO SOBRE PERSONAGEM")+Style.RESET_ALL)
        print(Fore.BLUE+Style.BRIGHT+centrar_texto("digita 'cancelar' a qualquer momento para voltar ao menu principal\n")+Style.RESET_ALL)  
        if opcao == "invalida":                                                      
            print(Fore.RED+Style.BRIGHT+centrar_texto("Deve conter alguma informação")+Style.RESET_ALL) 
        try:     
            info_adicional=(input("Digita um pequeno texto que contenha informação adicional sobre o personagem:\n").strip())
        except ValueError:
            pass 
        if info_adicional.strip().lower() == "cancelar":
            os.system('cls')
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("\nINFO SOBRE PERSONAGEM")+Style.RESET_ALL)
            print(Fore.BLUE+Style.BRIGHT+centrar_texto("digita 'cancelar' a qualquer momento para voltar ao menu principal\n")+Style.RESET_ALL) 
            print("Operação Cancelada. Voltando ao menu principal.")
            stop()
            return
        elif info_adicional != "": 
                personagem.set_info_adicional(info_adicional)               
                break                   
        else:
            opcao = "invalida"
    if isinstance(personagem,Nomad):
        inserir_dados_ficheiro(personagem.nome,personagem.nivel_inicial,personagem.nivel_max,personagem.ocupacao,personagem.pack,personagem.implante_cibernetico,personagem.info_adicional)
    else:
        inserir_dados_ficheiro(personagem.nome,personagem.nivel_inicial,personagem.nivel_max,personagem.ocupacao,personagem.gangue,personagem.implante_cibernetico,personagem.info_adicional) 
    texto_personagem_criado_animado()  
    # Conteúdo da função stop() escrito diretamente porque neste caso específico, o texto fica centrado no terminal
    for i in range(3,0,-1):
        print("\r",end=" ",flush=True) # \r move o cursor para o início da linha (se não o fizer, centrar_texto distorce o posicionamento do print)
        print(Fore.GREEN+Style.BRIGHT+centrar_texto(f"{i}")+Style.RESET_ALL)
        time.sleep(1) 

# Submenu que apresenta lista de personagens e apresenta algumas opções ao utilizador
def listar_personagens():
    # Iniciação obrigatória de variável que será utilizada mais à frente
    opcao = ""
    while(True):        
        os.system('cls') 
        FICHEIRO_CSV = 'CyberChar.csv'
        texto1 = "LISTA DE PERSONAGENS"
        texto2 = "digita 'cancelar' ou pressiona 'Enter' com nome em branco para voltar ao menu principal\n"
        dataframe = carregar_dataframe(FICHEIRO_CSV)
        exibir_dataframe_limitada(dataframe,texto1,texto2)
        if opcao == "invalida":                                        
            print(Fore.RED+Style.BRIGHT+centrar_texto("Personagem não encontrado")+Style.RESET_ALL)       
        nome_personagem = input("Digita o nome de qualquer personagem para ver mais informações: ")
        # Tirar espaços (no início e fim) e uppercase da string
        nome_personagem_final = nome_personagem.strip().lower()
        # Transferir nomes da dataframe para uma series
        # Tirar espaços (no início e fim) e uppercase da dataframe
        series_nomes_dataframe = dataframe['                Nome'].str.strip().str.lower()
        # Comparação de strings. nome_personagem_final existe ou não dentro da series
        nome_combina = series_nomes_dataframe.str.contains(nome_personagem_final)  
                        
        if nome_personagem_final.strip().lower() == 'cancelar' or nome_personagem_final.strip().lower() == '':
            print("\nVoltando ao menu principal.")
            stop()
            return 
        elif any(nome_combina):
            resultado = exibir_info_personagem(dataframe,nome_combina,texto1,texto2)
            if resultado == "lista":
                continue
            elif resultado == "menu":
                return            
        else:
            opcao = "invalida"               

# Apresentar Informações sobre personagem específico
def exibir_info_personagem(dataframe,nome_combina,texto1,texto2):    
    dataframe_personagem = dataframe[nome_combina].head(1)
    nome = dataframe_personagem['                Nome'].values[0] # Extrair informação (nome) da Dataframe
    # Iniciação obrigatória de variável que será utilizada mais à frente
    opcao = ""
    while(True):
        os.system('cls')
        exibir_dataframe_limitada(dataframe,texto1,texto2)
        # Lista que contém opções do menu
        escolhas = [            
            "Sim",
            "Escolher outro personagem"
        ]
        # Exibir o menu utilizando a função menu_escolhas()
        opcao = menu_escolhas(escolhas,(f"Ver informação sobre '{nome}'?"))          
        if opcao == "Sim":                    
            # Extrair restante informação da Dataframe                        
            nivel_inicial = dataframe_personagem['|  Nível Inicial'].values[0]
            nivel_max = dataframe_personagem['|   Nível Máximo'].values[0]
            ocupacao = dataframe_personagem['|       Ocupação'].values[0]
            gangue_pack = dataframe_personagem['|    Gangue/Pack'].values[0]
            implante = dataframe_personagem['|       Implante Cibernético'].values[0]
            info_adicional = dataframe_personagem['Informação Adicional'].values[0]
            # Instânciar o personagem de uma forma dinâmica com os dados extraidos e apresentar os dados            
            while(True): 
                os.system('cls')
                # Procurar "ocupacao" em todas as variáveis, funções e classes globais
                class_ocupacao = globals().get(ocupacao)

                if ocupacao == "Gangster":
                    personagem = class_ocupacao(nome,nivel_inicial,nivel_max,gangue_pack)
                    personagem.get_nome_centrado()
                    personagem.get_descricao()
                    personagem.set_implante_cibernetico(implante)
                    personagem.get_implante_cibernetico()
                    personagem.set_info_adicional(info_adicional)
                    personagem.get_info_adicional()

                    escolhas = [ 
                    "Info sobre Ocupação",
                    "Info sobre Implante",
                    "Info sobre Habilidade Especial",
                    "Info sobre Gangue",
                    "Escolher outro personagem",
                    "Voltar ao menu principal"
                    ] 
                    
                elif ocupacao == "Nomad":
                    personagem = class_ocupacao(nome,nivel_inicial,nivel_max,gangue_pack)
                    personagem.get_nome_centrado()
                    personagem.get_descricao()
                    personagem.set_implante_cibernetico(implante)
                    personagem.get_implante_cibernetico()
                    personagem.set_info_adicional(info_adicional)
                    personagem.get_info_adicional()

                    escolhas = [ 
                    "Info sobre Ocupação",
                    "Info sobre Implante",
                    "Info sobre Habilidade Especial",
                    "Info sobre Pack",
                    "Escolher outro personagem",
                    "Voltar ao menu principal"
                    ] 

                elif ocupacao == "-":
                    personagem = Personagem(nome,nivel_inicial,nivel_max)
                    personagem.get_nome_centrado()
                    personagem.get_descricao()
                    personagem.set_implante_cibernetico(implante)
                    personagem.get_implante_cibernetico()
                    personagem.set_info_adicional(info_adicional)
                    personagem.get_info_adicional()

                    escolhas = [ 
                    "Info sobre Ocupação",
                    "Info sobre Implante",
                    "Info sobre Habilidade Especial",
                    "Escolher outro personagem",
                    "Voltar ao menu principal"
                    ] 

                else:
                    personagem = class_ocupacao(nome,nivel_inicial,nivel_max)
                    personagem.get_nome_centrado()
                    personagem.get_descricao()
                    personagem.set_implante_cibernetico(implante)
                    personagem.get_implante_cibernetico()
                    personagem.set_info_adicional(info_adicional)
                    personagem.get_info_adicional() 

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
                    personagem.get_nome_centrado()
                    personagem.get_descricao()
                    print(get_descricao_classe(ocupacao))
                    escolhas = [
                    f"Voltar a {nome}",
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
                    elif opcao == f"Voltar a {nome}":
                        continue 
                elif opcao == "Info sobre Implante":
                    os.system('cls')
                    personagem.get_nome_centrado()
                    personagem.get_descricao()
                    print(get_descricao_implante(implante))
                    escolhas = [
                    f"Voltar a {nome}",
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
                    elif opcao == f"Voltar a {nome}":
                        continue 
                elif opcao == "Info sobre Habilidade Especial":
                    os.system('cls')
                    personagem.get_nome_centrado()
                    personagem.get_descricao()
                    print(get_descricao_habilidade_classe(ocupacao))
                    escolhas = [
                    f"Voltar a {nome}",
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
                    elif opcao == f"Voltar a {nome}":
                        continue 
                elif opcao == "Info sobre Gangue":
                    os.system('cls')
                    personagem.get_nome_centrado()
                    personagem.get_descricao()
                    print(get_descricao_gangue(gangue_pack))
                    escolhas = [
                    f"Voltar a {nome}",
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
                    elif opcao == f"Voltar a {nome}":
                        continue 
                elif opcao == "Info sobre Pack":
                    os.system('cls')
                    personagem.get_nome_centrado()
                    personagem.get_descricao()
                    print(get_descricao_pack(gangue_pack))
                    escolhas = [
                    f"Voltar a {nome}",
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
                    elif opcao == f"Voltar a {nome}":
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
        texto1 = "ELIMINAR PERSONAGEM"
        texto2 = "digita 'cancelar' ou pressiona 'Enter' com nome em branco para voltar ao menu principal\n"        
        # Exibir uma lista dos personagens
        dataframe = carregar_dataframe(FICHEIRO_CSV)
        exibir_dataframe_limitada(dataframe,texto1,texto2)
        # Pedir ao utilizador para digitar o nome do personagem a ser eliminado 
        if opcao == "invalida":                                        
            print(Fore.RED+Style.BRIGHT+centrar_texto("Personagem não encontrado")+Style.RESET_ALL)
        if opcao == "Não permitido":                                        
            print(Fore.RED+Style.BRIGHT+centrar_texto(f"Não é possível eliminar '{nome_personagem}'.")+Style.RESET_ALL)
        try:   
            nome_personagem = input("Digita o nome do personagem que desejas eliminar: ").strip()
        except ValueError:
            pass 
        # Voltar ao menu principal
        if nome_personagem.strip().lower() == "cancelar" or nome_personagem.strip().lower() == "":
            print("Operação Cancelada. Voltando ao menu principal.")
            stop()
            return
        # Se existe prosseguir
        elif nome_personagem in dataframe['                Nome'].values:            
            # Confirmar a eliminação
            while True: 
                # Verificar se o nome digitado faz parte dos personagens predefinidos
                if nome_personagem in personagens_predefinidos:
                    opcao = "Não permitido"
                    break
                os.system('cls')
                exibir_dataframe_limitada(dataframe,texto1,texto2)
                # Lista que contém opções do menu
                escolhas = [            
                    "Sim",
                    "Não"
                ]
                # Exibir o menu utilizando a função menu_escolhas()
                opcao = menu_escolhas(escolhas,(f"Tens a certeza que pretendes eliminar '{nome_personagem}'?"))
                if opcao == 'Sim':
                    # Eliminar o personagem do DataFrame e reescrever o arquivo CSV
                    df_novos_dados = dataframe[dataframe['                Nome'] != nome_personagem]
                    df_novos_dados.to_csv(FICHEIRO_CSV, encoding='utf-8', index=False)
                    print(f"Personagem '{nome_personagem}' eliminado com sucesso!")
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
        titulo_animado()  
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
