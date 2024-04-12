from colorama import Fore, Style # Modifies text color and style.

# Function to obtain the description of each implant
def get_implant_description(implant_name):
    description = implant_description.get(implant_name,"No information available")
    return "\n" + Fore.GREEN + Style.BRIGHT + implant_name + Style.RESET_ALL + description

# Function to obtain the description of each class
def get_class_description(class_name):
    description = class_description.get(class_name,"No information available")
    return "\n" + Fore.GREEN + Style.BRIGHT + class_name + Style.RESET_ALL + description

# Function to get description of specific ability from each class
def get_description_class_ability(class_name):
    tuple = class_ability_description.get(class_name,("-","No information available")) # Extract tuple
    ability_name = tuple[0]  # Extract the first tuple element
    ability_description = tuple[1]  # Extract the tuples second element    
    return "\n" + Fore.GREEN + Style.BRIGHT + ability_name + Style.RESET_ALL + ability_description

# Function to get description of each gang
def get_gang_description(gang_name):
    description = gang_description.get(gang_name,"No information available")
    return "\n" + Fore.GREEN + Style.BRIGHT + gang_name + Style.RESET_ALL + description

# Function to obtain description of each pack (nomad)
def get_pack_description(pack_name):
    description = pack_description.get(pack_name,"No information available")
    return "\n" + Fore.GREEN + Style.BRIGHT + pack_name + Style.RESET_ALL + description

# Function to retrieve Cyberpunk Lore / Unique Texts
def get_cyberpunk_lore(lore_name):
    return cyberpunk_lore.get(lore_name)

# Description of each CYBERNETIC IMPLANT
implant_description = {
"Sandevistan":"""
Sandevistan is a cybernetic implant that allows its user to slow down time,
according to their own perception.
To an outside observer, it appears as if the user is simply moving at an extremely fast speed.
This implant has a limited duration of only a few seconds,
but it can be recharged afterwards.
Some modifications allow the user to optimize the Sandevistan, increasing its duration,
reducing its recharge time
and providing other useful benefits.
""",
"Monowire":"""
The Monowire stands out as one of the most powerful and flashy pieces of cyberware
that can be found in the Cyberpunk universe.
This weapon consists of a thin, whip-like wire
that is only one molecule thick.
""",
"Gorilla Arms":"""
It is essential that your punches are powerful enough to quickly defeat your enemies.
To achieve this, we suggest acquiring the Gorilla Arms.
This upgrade considerably amplifies the damage caused by your fists,
allowing you to inflict significant suffering on your opponents.
""",
"Cybernetic Chrome Arm":"""
A cybernetic arm uses synthetic muscle fibers instead of flesh and blood.
They do not tire or feel pain, and are also much stronger and more powerful than normal muscle tissue.
They have tremendous gripping power,
and can easily crush light metals, woods, and plastics.
They can reduce glass and plastic to powder
(though they do not have the ability to turn coal into diamonds!).
""",
"Interface Links":"""
Interface Links can only be installed at a Clinic,
during the installation of a Neural Link.
Interface Links are placed on the wrists or head,
allowing connection to Smartguns, Cyberdecks, heavy equipment, and even driving vehicles without using hands.
It's possible to install multiple Interface Links simultaneously, enabling multiple connections at once.
""",
"Samson frame":"""

Imagine an tireless worker, incredibly strong, and capable of surviving practically any accident.
This is Samson, a full-body conversion.
Designed for construction, loading, and hazmat operations (handling toxic materials and environments),
Samson is as effective as an entire team of workers.
He is equally competent hundreds of meters above ground as a welder on high steel structures,
or hundreds of meters below the Earth's surface in mining tunnels.
Additionally, Samson excels in activities such as forestry, oil drilling, toxic waste disposal, and any other imaginable industrial application.
""",
"Cybernetic Vision":"""
A combination of digital processor and camera, meant to replace human eyes.
Cybernetic Vision is akin to normal vision, but enhanced.
Colors are more vivid, images sharper and this is just the beginning...
"""
}

