#File: DetailedNPC.py - Detailed NPC Creator 
#Create Detailed NPC Characters based on Dungeons and Dragons 5e
# Python Ver 3.6.5
# Author:  Andrew Chamberlain
# Date:    4/20/2018
#Last Updated: 5/15/2018
######################################
#
import random

def npc_appearance():
    npc_appearance_list = ["Distinctive jewlery: earrings, necklace, circlet, bracelets", "Piercings",
    "Flamboyant or outlandish cloths", "Formal, clean clothes","Ragged, dirty clothes",
    "Pronounced scar", "Missing teeth", "Missing fingers", "Unusal eye colo (or two different colors)",
    "Tattoos", "Birthmark", "Unusual skin color", "Bald", "Braided beard or hair", "Unusual hair color",
    "Nervous eye twitch", "Distinctive nose", "Distinctive posture (crooked or rigid)", 
    "Exceptionally beautiful", "Exceptionally ugly"]
    npc_appearance_desc = random.choice(npc_appearance_list)
    #NPCAppearanceIndex = npc_appearance_list.index(npc_appearance_desc)
    print("Appearance:",npc_appearance_desc)

def npc_high_ability():
    npc_high_ability_list = ["Strength - powerful, brawny, strong as an ox", "Dexterity - lithe, agile, graceful",
    "Constitution - hardy, hale, healthy", "Intelligence - studious, learned, inquisitive", 
    "Wisdom - perceptive, spiritual, insightful", "Charisma - persuasive, forceful, born leader"]
    npc_high_ability_desc = random.choice(npc_high_ability_list)
    #NPCHighAbilityIndex = npc_high_ability_list.index(npc_high_ability_desc)
    print("High Ability:",npc_high_ability_desc)

def npc_low_ability():
    npc_low_ability_list = ["Strength - feeble, scrawny", "Dexterity - clumsy, fumbling", "Constitution - sickly, pale",
    "Intelligence - dim-witted, slow", "Wisdom - oblivious, absentminded", "Charisma - dull, boring"]
    npc_low_ability_desc = random.choice(npc_low_ability_list)
    #NPCLowAbilityIndex = npc_low_ability_list.index(npc_low_ability_desc)
    print("Low Ability:",npc_low_ability_desc)

def npc_talent():
    npc_talent_list = ["Plays a musical instrument", "Speaks several languages fluently", "Unbelievably lucky", "Perfect memory",
    "Great with animals", "Great with children", "Great at solving puzzles", "Great at one game", "Great at impersonations",
    "Draws beautifully", "Paints beautifully", "Sings beautifully", "Drinks everyone under the table", "Expert carpenter",
    "Expert cook", "Expert dart thrower and rock skipper", "Expert juggler", "Skilled actor and master of disguise", 
    "Skilled dancer", "Knows thieves' cant"]
    npc_talent_desc = random.choice(npc_talent_list)
    #NPCTalentIndex = NPCTalenList.index(npc_talent_desc)
    print("Talent:",npc_talent_desc)

def npc_mannerisms():
    npc_mannerisms_list = ["Prone to singing, whistling, or humming quietly", "Speaks in rhyme or some other peculiar way",
    "Particularly low or high voice", "Slurs words lisps, or stutters", "Enunciates overly clearly", "Speaks loudly", "Whispers",
    "Uses flowery speech or long words", "Uses colorful oaths and exclamations", "Makes constant jokes or puns", "Prone to predictions of doom",
    "Fidgets", "Squints", "Stares into the distance", "Chews something", "Paces", "Taps fingers", "Bites fingernails", "Twirls hair or tugs beard"]
    npc_mannerisms_desc = random.choice(npc_mannerisms_list)
    #NPCMannerismsIndex = npc_mannerisms_list.index(npc_mannerisms_desc)
    print("Mannerisms:",npc_mannerisms_desc)

def npc_interaction():
    npc_interaction_list = ['Argumentative', 'Arrogant', 'Blustering', 'Rude', 'Curios', 'Friendly', 'Honest', 'Hot tempered', 'Irritable', 'Ponderous',
    'Quiet', 'Suspicious']
    npc_interaction_desc = random.choice(npc_interaction_list)
    #NPCInteractionIndex = NPCInteratcionList.index(npc_interaction_desc)
    print("Interactions:",npc_interaction_desc)

