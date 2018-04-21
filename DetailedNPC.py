#File: DetailedNPC.py - Detailed NPC Creator 
#Create Detailed NPC Characters based on Dungeons and Dragons 5e
# Python Ver 3.6.5
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
    print("Appearance:",NPCAppearanceDesc)

def NPCHighAbility():
    NPCHighAbilityList = ["Strength - powerful, brawny, strong as an ox", "Dexterity - lithe, agile, graceful",
    "Constitution - hardy, hale, healthy", "Intelligence - studious, learned, inquisitive", 
    "Wisdom - perceptive, spiritual, insightful", "Charisma - persuasive, forceful, born leader"]
    NPCHighAbilityDesc = random.choice(NPCHighAbilityList)
    #NPCHighAbilityIndex = NPCHighAbilityList.index(NPCHighAbilityDesc)
    print("High Ability:",NPCHighAbilityDesc)

def NPCLowAbility():
    NPCLowAbilityList = ["Strength - feeble, scrawny", "Dexterity - clumsy, fumbling", "Constitution - sickly, pale",
    "Intelligence - dim-witted, slow", "Wisdom - oblivious, absentminded", "Charisma - dull, boring"]
    NPCLowAbilityDesc = random.choice(NPCLowAbilityList)
    #NPCLowAbilityIndex = NPCLowAbilityList.index(NPCLowAbilityDesc)
    print("Low Ability:",NPCLowAbilityDesc)

def NPCTalent():
    NPCTalentList = ["Plays a musical instrument", "Speaks several languages fluently", "Unbelievably lucky", "Perfect memory",
    "Great with animals", "Great with children", "Great at solving puzzles", "Great at one game", "Great at impersonations",
    "Draws beautifully", "Paints beautifully", "Sings beautifully", "Drinks everyone under the table", "Expert carpenter",
    "Expert cook", "Expert dart thrower and rock skipper", "Expert juggler", "Skilled actor and master of disguise", 
    "Skilled dancer", "Knows thieves' cant"]
    NPCTalentDesc = random.choice(NPCTalentList)
    #NPCTalentIndex = NPCTalenList.index(NPCTalentDesc)
    print("Talent:",NPCTalentDesc)

def NPCMannerisms():
    NPCMannerismsList = ["Prone to singing, whistling, or humming quietly", "Speaks in rhyme or some other peculiar way",
    "Particularly low or high voice", "Slurs words lisps, or stutters", "Enunciates overly clearly", "Speaks loudly", "Whispers",
    "Uses flowery speech or long words", "Uses colorful oaths and exclamations", "Makes constant jokes or puns", "Prone to predictions of doom",
    "Fidgets", "Squints", "Stares into the distance", "Chews something", "Paces", "Taps fingers", "Bites fingernails", "Twirls hair or tugs beard"]
    NPCMannerismsDesc = random.choice(NPCMannerismsList)
    #NPCMannerismsIndex = NPCMannerismsList.index(NPCMannerismsDesc)
    print("Mannerisms:",NPCMannerismsDesc)

def NPCInteraction():
    NPCInteractionList = ["Argumentative", "Arrogant", "Blustering", "Rude", "Curios", "Friendly", "Honest", "Hot tempered", "Irritable", "Ponderous",
    "Quiet", "Suspicious"]
    NPCInteractionDesc = random.choice(NPCInteractionList)
    #NPCInteractionIndex = NPCInteratcionList.index(NPCInteractionDesc)
    print("Interactions:",NPCInteractionDesc)

def NPCIdeals():
    NPCIdealGood = ["Beauty", "Charity", "Greater good", "Life", "Respect"]
    NPCIdealLawful = ["Community", "Fairness", "Honor", "Logic", "Responsibility", "Tradition"]
    NPCIdealNeutral = ["Balance", "Knowledge", "Live and let live", "Moderation", "Neutrality", "People"]
    NPCIdealEvil = ["Domination", "Greed", "Might", "Pain", "Retribution", "Slaughter"]
    NPCIdealChaotic = ["Change", "Creativity", "Freedom", "Independence", "No limits", "Whimsy"]
    NPCIdealOther = ["Aspiration", "Discovery", "Glory", "Nation", "Redemption", "Self-knowledge"]
    NPCIdealRandom = ["NPCIdealGood", "NPCIdealLawful", "NPCIdealNeutral", "NPCIdealEvil", 
    "NPCIdealChaotic", "NPCIdealOther"]
    #####IdealOptions = ["Good", "Lawful", "Neutral", "Evil", "Chaotic", "Other", "Random"]####
    IdealChoice = input("Select an ideal: ")
    if IdealChoice == 'Good':
        NPCIdealsDesc = random.choice(NPCIdealGood)
        print("Good Ideal:", NPCIdealsDesc)
    elif IdealChoice == 'Lawful':
        NPCIdealsDesc = random.choice(NPCIdealLawful)
        print("Lawful Ideal:", NPCIdealsDesc)
    elif IdealChoice == 'Neutral':
        NPCIdealsDesc = random.choice(NPCIdealNeutral)
        print("Neutral Ideal:", NPCIdealsDesc)
    elif IdealChoice == 'Evil':
        NPCIdealsDesc = random.choice(NPCIdealEvil)
        print("Evil Ideal:", NPCIdealsDesc)
    elif IdealChoice == 'Chaotic':
        NPCIdealsDesc = random.choice(NPCIdealChaotic)
        print("Chaotic Ideal:", NPCIdealsDesc)
    elif IdealChoice == 'Other':
        NPCIdealsDesc = random.choice(NPCIdealOther)
        print("Other Ideal:", NPCIdealsDesc)
    elif IdealChoice == 'Random':
        NPCIdealRandomSelection = random.choice(NPCIdealRandom)
        if NPCIdealRandomSelection == "NPCIdealGood":
            NPCIdealsDesc = random.choice(NPCIdealGood)
            print("Good Ideal:", NPCIdealsDesc)
        elif NPCIdealRandomSelection == "NPCIdealLawful":
            NPCIdealsDesc = random.choice(NPCIdealLawful)
            print("Lawful Ideal:", NPCIdealsDesc)
        elif NPCIdealRandomSelection == "NPCIdealNeutral":
            NPCIdealsDesc = random.choice(NPCIdealNeutral)
            print("Neutral Ideal:", NPCIdealsDesc)
        elif NPCIdealRandomSelection == "NPCIdealEvil":
            NPCIdealsDesc = random.choice(NPCIdealEvil)
            print("Evil Ideal:", NPCIdealsDesc)
        elif NPCIdealRandomSelection == "NPCIdealChaotic":
            NPCIdealsDesc = random.choice(NPCIdealChaotic)
            print("Chaotic Ideal:", NPCIdealsDesc)
        elif NPCIdealRandomSelection == "NPCIdealOtherc":
            NPCIdealsDesc = random.choice(NPCIdealOther)
            print("Other Ideal:", NPCIdealsDesc)
        else:
            print("There was an error in your ideals request")
    else:
        print("You did not select an available ideal")

NPCIdeals()
NPCAppearance()
NPCMannerisms()
NPCInteraction
NPCHighAbility()
NPCLowAbility()
NPCTalent()



