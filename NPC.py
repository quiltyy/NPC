# Python Ver 3.6.5
#/Users/Quilty/Documents/Projects/NPC.py - NPC Creator 
# Author:  Andrew Chamberlain
# Date:    4/20/2018
######################################
#
import random

def NPCAppearance():
    NPCAppearanceList = ["Distinctive jewlery: earrings, necklace, circlet, bracelets", "Piercings",
    "Flamboyant or outlandish cloths", "Formal, clean clothes","Ragged, dirty clothes",
    "Pronounced scar", "Missing teeth", "Missing fingers", "Unusal eye colo (or two different colors)",
    "Tattoos", "Birthmark", "Unusual skin color", "Bald", "Braided beard or hair", "Unusual hair color",
    "Nervous eye twitch", "Distinctive nose", "Distinctive posture (crooked or rigid)", 
    "Exceptionally beautiful", "Exceptionally ugly"]
    NPCAppearanceDesc = random.choice(NPCAppearanceList)
    #NPCAppearanceIndex = NPCAppearanceList.index(NPCAppearanceDesc)
    print(NPCAppearanceDesc)

def NPCHighAbility():
    NPCHighAbilityList = ["Strength - powerful, brawny, strong as an ox", "Dexterity - lithe, agile, graceful",
    "Constitution - hardy, hale, healthy", "Intelligence-studious, learned, inquisitive", 
    "Wisdom - perceptive, spiritual, insightful", "Charisma - persuasive, forceful, born leader"]
    NPCHighAbilityDesc = random.choice(NPCHighAbilityList)
    #NPCHighAbilityIndex = NPCHighAbilityList.index(NPCHighAbilityDesc)
    print(NPCHighAbilityDesc)

def NPCLowAbility():
    NPCLowAbilityList = ["Strength - feeble, scrawny", "Dexterity - clumsy, fumbling", "Constitution - sickly, pale",
    "Intelligence - dim-witted, slow", "Wisdom - oblivious, absentminded", "Charisma - dull, boring"]
    NPCLowAbilityDesc = random.choice(NPCLowAbilityList)
    #NPCLowAbilityIndex = NPCLowAbilityList.index(NPCLowAbilityDesc)
    print(NPCLowAbilityDesc)

def NPCTalent():
    NPCTalentList = ["Plays a musical instrument", "Speaks several languages fluently", "Unbelievably lucky", "Perfect memory",
    "Great with animals", "Great with children", "Great at solving puzzles", "Great at one game", "Great at impersonations",
    "Draws beautifully", "Paints beautifully", "Sings beautifully", "Drinks everyone under the table", "Exper carpenter",
    "Expert cook", "Expert dart thrower and rock skipper", "Expert juggler", "Skilled actor and master of disguise", 
    "Skilled dancer", "Knows thieves' cant"]
    NPCTalentDesc = random.choice(NPCTalentList)
    #NPCTalentIndex = NPCTalenList.index(NPCTalentDesc)
    print(NPCTalentDesc)

def NPCMannerisms():
    NPCMannerismsList = ["Prone to singing, whistling, or humming quietly", "Speaks in rhyme or some other peculiar way",
    "Particularly low or high voice", "Slurs words lisps, or stutters", "Enunciates overly clearly", "Speaks loudly", "Whispers",
    "Uses flowery speech or long words", "Uses colorful oaths and exclamations", "Makes constant jokes or puns", "Prone to predictions of doom",
    "Fidgets", "Squints", "Stares into the distance", "Chews something", "Paces", "Taps fingers", "Bites fingernails", "Twirls hair or tugs beard"]
    NPCMannerismsDesc = random.choice(NPCMannerismsList)
    #NPCMannerismsIndex = NPCMannerismsList.index(NPCMannerismsDesc)
    print(NPCMannerismsDesc)

def NPCInteraction():
    NPCInteractionList = ["Argumentative", "Arrogant", "Blustering", "Rude", "Curios", "Friendly", "Honest", "Hot tempered", "Irritable", "Ponderous",
    "Quiet", "Suspicious"]
    NPCInteractionDesc = random.choice(NPCInteractionList)
    #NPCInteractionIndex = NPCInteratcionList.index(NPCInteractionDesc)
    print(NPCInteractionDesc)

def NPCIdeals():
    NPCGood = ["Beauty", "Charity", "Greater good", "Life", "Respect"]
    NPCLawful = ["Community", "Fairness", "Honor", "Logic", "Responsibility", "Tradition"]
    NPCNeutral = ["Balance", "Knowledge", "Live and let live", "Moderation", "Neutrality", "People"]
    NPCEvil = ["Domination", "Greed", "Might", "Pain", "Retribution", "Slaughter"]
    NPCChaotic = ["Change", "Creativity", "Freedom", "Independence", "No limits", "Whimsy"]
    NPCOther = ["Aspiration", "Discovery", "Glory", "Nation", "Redemption", "Self-knowledge"]

NPCAppearance()
NPCMannerisms()
NPCInteraction
NPCHighAbility()
NPCLowAbility()
NPCTalent()


