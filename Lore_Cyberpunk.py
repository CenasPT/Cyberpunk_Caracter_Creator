from colorama import Fore, Style # Modifica cor e estilo do text.
from Animations_Cyberpunk import center_text # centra o text

# Função para obter descrição de cada implante
def get_descricao_implante(name_implante):
    descricao = descricao_implante.get(name_implante,"Nunhuma informação disponível")
    return "\n" + Fore.GREEN + Style.BRIGHT + name_implante + Style.RESET_ALL + descricao

# Função para obter descrição de cada classe
def get_descricao_classe(name_classe):
    descricao = descricao_classe.get(name_classe,"Nunhuma informação disponível")
    return "\n" + Fore.GREEN + Style.BRIGHT + name_classe + Style.RESET_ALL + descricao

# Função para obter descrição da habilidade específica de cada classe
def get_descricao_habilidade_classe(name_classe):
    tuplo = descricao_habilidade_classe.get(name_classe,("-","Nunhuma informação disponível")) # Extrair o tuplo
    name_habilidade = tuplo[0]  # Extrair o primeiro elemento do tuplo
    descricao_habilidade = tuplo[1]  # Extrair o segundo elemento do tuplo    
    return "\n" + Fore.GREEN + Style.BRIGHT + name_habilidade + Style.RESET_ALL + descricao_habilidade

# Função para obter descrição de cada gang
def get_descricao_gangue(name_gangue):
    descricao = descricao_gangue.get(name_gangue,"Nunhuma informação disponível")
    return "\n" + Fore.GREEN + Style.BRIGHT + name_gangue + Style.RESET_ALL + descricao

# Função para obter descrição de cada pack (nomad)
def get_descricao_pack(name_pack):
    descricao = descricao_pack.get(name_pack,"Nunhuma informação disponível")
    return "\n" + Fore.GREEN + Style.BRIGHT + name_pack + Style.RESET_ALL + descricao

# Função para obter Lore de Cyberpunk / texts singulares
def get_lore_cyberpunk(name_lore):
    return lore_cyberpunk.get(name_lore)

# Descrição de cada IMPLANTE CIBERNÉTICO
descricao_implante = {
"Sandevistan":"""
O Sandevistan é um implante cibernético que permite ao seu utilizador abrandar o tempo,
isto segundo a sua própria percepção.
Quem vê de fora, apenas assiste a um humano extremamente rápido no que diz respeito aos seus reflexos.
Este implante possui um tempo limite de duração de apenas alguns segundos,
podendo ser recarregado posteriormente.
Algumas modificações possibilitam ao utilizador optimizar o Sandevistan,
aumentando a sua duração,
reduzindo o tempo de recarga 
entre outros benefícios úteis.
""",
"Monowire":"""
O Monowire destaca-se como uma das peças cibernéticas mais poderosas e chamativas
que podem ser encontradas no universo Cyberpunk.
Esta arma consiste num fio fino semelhante a um chicote,
com uma espessura de apenas uma molécula.
""",
"Gorilla Arms":"""
É essencial que os teus socos sejam poderosos o suficiente para derrotar rapidamente os teus inimigos.
Para alcançar isso, sugerimos a aquisição dos Gorilla Arms.
Esta melhoria amplifica consideravelmente os estragos causados pelos teus punhos,
permitindo provocar um sofrimento significativo nos teus adversários.
""",
"Braço cibernético Cromado":"""
Um braço cibernético utiliza fibras musculares sintéticas em vez de carne e sangue.
Não se cansam nem sentem dor, sendo também muito mais resistentes e poderosos do que o tecido muscular normal.
Possui um poder de aperto tremendo,
podem facilmente esmagar metais leves, madeiras e plásticos.
Conseguem reduzir vidro e plástico a pó (embora não tenham a capacidade de transformar carvão em diamantes!).
""",
"Ligações de Interface":"""
As Ligações de Interface só podem ser instaladas numa Clínica,
durante a instalação de uma Ligação Neural.
As Ligações de Interface são colocadas nos pulsos ou na cabeça,
permitindo a ligação a Smartguns, Cyberdecks, equipamento pesado e até mesmo conduzir veículos sem usar as mãos.
É possível instalar várias Ligações de Interface ao mesmo tempo, permitindo várias ligações em simultâneo.
""",
"Samson frame":"""
Imagina um trabalhador incansável, incrivelmente forte e capaz de sobreviver a praticamente qualquer acidente.
Este é o Samson, uma conversão corporal completa.
Projetado para trabalhos de construção, carga e operações "hazmat" (onde se lida com materiais e ambientes tóxicos),
o Samson é tão eficaz quanto uma equipa inteira de trabalhadores.
Ele é igualmente competente a centenas de metros acima do solo como soldador em estruturas de aço elevadas,
ou a centenas de metros abaixo da superfície da Terra em túneis de mineração.
Além disso, o Samson também se destaca em atividades como exploração florestal,
perfuração de petróleo, eliminação de resíduos tóxicos e em qualquer outra aplicação industrial imaginável.
""",
"Visão Cibernética":"""
Uma combinação de processador digital e câmera, que serve para substituir os olhos humanos.
A visão cibernética é semelhante à visão normal, mas melhorada.
As cores são mais vivas, as imagens mais nítidas. E isto é apenas o começo...
"""
}

