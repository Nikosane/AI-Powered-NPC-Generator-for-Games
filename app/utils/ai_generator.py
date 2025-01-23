import random

def generate_npc_name():
    names = ["Aragorn", "Legolas", "Gandalf", "Frodo", "Eowyn"]
    return random.choice(names)

def generate_npc_role():
    roles = ["Warrior", "Mage", "Thief", "Healer", "Ranger"]
    return random.choice(roles)

def generate_npc_backstory():
    backstories = [
        "Once a humble farmer, now a fearless warrior.",
        "Trained in the arcane arts from a young age.",
        "A rogue with a mysterious past.",
        "A healer seeking redemption.",
        "A ranger who protects the wilds."
    ]
    return random.choice(backstories)
