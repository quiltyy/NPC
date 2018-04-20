# Python Ver 3.6.5
#/Users/Quilty/Documents/Projects/NPC.py - NPC Creator 
# Author:  Andrew Chamberlain
# Date:    4/20/2018
######################################
#
import random

def diceroll(dice):
d100 = random.randint(1,100)
d20 = random.randint(1,20)
d12 = random.randint(1,12)
d10 = random.randint(0,9)
d8 = random.randint(1,8)
d6 = random.randint(1,6)
d4 = random.randint(1,4)

def NPCAppearance():
    NPCAppearanceList = ["Distinctive jewlery: earrings, necklace, circlet, bracelets", "Piercings",
    "Flamboyant or outlandish cloths", "Formal, clean clothes","Ragged, dirty clothes",
    "Pronounced scar", "Missing teeth", "Missing fingers", "Unusal eye colo (or two different colors)",
    "Tattoos", "Birthmark", "Unusual skin color", "Bald", "Braided beard or hair", "Unusual hair color",
    "Nervous eye twitch", "Distinctive nose", "Distinctive posture (crooked or rigid)", 
    "Exceptionally beautiful", "Exceptionally ugly"]

def NPCHighAbility():
    NPCHighAbilityList = ["Strength - powerful, brawny, strong as an ox", "Dexterity - lithe, agile, graceful",
    "Constitution - hardy, hale, healthy", "Intelligence-studious, learned, inquisitive", 
    "Wisdom - perceptive, spiritual, insightful", "Charisma - persuasive, forceful, born leader"]
    NPCHighAbilityDesc = random.choice(NPCHighAbilityList)
    NPCHighAbilityIndex = NPCHighAbilityList.index(NPCHighAbilityDesc) 

def NPCLowAbility():
    NPCLowAbilityList = ["Strength - feeble, scrawny", "Dexterity - clumsy, fumbling", "Constitution - sickly, pale",
    "Intelligence - dim-witted, slow", "Wisdom - oblivious, absentminded", "Charisma - dull, boring"]
    NPCLowAbilityDesc = random.choice(NPCLowAbilityList)
    NPCLowAbilityIndex = NPCLowAbilityList.index(NPCLowAbilityDesc)

def NPCTalent():
    NPCTalenList = ["Plays a musical instrument", "Speaks several languages fluently", "Unbelievably lucky", "Perfect memory",
    "Great with animals", "Great with children", "Great at solving puzzles", "Great at one game", "Great at impersonations",
    "Draws beautifully", "Paints beautifully", "Sings beautifully", "Drinks everyone under the table", "Exper carpenter",
    "Expert cook", "Expert dart thrower and rock skipper", "Expert juggler", "Skilled actor and master of disguise", 
    "Skilled dancer", "Knows thieves' cant"]
    NPCTalentDesc = random.choice(NPCTalent)
    NPCTalentIndex = NPCTalenList.index(NPCTalentDesc)

