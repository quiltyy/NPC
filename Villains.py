#
######################################
#File: DetailedNPC.py - Detailed NPC Creator 
#Create Detailed NPC Characters based on Dungeons and Dragons 5e
# Python Ver 3.6.5
# Author:  Andrew Chamberlain
# Date:    4/20/2018
#Last Updated: 4/21/2018
######################################
#

import random

def VScheme():
    SchemeImmortality = ["Acquire a legendary item to prolong life", "Ascend to godhood",
    "Become undead or obtain a younger body", "Steal a planar creature's essence"]
    SchemeInfluence = ["Seize a position of power or title", "Win a contest or tournament",
    "Win favor with a powerful individual", "Place a pawn in a position of power"]
    SchemeMagic = ["Obation an ancient artifact", "Build a construct or magical device",
    "Carry out a deity's wishes", "Offer sacrifices to a deity", "Contact a lost deity or power",
    "Open a gate to another world"]
    SchemeMayhem = ["Fullfill an apocalyptic prophecy", "Enact the vengeful will have a god or patron",
    "Spread a vile contagion", "Overthrow a government", "Trigger a natural disaster", 
    "Utterly destroy a bloodlone or clan"]
    SchemePassion = ["Prolong the life of a loved one", "Prove  worthy of another person's love",
    "Raise or restore a dead loved one", "Destroy rivals for another person's affection"]
    SchemePower = ["Conquer a region or incite a rebellion", "Seize control of an army",
    "Become the power behind the throne", "gain the favor of a ruler"]
    SchemeRevenge = ["Avenge a past humiliation or insult", "Avenge a past imprisonment or injury",
    "Avenge the death of a loved one", "Gain the favor of a ruler"]
    SchemeWealth = ["Control natural resources or trade", "Marry into wealth", "Plunder ancient ruins",
    "Retrieve stolen property and punish the theif"]
    ObjectiveChoice = input("Select an objective: ")
    if ObjectiveChoice == 'Immortality':
        SchemeDesc = random.choice(SchemeImmortality)
        print("Objective: Immortality")
        print("Villain Scheme:", SchemeDesc)
    if ObjectiveChoice == 'Influence':
        SchemeDesc = random.choice(SchemeInfluence)
        print("Objective: Influence")
        print("Villain Scheme:", SchemeDesc)
    if ObjectiveChoice == 'Magic':
        SchemeDesc = random.choice(SchemeMagic)
        print("Objective: Magic")
        print("Villain Scheme:", SchemeDesc)
    if ObjectiveChoice == 'Mayhem':
        SchemeDesc = random.choice(SchemeMayhem)
        print("Objective: Mayhem")
        print("Villain Scheme:", SchemeDesc)
    if ObjectiveChoice == 'Passion':
        SchemeDesc = random.choice(SchemePassion)
        print("Objective: Passion")
        print("Villain Scheme:", SchemeDesc)
    if ObjectiveChoice == 'Magic':
        SchemeDesc = random.choice(SchemePower)
        print("Objective: Power")
        print("Villain Scheme:", SchemeDesc)
    if ObjectiveChoice == 'Revenge':
        SchemeDesc = random.choice(SchemeRevenge)
        print("Objective: Revenge")
        print("Villain Scheme:", SchemeDesc)
    if ObjectiveChoice == 'Wealth':
        SchemeDesc = random.choice(SchemeWealth)
        print("Objective: Wealth")
        print("Villain Scheme:", SchemeDesc)
    else:
        print("Please select another objective.")

def VMethods():
    Main = ['Agricultural Devastation', 'Assault or Beatings', 
    'Bounty Hunting or Assassination', 'Captivity or Coercion', 'Confidence Scams',
    'Defamation', 'Dueling', 'Execution', 'Impersonation or Disguise', 'Lying or Perjury',
    'Magical Mayhem', 'Murder', 'Neglect', 'Politics', 'Religion', 'Stalking',
    'Theft or Property Crime', 'Torture', 'Vice', 'Warfare']
    Agriculture = ['Blight', 'Crop', 'Drought', 'Famine']
    Captivity = ['Bribery', 'Enticement', 'Eviction', 'Imprisonment', 'Kidnapping',
    'Legal Intimidation', 'Press Gangs', 'Shackling', 'Threats or Harassment']
    Scams = ['Breach of Contract', 'Cheating', 'Fast Talking', 'Fine Print',
    'Fraud or Swindling', 'Quackery or Tricks']
    Defamation = ['Framing', 'Gossipsing or Slander', 'Humiliation', 'Libel or Insults']
    Execution = ['Beheading', 'Burning at the Stake', 'Burying Alive', 'Crucification',
    'Drawing and Quartering', 'Hanging', 'Impalement', 'Sacrifice (living)']
    Magical = ['Hauntings', 'Illusions', 'Infernal Bargains', 'Mind Control', 'Petrification',
    'Raising or Animating the Dead', 'Summoning Monsters', 'Weather Control']
    Murder = ['Assassination', 'Cannibalism', 'Dismemberment', 'Drowning', 'Electrocution',
    'Euthanasia (involuntary)', 'Disease', 'Proisoning', 'Stabbing', 'Strangulation or Suffocation']
    Politics = ['Betrayal or Treason', 'Conspiracy', 'Espionage or Spying', 'Genocide',
    'Oppression', 'Raising Taxes']
    Religion = ['Curses', 'Desecration', 'False Gods', 'Heresy or Cults']
    Theft = ['Arson', 'Blackmail or Extortion', 'Burglary', 'Counterfeiting', 'Highway Robbery',
    'Looting', 'Mugging', 'Poaching', 'Seizing Property', 'Smuggling']
    Torture = ['Acid', 'Blinding', 'Branding', 'Racking', 'Thumbscrews', 'Whipping']
    Vice = ['Adultery', 'Drugs or Alcohol', 'Gambling', 'Seduction']
    Warfare = ['Ambush', 'Invasion', 'Massacre', 'Mercenaries', 'Rebellion', 'Terrorism']
    RandomMain = random.choice(Main)
    if RandomMain == 'Argricultural Devastation':
        XMethods = random.choice(Agriculture)
        print ('Method:', XMethods)
    if RandomMain == 'Captivity or Coericion':
        XMethods = random.choice(Captivity)
        print ('Method:', XMethods)
    if RandomMain == 'Confidence Scams':
        XMethods = random.choice(Scams)
        print ('Method:', XMethods)
    if RandomMain == 'Defamation':
        XMethods = random.choice(Defamation)
        print ('Method:', XMethods)
    if RandomMain == 'Execution':
        XMethods = random.choice(Execution)
        print ('Method:', XMethods)
    if RandomMain == 'Magical Mayhem':
        XMethods = random.choice(Magical)
        print ('Method:', XMethods)
    if RandomMain == 'Murder':
        XMethods = random.choice(Murder)
        print ('Method:', XMethods)
    if RandomMain == 'Politics':
        XMethods = random.choice(Politics)
        print ('Method:', XMethods)
    if RandomMain == 'Religion':
        XMethods = random.choice(Religion)
        print ('Method:', XMethods)
    if RandomMain == 'Theft or Property Crime':
        XMethods = random.choice(Theft)
        print ('Method:', XMethods)
    if RandomMain == 'Torture':
        XMethods = random.choice(Torture)
        print ('Method:', XMethods)
    if RandomMain == 'Vice':
        XMethods = random.choice(Vice)
        print ('Method:', XMethods)
    if RandomMain == 'Warfare':
        XMethods = random.choice(Warfare)
        print ('Method:', XMethods)
    else:
        print ('Sorry')


VScheme()
VMethods()