# Descrição de cada CLASSE
descricao_classe = {
"Corpo":"""
Elegantes e sem princípios, os "Corpos" ou Executivos são funcionários de corporações.
Sendo ricos e persuasivos, são capazes de mobilizar favores e recursos para além do que a maioria das pessoas consegue sequer sonhar.
""",
"Rockerboy":"""
Rockerboys são músicos rebeldes que usam a música e a revolta para lutar contra a autoridade.
Assemelham-se muito aos punks dos anos 80, que olham com desdenho para os corporativos "vendidos", traidores da arte.
Graças ao seu carisma, conseguem influenciar, incitar e encantar um grande número de pessoas através dos seus espectáculos musicais.
""",
"Gangster":"""
Durante o dia, as ruas são dominadas pelos executivos corporativos e pelos trabalhadores que se deslocam para o trabalho.
Mas à noite, os predadores saem dos seus esconderijos entre rochas e montes de lixo, e a cidade ganha vida.
Apelidados de lixo das ruas, gangsters são na realidade os soberanos da noite na cidade.
Seja um pequeno grupo de uma dúzia ou um exército de duzentos, cada gang em Night City é tão diverso quanto a própria rua.
Cromados, viciados e aberrantes, todos misturados numa mistura letal, regada abundantemente com sangue.
""",
"Polícia":"""
Os Agentes da Lei, ou Polícias, podem abranger desde detetives privados até agentes governamentais.
Como figuras de autoridade, possuem a capacidade de intimidar ou controlar outros através da sua posição como agentes da lei.
""",
"Solo":"""
Os Solos são assassinos contratados, guarda-costas e mercenários.
Graças ao seu profissionalismo e treino constante,
têm a capacidade de detetar perigos,
identificar armadilhas e exibir uma habilidade quase sobrenatural para evitar danos.
""",
"Netrunner":"""
Os Netrunners são hackers experientes, mas com um sistema de interface cibernetica implantada no seu corpo.
Utilizam os seus implantes de interface cérebro-computador,
navegam pela Internet em busca de sistemas para hackear e informações para vender aos fixers.
Embora qualquer pessoa possa entrar na Net (também conhecida como ciberespaço),
a maioria não consegue utilizar o "Menu".
Um conjunto de Aplicações que permitem ao Netrunner Localizar e Controlar Remotamente.
Executar, Carregar, Criar e Apagar Software.
""",
"Techie":"""
Os Techies (ou Técnicos) abrangem desde técnicos até especialistas em cibernética.
Normalmente, são techies underground, que realizam trabalhos "off-the-record".
""",
"Media":"""
Os profissionais dos media podem ir desde sensacionalistas desesperados por atenção até demagogos,
mas também poderás encontrar alguns dissidentes credíveis e honestos num mundo dominado por fantoches controlados por corporações.
Enquanto mantiverem a sua credibilidade como jornalistas relevantes,
as pessoas acreditam no que estão a dizer, mesmo que não haja factos para sustentar as suas afirmações.
""",
"Fixer":"""
Os Fixers são os intermediários com relações fortes, contrabandistas e detentores de informações precisosas.
Graças às suas ligações nas ruas,
conseguem localizar, adquirir e obter informações sobre pessoas, lugares ou objetos desejados dentro da sua área de atuação,
que de seguida vendem no mercado negro.
""",
"Nomad":"""
Os Nómadas eram "escravos" corporativos,
que foram despedidos e ostracizados do emprego.
Agora percorrem as estradas como viajantes e gangues motociclistas.
Devido à dureza da vida na estrada, mantêm laços familiares fortes.
Se um Nómada estiver em apuros, pode contar com os membros da sua família para o apoiarem.
"""
}

