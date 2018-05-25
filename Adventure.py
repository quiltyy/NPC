#File: Adventure.py - Adventure Creator 
#Create Adventures based on Dungeons and Dragons 5e
# Python Ver 3.6.5
# Author:  Andrew Chamberlain
# Date:    5/25/2018
#Last Updated: 5/25/2018
######################################
#

import random

def adventure_introduction():
    adventure_introduction_list = ["While traveling in the wilderness, the characters fall into a sinkhole that opens beneath their feet dropping them into the adventure location",
    "While traveling in the wilderness, the cahracters notice the entrance to the adventure location.",
    "While traveling on the road, the characters are attacaked by monsters that flee into the nearby adventure location",
    "The adventurers find a map on a dead body.  In addition to the map setting up the adventure, the adventure's villain wants the map",
    "A mysterious magic item or a cruel villain teleports teh characters to the adventure location.",
    "A stranger approached the caharacters in a tavern and urges them toward the adventure location",
    "A town or village needs volunteers to go to the adventure location", "An NPC the characters care about needs them to go to the adventure location",
    "An NPC the characters must obey orders them to go to the adventure location", "An NPC the characters respect asks them to go to the adventure location",
    "One night, the characters all dream about entering the adventure location", "A ghost appears and terorizes a village.  Research reveals that it can be put to rest only by entering the adventure location"]
    adventure_introduction_description = random.choice(adventure_introduction_list)
    print("Adventure Introduction:\n",adventure_introduction_description)

def dungeon_goals():
    dungeon_goals_list = ["Stop the dungeon's monstrous inhabitants from raiding the surface world.",
    "Foil a villain's evil scheme.", "Destroy a magical threat inside the dungeon.", "Acquire treasure.",
    "Find a particular item for a specific purpose.", "Retrieve a stolen item hidden in the dungeon.",
    "Find information needed for a special purpose.", "Rescue a captive.", "Discover the fate of a previous adventuring party",
    "Find an NPC who disappeared in the area.", "Slay a dragon or some other challenging monster.", "Discover the nature and origin of a strange location or pehnomenon",
    "Pursue fleeing foes taking refuge in the dungeon", "Escape from captivity in the dungeon", "Clear a ruin so it can be rebuilt and reoccupied.",
    "Discover why a villain is interested in the dungeon", "Win a bet or complete a rite of passage by surviving in the dungeon for a certain amount of time.",
    "Parley with a villain in the dungeon.", "Hide from a threat outside the dugeon."]
    dungeon_goals_description = random.choice(dungeon_goals_list)
    print("Dungeon Goals:\n",dungeon_goals_description)

def adventure_climax():
    adventure_climax_list = ["The adventurers confront the main villain and a group of minions in a bloody battle to the finish.",
    "The adventurers chase the villain while dodging obstacles designed to thwart them, leading to a final confrontation in or outside the villain's refuge",
    "The actions of the adventurers or the villain result in a cataclysmic event that the adventurers must escape.",
    "The adventurers race to the site where the villain is bringing a master plan to its conclusion arriving just as the plan is about to be completed",
    "The villain and two or three lieutenants perform separate rites in a large room.  The adventurers must disrupt all the riates at the same time.",
    "An ally betrays the adventurers as they're about to achieve their goal. (Use this climax carefully, and don't overuse it.)",
    "A portal opens to another plane of existence.  Creatures on the other side spill out, forcing the adventurers to close the portal and deal with the villain at the same time.",
    "Traps, hazards, or animated objects turn against the adventurers while the main villain attacks, who attempts to escape in the chaos.",
    "A threat more powerful than the adventurers appears, destroys the main villain, and then turns its attention on the characters.",
    "The adventurers must choose whether to pursue the fleeing main villain or save an NPC they care about or a group of innocents.",
    "The adventurers must discover the main villain's secret weakness before they can hope to defeat the villain."]
    adventure_climax_description = random.choice(adventure_climax_list)
    print("Adventure Climax:\n",adventure_climax_description)

adventure_introduction()
dungeon_goals()
adventure_climax()