def npc_ideals():
    npc_ideal_good = ['Beauty', 'Charity', "Greater good", 'Life', 'Respect']
    npc_ideal_lawful = ['Community', 'Fairness', 'Honor', 'Logic', 'Responsibility', 'Tradition']
    npc_ideal_neutral = ['Balance', 'Knowledge', "Live and let live", 'Moderation', 'Neutrality', 'People']
    npc_ideal_evil = ['Domination', 'Greed', 'Might', 'Pain', 'Retribution', 'Slaughter']
    npc_ideal_chaotic = ['Change', 'Creativity', 'Freedom', 'Independence', 'No limits', 'Whimsy']
    npc_ideal_other = ['Aspiration', 'Discovery', 'Glory', 'Nation', 'Redemption', 'Self-knowledge']
    npc_ideal_random = ["npc_ideal_good", "npc_ideal_lawful", "npc_ideal_neutral", "npc_ideal_evil", 
    "npc_ideal_chaotic", "npc_ideal_other"]
    #####IdealOptions = ['Good', 'Lawful', 'Neutral', 'Evil', 'Chaotic', 'Other', 'Random']####
    ideal_choice = input("Select an ideal: ")
    if ideal_choice.lower() == 'good':
        npc_ideal_desc = random.choice(npc_ideal_good)
        print("Good Ideal:", npc_ideal_desc)
    elif ideal_choice.lower() == 'lawful':
        npc_ideal_desc = random.choice(npc_ideal_lawful)
        print("Lawful Ideal:", npc_ideal_desc)
    elif ideal_choice.lower() == 'neutral':
        npc_ideal_desc = random.choice(npc_ideal_neutral)
        print("Neutral Ideal:", npc_ideal_desc)
    elif ideal_choice.lower() == 'evil':
        npc_ideal_desc = random.choice(npc_ideal_evil)
        print("Evil Ideal:", npc_ideal_desc)
    elif ideal_choice.lower() == 'chaotic':
        npc_ideal_desc = random.choice(npc_ideal_chaotic)
        print("Chaotic Ideal:", npc_ideal_desc)
    elif ideal_choice.lower() == 'other':
        npc_ideal_desc = random.choice(npc_ideal_other)
        print("Other Ideal:", npc_ideal_desc)
    elif ideal_choice.lower() == 'random':
        npc_ideal_random_selection = random.choice(npc_ideal_random)
        if npc_ideal_random_selection == "npc_ideal_good":
            npc_ideal_desc = random.choice(npc_ideal_good)
            print("Good Ideal:", npc_ideal_desc)
        elif npc_ideal_random_selection == "npc_ideal_lawful":
            npc_ideal_desc = random.choice(npc_ideal_lawful)
            print("Lawful Ideal:", npc_ideal_desc)
        elif npc_ideal_random_selection == "npc_ideal_neutral":
            npc_ideal_desc = random.choice(npc_ideal_neutral)
            print("Neutral Ideal:", npc_ideal_desc)
        elif npc_ideal_random_selection == "npc_ideal_evil":
            npc_ideal_desc = random.choice(npc_ideal_evil)
            print("Evil Ideal:", npc_ideal_desc)
        elif npc_ideal_random_selection == "npc_ideal_chaotic":
            npc_ideal_desc = random.choice(npc_ideal_chaotic)
            print("Chaotic Ideal:", npc_ideal_desc)
        elif npc_ideal_random_selection == "NPCIdealOtherc":
            npc_ideal_desc = random.choice(npc_ideal_other)
            print("Other Ideal:", npc_ideal_desc)
        else:
            print("There was an error in your ideals request")
    else:
        print("You did not select an available ideal")

def npc_bond():
    npc_bond_list = ["Dedicated to fulfilling a personal life goal", "Protective of close family members",
    "Protective of colleagues or compatriots", "Loyal to a benefactor, patron, or employer",
    "Captivated by a romantic interest", "Drawn to a special place", "Protective of a sentimental keepsake",
    "Protective of a valuable possesssion", "Out for revenge"]
    npc_bond_desc = random.choice(npc_bond_list)
    #NPCInteractionIndex = NPCInteratcionList.index(npc_interaction_desc)
    print("Bond:",npc_bond_desc)

def npc_flaw():
    npc_flaw_list = ["Forbidden love or susceptibility to romance", "Enjoys decadent pleasures", "Arrogance",
    "Envies another creature's possesssions or station", "Overpowering greed", "Prone to rage",
    "Has a powerful enemy", "Specific phobia", "Shameful or scandalous history", "Secret crime or misdeed",
    "Possession of forbidden lore", "Foolhardy bravery"]
    npc_flaw_desc = random.choice(npc_flaw_list)
    #NPCInteractionIndex = NPCInteratcionList.index(npc_interaction_desc)
    print("Flaw:",npc_flaw_desc)

npc_ideals()
npc_flaw()
npc_bond()
npc_appearance()
npc_mannerisms()
npc_interaction
npc_high_ability()
npc_low_ability()
npc_talent()