# Descrição da HABILIDADE ESPECÍFICA de cada CLASSE (neste caso, dicionário onde cada chave está associada a um tuplo)
descricao_habilidade_classe = {
"Corpo":
("Recursos","""
Esta habilidade representa a capacidade do corporativo de comandar recursos da corporação.
É utilizada como uma habilidade de persuasão, com base na escala dos recursos solicitados.
Pode incluir guarda-costas, armas, edifícios, dinheiro, poder, ações, distritos, aviões, iates, países, assassinos, armas de fogo, armas brancas e muito mais.
Obviamente, quanto mais poderosa a corporação, mais recursos poderá invocar a qualquer momento.
"""),
"Rockerboy":
("Carisma Impactante","""
Rockerboy consegue influenciar através do carisma presente na sua personalidade.
À medida que desenvolvem a sua personalidade e habilidades, podem afetar grupos maiores e convocar seguidores para pedidos de lealdade de maior envergadura.
"""),
"Gangster":
("Voz das Ruas","""
Os Gangsters têm um talento especial para obter informações e favores das pessoas que habitam as ruas de Night City.
Seja através de intimidação, suborno ou persuasão, conseguem rapidamente estabelecer contactos e ganhar a confiança dos habitantes locais.
Esta habilidade torna-os mestres em reunir informações sobre o ambiente urbano, encontrar mercadorias valiosas ou até mesmo recrutar aliados improváveis para as suas empreitadas criminosas.
"""),
"Polícia":
("Autoridade","""
Os polícias recorrem à Autoridade para obrigar as pessoas a fazer tudo o que desejam.
Alguns baseiam-se no medo ou na intimidação, enquanto outros simplesmente agem como profissionais no cumprimento das suas funções.
"""),
"Solo":
("Sentido de Combate","""
Esta capacidade baseia-se no treino constante e profissionalismo do Solo.
Permite-lhe perceber perigos, detetar armadilhas e exibir uma habilidade quase sobrenatural para evitar danos.
"""),
"Netrunner":
("Interface","""
Uma capacidade extraordinária de interação e manipulação dentro do ciberespaço.
Permite que os Netrunners consigam perceber dados brutos como objetos pseudo-físicos abstratos,
traduzindo informações em estímulos sensoriais artificiais.
"""),
"Techie":
("Adaptação Improvisada","""
Permite reparar e melhorar equipamentos, armas ou implantes cibernéticos,
mas também encontrar os materiais e equipamentos necessários para criar ou consertar esses equipamentos.
"""),
"Media":
("Credibilidade","""
É crucial para fazer com que a sua história seja ouvida e levada a sério,
convencer as pessoas a partilharem informações,
fornecerem acesso aos locais onde a história realmente acontece.
Quanto maior for a Credibilidade, mais pessoas conseguirá persuadir
e mais simples será convencer autoridades de alto nível da veracidade das suas informações.
"""),
"Fixer":
("Streetdeal","""
A habilidade especial do fixer é negociar um Acordo de Rua.
Se o cliente do fixer aceitar o acordo, então esse cliente está "em Run".
As Runs são trabalhos que o Fixer oferece para fornecer aos seus clientes dinheiro para comprar equipamento, provisões, etc.
"""),
"Nomad":
("Família","""
Um Nómada pode recorrer ao seu grupo para hospitalidade, proteção e assistência,
mas tem de retribuir essa ajuda ou perderá estatuto e sofrerá penalizações como consequência.
""")
}