# Description of each CLASS
class_description = {
"Corpo":"""
Sleek and unscrupulous, "Corpos" or Executives are corporate employees.
Being wealthy and persuasive, they can mobilize favors and resources beyond what most people can even dream of.
""",
"Rockerboy":"""
Rockerboys are rebellious musicians who use music and rebellion to fight against authority.
They closely resemble the punks of the 80s, looking disdainfully at the "sellout" corporates, betrayers of art.
Thanks to their charisma, they can influence, incite, and enchant a large number of people through their musical performances.
""",
"Gangster":"""
During the day, the streets are dominated by corporate executives and workers commuting to work.
But at night, predators emerge from their hideouts among rocks and piles of garbage, and the city comes to life.
Dubbed as street trash, gangsters are actually the rulers of the night in the city.
Whether a small group of a dozen or an army of two hundred, each gang in Night City is as diverse as the street itself.
Chrome, addicts, and aberrations, all mixed into a deadly concoction, abundantly sprinkled with blood.
""",
"Cop":"""
Law Enforcement Agents, or Cops, can range from private detectives to government agents.
As figures of authority, they have the ability to intimidate or control others through their position as law enforcement agents.
""",
"Solo":"""
Solos are hired assassins, bodyguards, and mercenaries.
Thanks to their professionalism and constant training,
they have the ability to detect dangers,
identify traps, and display an almost supernatural ability to avoid harm.
""",
"Netrunner":"""
Netrunners are experienced hackers, but with a cybernetic interface system implanted in their bodies.
They use their brain-computer interface implants
to navigate the Internet in search of systems to hack and information to sell to fixers.
Although anyone can enter the Net (also known as cyberspace),
most cannot use the "Menu".
A set of Applications that allow the Netrunner to Locate and Remote Control.
Execute, Load, Create, and Delete Software.
""",
"Techie":"""
Techies encompass everything from technicians to cybernetics specialists.
They are typically underground techies who perform "off-the-record" jobs.
""",
"Media":"""
Media professionals can range from attention-seeking sensationalists to demagogues,
but you can also find some credible and honest dissenters in a world dominated by corporate-controlled puppets.
As long as they maintain their credibility as relevant journalists,
people believe what they are saying, even if there are no facts to support their claims.
""",
"Fixer":"""
Fixers are intermediaries with strong connections, smugglers, and holders of valuable information.
Thanks to their connections on the streets,
they can locate, acquire, and obtain information about desired people, places, or objects within their area of operation,
which they then sell on the black market.
""",
"Nomad":"""
Nomads were corporate "slaves",
who were fired and ostracized from employment.
Now they roam the roads as travelers and motorcycle gangs.
Due to the harshness of life on the road, they maintain strong family ties.
If a Nomad is in trouble, they can count on their family members to support them.
"""
}

