#
# classes.py, contains classes w/variables to save values
#

class Player:
    # __init__, initialize variables for player
    def __init__(self, name, age, level, exp, max_health, health, power, defense, items, equipped_weapon, equipped_armor, equipped_shield, battling, running, room, hacker):
        self.name = name
        self.age = age
        self.level = level 
        self.exp = exp 
        self.max_health = max_health
        self.health = health
        self.power = power 
        self.defense = defense 
        self.items = items
        self.equipped_weapon = equipped_weapon
        self.equipped_armor = equipped_armor 
        self.equipped_shield = equipped_shield 
        self.battling = battling
        self.running = running 
        self.room = room
        self.hacker = hacker 

class Character:
    # __init__, initialize variables for character
    def __init__(self, name, age, level, max_health, health, power, defense, equipped_weapon, equipped_armor, equipped_shield):
        self.name = name
        self.age = age
        self.level = level
        self.max_health = max_health
        self.health = health
        self.power = power 
        self.defense = defense 
        self.equipped_weapon = equipped_weapon 
        self.equipped_armor = equipped_armor 
        self.equipped_shield = equipped_shield

class Item:
    # __init__, initialize variables for item
    def __init__(self, item_type, name, description, power):
        self.item_type = item_type # three different types, Weapon, Armor, Consumable
        self.name = name 
        self.description = description 
        self.power = power 

class Room:
    def __init__(self, room_num, room_type, room_item, room_monster, room_complete):
        self.room_num = room_num
        self.room_type = room_type
        self.room_item = room_item
        self.room_monster = room_monster 
        self.room_complete = room_complete 