# Descrição de cada gang
descricao_gangue = {
"Maelstrom":"""
Desesperados por se tornarem mais máquina do que homem, sem se importarem com as consequências. 
Os Maelstrom implantam os seus corpos ao extremo com implantes cibernéticos poderosos e altamente ilegais.
Contrabando, assassinatos encomendados e assaltos de alto risco são a sua especialidade e são implacavelmente habilidosos nisso.
É melhor jogares segundo as suas regras e mostrares algum respeito,
se não quiseres que os seus olhos mecânicos vermelho-sangue sejam a última imagem que algum dia verás.
""",
"Valentinos":"""
A lealdade, a família e o apoio mútuo são a essência do credo dos Valentinos.
As ruas de Heywood são o seu refúgio,
adornadas com murais coloridos e santuários dedicados ao seu ídolo, Santa Muerte,
sendo também palco de corridas de alta velocidade e festas de rua que duram toda a noite.
Sabem como se divertir, mas causar problemas no seu território significa enfrentar todo um bairro
""",
"6th Street":"""
No início eram apelidados de heróis,
uma força que se oporia às corporações e gangues que aterrorizavam a comunidade local.
No entanto, a visão original dos seus fundadores desvaneceu-se.
Agora, dominam Santo Domingo e são tão auto-servientes e autojustos como o pior que existe em Night City.
""",
"VooDoo Boys":"""
Ninguém em Night City está tão profundamente entrelaçado com as entranhas da Net como os Voodoo Boys.
Enraizados na cultura e tradição haitianas,
estes netrunners de elite usam a sua mestria no reino digital para hackear dados e informações que de outra forma seriam intocáveis.
São a escolha ideal para aceder para além da Blackwall,
mas mantém os olhos abertos,
porque desconfiam bastante de estranhos.
""",
"Animals":"""
Numa cidade onde a maioria confia em implantes cibernéticos e armas de ponta,
os Animals destacam-se ao maximizar o seu poder muscular natural.
Injetam-se com esteroides e suplementos,
ficando completamente e agressivamente musculados.
Utilizam a sua força para intimidar, extorquir e subjugar qualquer um que precise 'aprender uma lição'.
""",
"Tyger Claws":"""
Japantown é, sem sombra de dúvida, o território principal dos Tyger Claws.
Desde o entretenimento ilícito profundamente enraizado no distrito da luz vermelha até aos serviços totalmente legítimos na superfície.
Estes gangsters tatuados sabem como extorquir dinheiro dos que buscam prazer.
Tentar desafiá-los significa arriscar-se a perder mais do que simplesmente dinheiro.
""",
"Moxes":"""
Os Mox podem não ser tão numerosos ou territorialmente dominantes como outras gangues,
mas constituem uma força a ter em consideração.
Sob a liderança de trabalhadoras do sexo, punks, anarquistas e membros de minorias sexuais,
inspirados pelos princípios da falecida stripper transformada em dona de clube de strip, Elizabeth 'Lizzie' Borden,
este gang protege os seus membros contra a violência e o abuso.
No entanto, não se enganem ao idealizar.
A sua forma de proteção não é isenta de derramamento de sangue,
não é gratuita e está longe de ser desprovida de atividades obscuras.
""",
"Scavengers":"""
Os Scavengers, ou 'Scavs', ocupam o patamar mais baixo em Night City.
Eles recolhem implantes, tecnologia e órgãos das sua vítimas,
depois de os atacar nas ruas e arrastar para porões sombrios.
Sobrevivem vendendo os seus saques sangrentos no mercado negro.
Assassinos sem vergonha e sem escrúpulos,
visam membros de gangues e cidadãos cumpridores da lei de igual modo.
Para um Scavenger, é tudo a mesma coisa.
""",
"Barguest":"""
Os homens nas suas fileiras variam desde soldados endurecidos em batalhas com stress pós-traumático
até jovens desesperados das ruas,
contrabandistas dos cais,
mercenários e vigaristas de várias especialidades.
No topo da cadeia alimentar estão os soldados
que fazem parte do círculo de confiança de Hansen, o líder de Dogtown.
Embora as ruas estejam frequentemente repletas de soldados,
raramente se interessam pelos problemas dos cidadãos de Dogtown.
No entanto, se saíres para as ruas deixando um rasto de destruição,
eles certamente mostrarão interesse.
O Barghest raramente expõe a sua cabeça fora de Dogtown.
É aqui que são tratados como soberanos.
Fora das suas muralhas, são apenas mais um gang armado até aos dentes com armas perigosas.
"""
}

