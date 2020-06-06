
class Item:

    def __init__(self, name, damage, handedness, defense, equipped_location, health_gen, stamina_gen, magic_gen, description):
        self.name = name
        self.damage = damage
        self.handedness = handedness
        self.defense = defense
        self.equipped_location = equipped_location
        self.health_gen = health_gen
        self.stamina_gen = stamina_gen
        self.magic_gen = magic_gen
        self.description = description


    #attack, defense, hp_gen, mana_gen, description, space_taken, handedness, equpped_location
