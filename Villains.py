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

VScheme()