# Descrição de cada PACK (nomad)
descricao_pack = {
"Wraiths":"""
Os Wraiths constituem um grupo eclético de indivíduos exilados de outros grupos nómadas por violação de tradições e outras transgressões.
Enquanto a maioria das famílias nómadas vive nos limites da lei,
os Wraiths posicionam-se de forma inabalável fora da mesma,
rejeitando a estética de 'calor folclórico' comum aos verdadeiros grupos nómadas.
Realizam incursões a comboios armados com armas modificadas e lança-mísseis,
vestem-se com tons de preto e azul, evocando imagens etéreas e espectrais.
Embora para os habitantes da cidade sejam apenas mais uma tribo nómada,
os Wraiths assemelham-se mais a mercenários que, por acaso, partilham raízes nómadas.
""",
"Aldecaldos":"""
Quando a violência entre gangues tirou a vida do filho de Juan Aldecaldo,
os protestos apaixonados do pai tornaram-se um farol para muitos imigrantes indignados em Los Angeles.
Formaram uma família à sua volta e saíram da cidade,
adotando o estilo de vida nómada.
O ancião Aldecaldo veio a falecer nos anos seguintes,
e agora os Aldecaldos encontram-se acampados nos desertos perto de Night City.
As suas caravanas transformadas em oficinas móveis,
carros modificados e a habilidade para a recolha secreta de materiais,
permite-lhes levar uma vida nos arredores da cidade,
onde transportam contrabando para quem estiver disposto a pagar.
"""
}

# Lore de Cyberpunk / texts singulares
lore_cyberpunk = {
"O mundo de Cyberpunk":"""
O mundo de Cyberpunk é um futuro distópico onde megacorporações
controlam quase todos os aspectos da vida, desde a política até à economia.
Uma sociedade altamente tecnológica, onde implantes cibernéticos e realidade virtual fazem parte do dia-a-dia,
a desigualdade social é notória, criando uma divisão entre os privilegiados e os desfavorecidos.
Night City, uma metrópole decadente na costa oeste dos Estados Unidos, serve como o cenário principal.
Nesta cidade sombria e perigosa, gangues violentos disputam as ruas para obter controlo,
enquanto a polícia muitas vezes se mostra corrupta e ineficaz.
No universo de Cyberpunk , indivíduos assumem papéis como mercenários, hackers e outras figuras marginais,
lutando pela sobrevivência e sucesso num mundo onde a lei do mais forte reina soberana.
Ao explorarem os becos sombrios e os arranha-céus brilhantes de Night City,
estes indivíduos encontrarão desafios mortais, intrigas corporativas e oportunidades para fazer fortuna ou perder tudo.
Com uma atmosfera sombria e uma energia constante pulsando pelas suas ruas,
este universo escontra-se repleto de experiências envolventes e emocionantes.
A população faz parte de um futuro distópico onde as fronteiras entre humano e máquina se desvanecem a cada avanço tecnológico.
""",
"Implantes Cibernéticos":"""
Implantes cibernéticos são dispositivos tecnológicos integrados no corpo humano,
concebidos para melhorar o desempenho físico, mental ou sensorial.
Utilizando avanços na engenharia biomédica e na nanotecnologia,
estes implantes podem oferecer uma ampla gama de funcionalidades.
Ao serem implantados no corpo, estes dispositivos podem se unir com os tecidos biológicos,
tornando-se parte integrante do organismo.
São controlados através de interfaces neurais,
o que permite uma ligação direta entre o cérebro e os sistemas cibernéticos.
Os implantes cibernéticos representam um avanço significativo na evolução humana
e são capazes de proporcionar capacidades que seriam consideradas impossíveis.
No entanto, levantam questões éticas e morais sobre a natureza da identidade humana
e até onde podemos ir na busca pelo melhoramento pessoal.
"""
}

