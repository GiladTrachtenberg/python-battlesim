import random

# Define the attributes of the soldiers
SOLDIER_ATTRIBUTES = {
    "tier_1": {
        "class": "cavalry", "health": 100, "attack": 10, "defense": 10,
        "preferred_distance": "close",
    },
    "tier_2": {
        "class": "archers", "health": 200, "attack": 20, "defense": 20,
        "preferred_distance": "far",
    },
    "tier_3": {
        "class": "infantry", "health": 300, "attack": 30, "defense": 30,
        "preferred_distance": "close",
    },
    "tier_4": {
        "class": "cavalry", "health": 400, "attack": 40, "defense": 40,
        "preferred_distance": "far",
    },
    "tier_5": {
        "class": "archers", "health": 500, "attack": 50, "defense": 50,
        "preferred_distance": "close",
    },
}

# Define the class advantages
CLASS_ADVANTAGES = {
    "cavalry": {"infantry": 1.2, "archers": 1.2},
    "archers": {"infantry": 1.2},
    "infantry": {"cavalry": 1.2},
}

# Define the terrain advantages
TERRAIN_ADVANTAGES = {
    "height_advantage": {"attack": 1.2, "defense": 1.2},
    "height_disadvantage": {"attack": 0.8, "defense": 0.8},
}

def calculate_attack(attacker, defender, terrain_advantage, technical_advantage, class_advantage, distance_multiplier, commander_multiplier):
    """Calculate the attack damage dealt by the attacker to the defender."""
    attack_damage = attacker["attack"] * terrain_advantage * technical_advantage * class_advantage * distance_multiplier * commander_multiplier
    return attack_damage

def calculate_defense(defender, attacker, terrain_advantage, technical_advantage, class_advantage, distance_multiplier, commander_multiplier):
    """Calculate the defense absorbed by the defender from the attacker's attack."""
    defense = defender["defense"] * terrain_advantage * technical_advantage * class_advantage * distance_multiplier * commander_multiplier
    return defense


def calculate_distance_multiplier(attacker, defender):
    """Calculate the distance multiplier based on the preferred distances of the attacker and the defender."""
    attacker_preferred_distance = attacker["preferred_distance"]
    defender_preferred_distance = defender["preferred_distance"]
    if attacker_preferred_distance == defender_preferred_distance:
        distance_multiplier = 1
    elif (attacker_preferred_distance == "close" and defender_preferred_distance == "far") or (attacker_preferred_distance == "far" and defender_preferred_distance == "close"):
        distance_multiplier = 1.2
    else:
        distance_multiplier = 0.8
    return distance_multiplier

def battle(attacker, defender, terrain_advantage, technical_advantage, commander_multiplier):
    """Simulate a battle between the attacker and the defender."""
    # Calculate the distance multiplier based on the preferred distances of the attacker and the defender
    distance_multiplier = calculate_distance_multiplier(attacker, defender)
    
    # Calculate the class advantage based on the classes of the attacker and the defender
    class_advantage = 1
    if attacker["class"] in CLASS_ADVANTAGES:
        if defender["class"] in CLASS_ADVANTAGES[attacker["class"]]:
            class_advantage = CLASS_ADVANTAGES[attacker["class"]][defender["class"]]
    
    # Calculate the attack and defense values for the attacker and the defender
    attack_damage = calculate_attack(attacker, defender, terrain_advantage, technical_advantage, class_advantage, distance_multiplier, commander_multiplier)
    defense = calculate_defense(defender, attacker, terrain_advantage, technical_advantage, class_advantage, distance_multiplier, commander_multiplier)
    
    # Subtract the defense from the attack damage to determine the damage taken by the defender
    damage_taken = attack_damage - defense
    if damage_taken < 0:
        damage_taken = 0
    
    # Subtract the damage taken from the defender's health
    defender["health"] -= damage_taken
    
    # Check if the defender has been defeated
    if defender["health"] <= 0:
        return True
    else:
        return False

    

# Define the attributes of the armies
ARMY_1 = {
    "tier_1": {"count": 5, "attributes": SOLDIER_ATTRIBUTES["tier_1"]},
    "tier_2": {"count": 10, "attributes": SOLDIER_ATTRIBUTES["tier_2"]},
    "tier_3": {"count": 15, "attributes": SOLDIER_ATTRIBUTES["tier_3"]},
    "tier_4": {"count": 20, "attributes": SOLDIER_ATTRIBUTES["tier_4"]},
    "tier_5": {"count": 25, "attributes": SOLDIER_ATTRIBUTES["tier_5"]},
}

ARMY_2 = {
    "tier_1": {"count": 30, "attributes": SOLDIER_ATTRIBUTES["tier_1"]},
    "tier_2": {"count": 25, "attributes": SOLDIER_ATTRIBUTES["tier_2"]},
    "tier_3": {"count": 20, "attributes": SOLDIER_ATTRIBUTES["tier_3"]},
    "tier_4": {"count": 15, "attributes": SOLDIER_ATTRIBUTES["tier_4"]},
    "tier_5": {"count": 10, "attributes": SOLDIER_ATTRIBUTES["tier_5"]},
}

# Define the terrain and technical advantages
terrain_advantage = TERRAIN_ADVANTAGES["height_advantage"]
technical_advantage = 1.2

# Define the commander multiplier
commander_multiplier = 1.5

# Simulate the battle
while True:
    # Select a random soldier from each army to fight
    attacker = random.choice(list(ARMY_1.values()))["attributes"]
    defender = random.choice(list(ARMY_2.values()))["attributes"]
    
    # Simulate the battle
    result = battle(attacker, defender, terrain_advantage, technical_advantage)
    
    # If the defender was defeated, reduce their count by 1
    if result:
        ARMY_2[defender["tier"]]["count"] -= 1
    
    # If the attacker was defeated, reduce their count by 1
    if not result:
        ARMY_1[attacker["tier"]]["count"] -= 1
        
    # If either army has been defeated, end the battle
    if ARMY_1[defender["tier"]]["count"] <= 0 or ARMY_2[attacker["tier"]]["count"] <= 0:
        break

print(result)