# Description of the SPECIFIC ABILITY of each CLASS (in this case, a dictionary where each key is associated with a tuple)
class_ability_description = {
"Corpo":
("Resources","""
This ability represents the corporate's ability to command resources from the corporation.
It is used as a persuasion skill, based on the scale of the requested resources.
It can include bodyguards, weapons, buildings, money, power, stocks, districts, airplanes, yachts, countries, assassins, firearms, melee weapons,
and much more.
Obviously, the more powerful the corporation, the more resources it can invoke at any given time.
"""),
"Rockerboy":
("Impactful Charisma","""
Rockerboys can influence through the charisma present in their personality.
As they develop their personality and skills, they can affect larger groups and rally followers for requests of greater loyalty.
"""),
"Gangster":
("Streets Voice","""
Gangsters have a special talent for obtaining information and favors from the people inhabiting the streets of Night City.
Whether through intimidation, bribery, or persuasion, they can quickly establish contacts and gain the trust of local residents.
This ability makes them masters at gathering information about the urban environment,
finding valuable goods, or even recruiting unlikely allies for their criminal endeavors.
"""),
"Cop":
("Authority","""
Cops rely on Authority to compel people to do whatever they desire.
Some rely on fear or intimidation, while others simply act as professionals in the execution of their duties.
"""),
"Solo":
("Combat Sense","""
This ability is based on the constant training and professionalism of the Solo.
It allows them to perceive dangers, detect traps, and display an almost supernatural ability to avoid harm.
"""),
"Netrunner":
("Interface","""
An extraordinary ability for interaction and manipulation within cyberspace.
It enables Netrunners to perceive raw data as abstract pseudo-physical objects,
translating information into artificial sensory stimuli.
"""),
"Techie":
("Improvised Adaptation","""
Allows repairing and enhancing equipment, weapons, or cybernetic implants,
as well as finding the necessary materials and equipment to create or fix these items.
"""),
"Media":
("Credibility","""
It's crucial for getting your story heard and taken seriously,
convincing people to share information,
providing access to the places where the story actually unfolds.
The higher your Credibility, the more people you'll be able to persuade
and the easier it will be to convince high-level authorities of the truthfulness of your information.
"""),
"Fixer":
("Streetdeal","""
The fixer's special ability is negotiating a Street Deal.
If the fixer's client accepts the deal, then that client is "on the Run".
Runs are jobs that the Fixer offers to provide their clients with money to buy equipment, supplies, etc.
"""),
"Nomad":
("Family","""
A Nomad can rely on their group for hospitality, protection, and assistance,
but they must reciprocate this help or risk losing status and suffering penalties as a consequence.
""")
}

# Description of each gang
gang_description = {
"Maelstrom":"""
Desperate to become more machine than man, caring little for the consequences.
The Maelstrom push their bodies to the extreme with powerful and highly illegal cybernetic implants.
Smuggling, contract killings, and high-risk robberies are their specialties,
and they are relentlessly skilled at it.
It's best to play by their rules and show some respect,
unless you want their blood-red mechanical eyes to be the last image you'll ever see.
""",
"Valentinos":"""
Loyalty, family, and mutual support are the essence of the Valentinos' creed.
The streets of Heywood are their sanctuary,
adorned with colorful murals and shrines dedicated to their idol, Santa Muerte,
and are also the stage for high-speed races and all-night street parties.
They know how to have fun, but causing trouble in their territory means facing an entire neighborhood.
""",
"6th Street":"""
In the beginning, they were dubbed heroes,
a force that would oppose the corporations and gangs terrorizing the local community.
However, the original vision of their founders has faded.
Now, they dominate Santo Domingo and are as self-serving and self-righteous as the worst that Night City has to offer.
""",
"VooDoo Boys":"""
No one in Night City is as deeply intertwined with the depths of the Net as the Voodoo Boys.
Rooted in Haitian culture and tradition,
these elite netrunners use their mastery in the digital realm to hack into data and information that would otherwise be untouchable.
They are the ideal choice for accessing beyond the Blackwall, but keep your eyes open, because they are very distrustful of strangers.
""",
"Animals":"""

In a city where most rely on cybernetic implants and cutting-edge weapons,
the Animals stand out by maximizing their natural muscular power.
They inject themselves with steroids and supplements, becoming completely and aggressively muscular.
They use their strength to intimidate, extort, and subdue anyone who needs to "learn a lesson".
""",
"Tyger Claws":"""
Japantown is undoubtedly the main territory of the Tyger Claws.
From deeply rooted illicit entertainment in the red-light district
to entirely legitimate services on the surface.
These tattooed gangsters know how to extort money from those seeking pleasure.
Trying to challenge them means risking more than just money.
""",
"Moxes":"""
The Mox may not be as numerous or territorially dominant as other gangs,
but they are a force to be reckoned with.
Under the leadership of sex workers, punks, anarchists, and members of sexual minorities,
inspired by the principles of the late stripper turned strip club owner, Elizabeth 'Lizzie' Borden,
this gang protects its members against violence and abuse.
However, make no mistake in idealizing them.
Their form of protection is not without bloodshed, it's not free, and it's far from devoid of shady activities.
""",
"Scavengers":"""
The Scavengers, or 'Scavs', occupy the lowest tier in Night City.
They scavenge implants, technology, and organs from their victims
after attacking them on the streets and dragging them into dark basements.
They survive by selling their bloody loot on the black market.
Shameless and unscrupulous killers, they target gang members and law-abiding citizens alike.
To a Scavenger, it's all the same.
""",
"Barguest":"""
The men in their ranks range from battle-hardened soldiers with post-traumatic stress
to desperate young street dwellers, dockside smugglers, mercenaries, and swindlers of various specialties.
At the top of the food chain are the soldiers who are part of Hansen's trusted circle, the leader of Dogtown.
Although the streets are often crowded with soldiers, they rarely care about the problems of Dogtown citizens.
However, if you go out into the streets leaving a trail of destruction, they will surely show interest.
The Barghest rarely exposes their heads outside of Dogtown.
It is here that they are treated as sovereigns.
Outside their walls, they are just another heavily armed gang with dangerous weapons.
"""
}

