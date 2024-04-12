from Classes_Cyberpunk import * # Project Classes

# Predefined Character List
predefined_characters = ["Johnny Silverhand", "Morgan Blackhand", "Alt Cunningham", "Saburo Arasaka", "Adam Smasher", "Rogue Amendiares", "Rache Bartmoss"]
    
# Object instantiation (predefined characters of the project)
# Predefined Character 1
Johnny=Rockerboy("Johnny Silverhand",10,20)
Johnny.set_cybernetic_implant("Cybernetic Chrome Arm")
info ="""Johnny Silverhand, born Robert John Linder, was a famous and influential rockerboy and lead vocalist of the band Samurai.
As a military veteran, he defined the rockerboy movement as it is known today,
emerging as the leading figure in the fight against the corrupt government of the NUSA and the megacorporations,
often described as a terrorist due to this same struggle.
Despite his charisma and charm, he was also known to be irrational, impulsive, and manipulative.
Silverhand earned his nickname due to the silver left arm that was implanted after losing his true arm in the Second Central American Conflict.
Likely one of the first victims of cyberpsychosis, he became too temperamental.
Described in an interview as driven by his dedication and ambition,
but at the end of the day,
Silverhand is someone who doesn't care much about the people around him as long as they are used to achieve his goals.
Eventually, Silverhand was killed by Adam Smasher during the Night City Holocaust on August 20, 2023.
However, his consciousness was copied and stored on a device (Relic) after his encounter with Smasher, shortly before his death.
This copy is not his real consciousness but rather a digital replica of his personality."""
Johnny.set_additional_info(info)
# Predefined Character 2
Morgan=Solo("Morgan Blackhand",10,20)
Morgan.set_cybernetic_implant("Cybernetic Chrome Arm")
info ="""Morgan Blackhand has a black-chrome anodized cybernetic arm and is characterized by being pragmatic.
Blackhand manages to survive because he is astute and constantly looks after his own interests.
His reputation as one of the best solos is due in part to his ability to capture his targets alive instead of simply eliminating them.
Essentially, Blackhand is considered the "Solo of Solos," with years of experience and successful missions on his resume.
Morgan works for the highest offer, has no personal agenda, and does not aspire to be more than what he already is.
He simply accepts the jobs assigned to him and executes them in the way he deems most appropriate."""
Morgan.set_additional_info(info)
# Predefined Character 3
Alt=Netrunner("Alt Cunningham",10,20)
Alt.set_cybernetic_implant("Interface Links")
info ="""Altiera Cunningham, better known as Alt, was the top Netrunner in Night City during the 2000s and 2010s.
Described as a beautiful and talented woman,
she worked for the ITS Corporation and was the creator of the infamous Soulkiller program.
Cunningham was the girlfriend of the famous rockerboy Johnny Silverhand.
However, her life changed completely when she was kidnapped by the Arasaka Corporation,
which used her to create another version of the Soulkiller program for their own purposes.
This program later became the cause of Alt's demise, making her its first victim.
Currently, her consciousness exists only as a digital ghost on the Net."""
Alt.set_additional_info(info)
# Predefined Character 4
Saburo=Corpo("Saburo Arasaka",10,20)
Saburo.set_cybernetic_implant("?")
info ="""Saburo Arasaka, also known as the Emperor,
went from being a pilot in the Imperial Japanese Navy Air Service
to becoming the corporate god of the 21st century.
A native of Tokyo, he transformed the Arasaka Corporation into one of the largest companies in the world.
Saburo is proud, honorable, and, like a true Samurai Shogun, hungry for power.
Despite his advanced age and physical frailty, Saburo Arasaka remains the genius he always was in his youth.
He never relinquished control over Arasaka, even when his eldest son, Kei, took over as CEO of the Corporation,
remaining as chairman of the board and the true manipulator behind the major corporate decisions.
After decades of building the Arasaka Corporation,
Saburo focused his efforts on bioengineering and mental preservation technology.
He even created a digital copy of his personality at the Arasaka Headquarters in Tokyo.
At 158 years old, he still reigns at the top of Arasaka in 2077,
having built the company into a great empire of his generation.
He is proud, honorable, and relentless."""
Saburo.set_additional_info(info)
# Predefined Character 5
Smasher=Solo("Adam Smasher",10,20)
Smasher.set_cybernetic_implant("Samson frame")
info ="""Adam Smasher, Morgan Blackhand's rival, is a Solo completely transformed into a cyborg.
Employed by Arasaka, by 2077 he reached the position of chief of security and personal bodyguard of Yorinobu Arasaka.
Towering and practically devoid of humanity, Adam underwent a radical transformation after being nearly reduced to nothing by an RPG explosion.
Given the choice between being shut down or undergoing a total conversion to become a cyborg,
Adam opted for the latter, showing little interest in preserving his human side.
Without empathy for others, including his coworkers, Adam is kept alive by Arasaka to eliminate the corporation's enemies,
and can only be described in one way, pure and unrestrained evil."""
Smasher.set_additional_info(info)
# Predefined Character 6
Rogue=Fixer("Rogue Amendiares",10,20)
Rogue.set_cybernetic_implant("Cybernetic Vision")
info ="""Rogue Amendiares was quite famous during the 2010s in Night City.
Later, she became the owner of the famous nightclub Afterlife.
She was widely regarded as the best fixer in the city until 2077."""
Rogue.set_additional_info(info)
# Predefined Character 7
Bartmoss=Netrunner("Rache Bartmoss",10,20)
Bartmoss.set_cybernetic_implant("?")
info ="""Rache Bartmoss was a legendary Netrunner in the early 21st century.
He became famous as the man who caused the DataKrash and destroyed the Net.
He invented the programs Demon and Hound.
Alongside Spider Murphy, he wrote the books "Rache Bartmoss's Guide to the Net" and "Brainware Blowout."""
Bartmoss.set_additional_info(info)