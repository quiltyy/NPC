#
######################################
#File: DetailedNPC.py - Detailed NPC Creator 
#Create Detailed NPC Characters based on Dungeons and Dragons 5e
# Python Ver 3.6.5
# Author:  Andrew Chamberlain
# Date:    4/20/2018
#Last Updated: 5/15/2018
######################################
#

import random

def vscheme():
    scheme_immortality = ["Acquire a legendary item to prolong life", "Ascend to godhood",
    "Become undead or obtain a younger body", "Steal a planar creature's essence"]
    scheme_influence = ["Seize a position of power or title", "Win a contest or tournament",
    "Win favor with a powerful individual", "Place a pawn in a position of power"]
    scheme_magic = ["Obtain an ancient artifact", "Build a construct or magical device",
    "Carry out a deity's wishes", "Offer sacrifices to a deity", "Contact a lost deity or power",
    "Open a gate to another world"]
    scheme_mayhem = ["Fullfill an apocalyptic prophecy", "Enact the vengeful will have a god or patron",
    "Spread a vile contagion", "Overthrow a government", "Trigger a natural disaster", 
    "Utterly destroy a bloodlone or clan"]
    scheme_passion = ["Prolong the life of a loved one", "Prove  worthy of another person's love",
    "Raise or restore a dead loved one", "Destroy rivals for another person's affection"]
    scheme_power = ["Conquer a region or incite a rebellion", "Seize control of an army",
    "Become the power behind the throne", "gain the favor of a ruler"]
    scheme_revenge = ["Avenge a past humiliation or insult", "Avenge a past imprisonment or injury",
    "Avenge the death of a loved one", "Gain the favor of a ruler"]
    scheme_wealth = ["Control natural resources or trade", "Marry into wealth", "Plunder ancient ruins",
    "Retrieve stolen property and punish the theif"]
    objective_choice = input("Select an objective: ")
    if objective_choice.lower() == 'immortality':
        SchemeDesc = random.choice(scheme_immortality)
        print("Objective: Immortality")
        print("Villain Scheme:", SchemeDesc)
    elif objective_choice.lower() == 'influence':
        SchemeDesc = random.choice(scheme_influence)
        print("Objective: Influence")
        print("Villain Scheme:", SchemeDesc)
    elif objective_choice.lower() == 'magic':
        SchemeDesc = random.choice(scheme_magic)
        print("Objective: Magic")
        print("Villain Scheme:", SchemeDesc)
    elif objective_choice.lower() == 'mayhem':
        SchemeDesc = random.choice(scheme_mayhem)
        print("Objective: Mayhem")
        print("Villain Scheme:", SchemeDesc)
    elif objective_choice == 'passion':
        SchemeDesc = random.choice(scheme_passion)
        print("Objective: Passion")
        print("Villain Scheme:", SchemeDesc)
    elif objective_choice.lower() == 'power':
        SchemeDesc = random.choice(scheme_power)
        print("Objective: Power")
        print("Villain Scheme:", SchemeDesc)
    elif objective_choice.lower() == 'revenge':
        SchemeDesc = random.choice(scheme_revenge)
        print("Objective: Revenge")
        print("Villain Scheme:", SchemeDesc)
    elif objective_choice.lower() == 'wealth':
        SchemeDesc = random.choice(scheme_wealth)
        print("Objective: Wealth")
        print("Villain Scheme:", SchemeDesc)
    else:
        print("Please select another objective.")