# Description of each PACK (nomad)
pack_description = {
"Wraiths":"""
The Wraiths are an eclectic group of individuals exiled from other nomad groups for violating traditions and other transgressions.
While most nomad families live on the fringes of the law, the Wraiths stand unwaveringly outside it,
rejecting the aesthetic of 'folk warmth' common to true nomad groups.
They conduct raids on armored convoys with modified weapons and missile launchers,
dressing in shades of black and blue, evoking ethereal and spectral images.
Although to city dwellers they are just another nomad tribe,
the Wraiths resemble more mercenaries who happen to share nomadic roots.
""",
"Aldecaldos":"""
When gang violence took the life of Juan Aldecaldo's son,
the father's passionate protests became a beacon for many outraged immigrants in Los Angeles.
They formed a family around him and left the city, adopting the nomadic lifestyle.
The elder Aldecaldo passed away in the following years,
and now the Aldecaldos find themselves camped in the deserts near Night City.
Their caravans transformed into mobile workshops, modified cars, and the ability for secret material collection,
allows them to live on the outskirts of the city,
where they transport contraband for those willing to pay.
"""
}

# Cyberpunk Lore / Unique Texts
cyberpunk_lore = {
"The World of Cyberpunk":"""
The world of Cyberpunk is a dystopian future where megacorporations control almost every aspect of life, from politics to the economy.
A highly technological society where cybernetic implants and virtual reality are part of everyday life,
social inequality is stark, creating a division between the privileged and the underprivileged.
Night City, a decadent metropolis on the west coast of the United States, serves as the main setting.
In this dark and dangerous city, violent gangs fight for control of the streets, while the law enforcement often proves corrupt and ineffective.
In the Cyberpunk universe, individuals take on roles such as mercenaries, hackers, and other fringe figures,
fighting for survival and success in a world where the law of the jungle reigns supreme.
As they explore the dark alleys and gleaming skyscrapers of Night City,
these individuals will encounter deadly challenges, corporate intrigue, and opportunities to make a fortune or lose everything.
With a dark atmosphere and a constant energy pulsing through its streets,
this universe is filled with engaging and thrilling experiences.
The population is part of a dystopian future where the boundaries between human and machine blur with each technological advance.
""",
"Cybernetic Implants":"""
Cybernetic implants are technological devices integrated into the human body,
designed to enhance physical, mental, or sensory performance.
Utilizing advancements in biomedical engineering and nanotechnology,
these implants can offer a wide range of functionalities.
When implanted into the body, these devices can fuse with biological tissues,
becoming an integral part of the organism.
They are controlled through neural interfaces,
allowing for a direct link between the brain and cybernetic systems.
Cybernetic implants represent a significant advancement in human evolution
and are capable of providing capabilities that would be considered impossible.
However, they raise ethical and moral questions about the nature of human identity
and how far we can go in the pursuit of personal enhancement.
"""
}