def vmethods():
    main = ["Agricultural Devastation", "Assault or Beatings", 
    "Bounty Hunting or Assassination", "Captivity or Coercion", "Confidence Scams",
    'Defamation', 'Dueling', 'Execution', 'Impersonation or Disguise', 'Lying or Perjury',
    'Magical Mayhem', 'Murder', 'Neglect', 'Politics', 'Religion', 'Stalking',
    "Theft or Property Crime", 'Torture', 'Vice', 'Warfare']
    agriculture = ['Blight', 'Crop', 'Drought', 'Famine']
    captivity = ['Bribery', 'Enticement', 'Eviction', 'Imprisonment', 'Kidnapping',
    "Legal Intimidation", "Press Gangs", 'Shackling', "Threats or Harassment"]
    scams = ["Breach of Contract", 'Cheating', 'Fast Talking', 'Fine Print',
    "Fraud or Swindling", "Quackery or Tricks"]
    defamation = ['Framing', "Gossipsing or Slander", 'Humiliation', "Libel or Insults"]
    execution = ['Beheading', "Burning at the Stake", "Burying Alive", 'Crucification',
    "Drawing and Quartering", 'Hanging', 'Impalement', "Sacrifice (living)"]
    magical = ['Hauntings', 'Illusions', "Infernal Bargains", "Mind Control", 'Petrification',
    "Raising or Animating the Dead", "Summoning Monsters", "Weather Control"]
    murder = ['Assassination', 'Cannibalism', 'Dismemberment', 'Drowning', 'Electrocution',
    "Euthanasia (involuntary)", 'Disease', 'Proisoning', 'Stabbing', "Strangulation or Suffocation"]
    politics = ["Betrayal or Treason", 'Conspiracy', "Espionage or Spying", 'Genocide',
    'Oppression', "Raising Taxes"]
    religion = ['Curses', 'Desecration', "False Gods", "Heresy or Cults"]
    theft = ['Arson', "Blackmail or Extortion", 'Burglary', 'Counterfeiting', "Highway Robbery",
    'Looting', 'Mugging', 'Poaching', "Seizing Property", 'Smuggling']
    torture = ['Acid', 'Blinding', 'Branding', 'Racking', 'Thumbscrews', 'Whipping']
    vice = ['Adultery', "Drugs or Alcohol", 'Gambling', 'Seduction']
    warfare = ['Ambush', 'Invasion', 'Massacre', 'Mercenaries', 'Rebellion', 'Terrorism']
    random_main = random.choice(main)
    if random_main == "Argricultural Devastation":
        v_methods = random.choice(agriculture)
        print ("Method:", v_methods)
    elif random_main == "Captivity or Coericion":
        v_methods = random.choice(captivity)
        print ("Method:", v_methods)
    elif random_main == "Confidence Scams":
        v_methods = random.choice(scams)
        print ("Method:", v_methods)
    elif random_main == 'Defamation':
        v_methods = random.choice(defamation)
        print ("Method:", v_methods)
    elif random_main == 'Execution':
        v_methods = random.choice(execution)
        print ("Method:", v_methods)
    elif random_main == "Magical Mayhem":
        v_methods = random.choice(magical)
        print ("Method:", v_methods)
    elif random_main == 'Murder':
        v_methods = random.choice(murder)
        print ("Method:", v_methods)
    elif random_main == 'Politics':
        v_methods = random.choice(politics)
        print ("Method:", v_methods)
    elif random_main == 'Religion':
        v_methods = random.choice(religion)
        print ("Method:", v_methods)
    elif random_main == "Theft or Property Crime":
        v_methods = random.choice(theft)
        print ("Method:", v_methods)
    elif random_main == 'Torture':
        v_methods = random.choice(torture)
        print ("Method:", v_methods)
    elif random_main == 'Vice':
        v_methods = random.choice(vice)
        print ("Method:", v_methods)
    elif random_main == 'Warfare':
        v_methods = random.choice(warfare)
        print ("Method:", v_methods)
    else:
        print ("Method:", random_main)

def vweakness():
    weakness = ["A hidden object holds the villain's soul", "The villain's power is broken if the death of it's true love is avneged",
    "The villain is weakened in the presence of a particular artifact", "A special weapon deals extra daamge when used against the villain",
    "The villain is destroyed if it speaks it's true name", "An ancient prophecy or riddle reveals how the villain can be overthrown",
    "The villain falls when an ancient enemy forgives it's past actions", "The villain loses it's power if a mystic bargain it struck long ago is completed"]
    print ("Weakness: ", random.choice(weakness))

def vclass():
    class_list = ['Barbarian', 'Bard', "Death Domain Cleric", 'Druid', 'Fighter', 
    'Monk', 'Oathbreaker Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
    print ("Class: ", random.choice(class_list))

vscheme()
vclass()
vmethods()
vweakness()
