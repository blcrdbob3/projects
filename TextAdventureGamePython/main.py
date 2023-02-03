#
# Dragon Realm - A Text-Based Adventure by Saisiddarth Thyarla
#

# libraries
import random
import time 
from classes import Player, Character, Item, Room

def main():
    # List of Items
        # Weapons: 0-6
            # Fists - 0
            # Sword - 1
            # Club - 2
            # Baseball Bat - 3
            # Katana - 4
            # Diamond Sword - 5
            # Excalibur - 6
        # Consumables: 7-10
            # Lesser Health Potion - 7
            # Health Potion - 8
            # Greater Health Potion - 9
            # Bomb - 10
        # Shields: 11-13
            # Wooden Shield - 11
            # Iron Shield - 12
            # Diamond Shield - 13
        # Armor: 14-16
            # Leather Armor - 14
            # Iron Armor - 15
            # Diamond Armor - 16
    items = [Item("Weapon", "Fists", "Your bare fists. Can't do much, but it's your only chance.", 5), Item("Weapon", "Sword", "A reliable, sharp blade. Can cut through enemies.", 15), Item("Weapon", "Club", "A large wooden stick to bludgeon your enemies.", 10), Item("Weapon", "Baseball Bat", "A light, but strong weapon to batter your enemies.", 18), Item("Weapon", "Katana", "An elegant blade that can slice through enemies like butter.", 20), Item("Weapon", "Diamond Sword", "A glistening blade to overpower anything that comes in your path", 25), Item("Weapon", "Excalibur", "The fabled sword of legends is in your hands!", 40), Item("Consumable", "Lesser Health Potion", "A small glass flask filled with a ominous, yet delicious red liquid.", 15), Item("Consumable", "Health Potion", "A glass flask filled with a vibrant, warm red liquid.", 25), Item("Consumable", "Greater Health Potion", "A large glass flask filled with a voracious, elegant red liquid.", 40), Item("Consumable", "Bomb", "A bomb that when lit, can lead to devastating results.", -25), Item("Armor", "Wooden Shield", "A flimsy, but trusty wooden shield to defend you against enemies.", 2.5), Item("Armor", "Iron Shield", "A fine, rigid iron shield to defend you against enemies.", 5), Item("Armor", "Diamond Shield", "A beautiful, indestructible diamond shield to defend you against enemies.", 10), Item("Armor", "Leather Armor", "An assortment of hide and leather to protect you from attacks.", 5), Item("Armor", "Iron Armor", "A heavy, but strong iron armor to protect you from attacks.", 10), Item("Armor", "Diamond Armor", "A exotic, defensive diamond armor to protect you from attacks.", 15)]
    # List of Rooms 
    # 0 - Entrance
    # 1 - Treasure
    # 2 - Battle
    # 3 - Challenge
    # 4 - Empty
    # 5 - Exit (BOSS)
    room_types = [Room(0, "Entrance", None, None, False), Room(1, "Treasure", None, None, False), Room(2, "Battle", None, None, False), Room(3, "Challenge", None, None, False), Room(4, "Empty", None, None, True), Room(5, "Exit", None, None, False)]
    rooms = [room_types[0]]
    # List of Characters
    # 0 - Goblin
    # 1 - Orc
    # 2 - Ronin
    # 3 - Deatheater
    # 4 - Dragon
    # 5 - Hacker
    characters = [Character("Goblin", 10, 1, 25, 25, 5, 0, items[0], None, None), Character("Orc", 18, 3, 40, 40, 10, 0, items[2], None, items[11]), Character("Ronin", 20, 5, 60, 60, 15, 5, items[3], items[14], items[11]), Character("Deatheater", 100, 8, 100, 100, 20, 10, items[4], items[14], items[12]), Character("Dragon", 9001, 10, 400, 400, 30, 0, items[0], None, None), Character("Hacker", 0, 1000, 999, 999, 40, 0, items[6], items[16], items[13])]    
    # help_menu, displays commands and what they do
    def help_menu(player):
        if player.battling == False:
            # returns a string which will be printed 
            return("## Help Menu ##\n'Left' - Your character travels to another room, going left.\n'Right' - Your character journeys to another room, going right.\n'Look Up' - Your character looks up, admiring the ceiling.\n'Look Down' - Your character looks down, a true visionary of the floor.\n'Look Left' - Your character looks left, seeing an entrance.\n'Look Right' - Your character looks right, seeing a door.\n'Status' - Display your character's status, showing your current stats & items.\n'Open Chest' - If there a chest in the room, use this command to open it.\n'Inventory' - Display all of your player's current items in an interactable system.\n'Help' - This is the most amount of help you will get.\n'Exit' - Exit the terminal and end the game.")
        else: 
            # help menu is different while you are in battle
            return("## Help Menu ##\n'Attack' - Your character readies their weapon, and attacks.\n'Defend' - Your character defends against an oncoming attack.\n'Item' - Display your inventory where you can use items. \n'Run' - Your character tries to dip and bolt out of the battle. Only works sometimes.\n'Spare' - Your character tries to spare the enemy. Works depending on the enemy's health.\n'Status' - Display your character's status, showing your current stats & items.\n'Check' - Display your opponent's status, showing your opponent's current stats & items.\n'Help' - No one is going to help you in this battle.\n'Exit' - Forfeit the battle and end the game, exiting the terminal.")

    # display_status, displays a character's stats
    def display_status(player, room_num, room_type, target):
        if target == player:
            print(f"Name: {target.name}")
            print(f"Age: {target.age}")
            print(f"Level: {target.level}")
            print(f"Max Health: {target.max_health}")
            print(f"Health: {target.health}")
            print(f"Power: {target.power}")
            print(f"Defense: {target.defense}")
            print("Items:")
            for index, item in enumerate(target.items):
                print(target.items[index].name) 
            print("Equipped Weapon: " + str(target.equipped_weapon.name))
            # null checks
            if target.equipped_armor != None:
                print("Equipped Armor: " + str(target.equipped_armor.name))
            if target.equipped_shield != None:
                print("Equipped Shield: " + str(target.equipped_shield.name))
            print("Room #: " + str(room_num))
            print("Room Type: " + str(room_type))
        else: 
            print(f"Name: {target.name}")
            print(f"Age: {target.age}")
            print(f"Level: {target.level}")
            print(f"Max Health: {target.max_health}")
            print(f"Health: {target.health}")
            print(f"Power: {target.power}")
            print(f"Defense: {target.defense}")
            print("Equipped Weapon: " + str(target.equipped_weapon.name))
            if target.equipped_armor != None:
                print("Equipped Armor: " + str(target.equipped_armor.name))
            if target.equipped_shield != None:
                print("Equipped Shield: " + str(target.equipped_shield.name))
    
    # view_inventory, displays an inventory system for the player to navigate
    def view_inventory(player):
        # prints the list of items out
        for index, item in enumerate(player.items):
            print(str(index) + ": " + player.items[index].name)
            print("Description: " + player.items[index].description)
        # prompts user yes/no question
        affirmative = input("\nWould you like to use/equip an item? (YES/NO)\n").lower()
        if affirmative == "yes":
            print("Very well.")
            time.sleep(0.5)
            # find item with number
            item_num = input("Type in the number of which item you would like to use/equip, or type in cancel to cancel the action.\n").lower()
            # check to make sure item_num is a whole number equal or above zero
            while True: # yes this is a while True: loop, but for some reason enter bypasses input, this is the only fix I found
                if item_num.isdigit(): 
                    if int(item_num) < 0:
                        print("Please type in a whole number that is not less than zero")
                        item_num = input("Type in the number of which item you would like to use/equip, or type in cancel to cancel the action.\n").lower()
                        continue 
                    else:
                        break 
                elif item_num == "cancel":
                    print("Very well, cancelling the action.")
                    item_num = -1
                    break 
                else:
                    print("Please type in a whole number that is not less than than zero")
                    item_num = input("Type in the number of which item you would like to use/equip, or type in cancel to cancel the action.\n").lower()
                    continue
            # going through list of items to find it
            for index, item in enumerate(player.items):
                if item_num == -1:
                    # to cancel the action, this has to break as well so I do it like this
                    break 
                elif index == int(item_num):
                    # found the item, let's equip/use it!
                    if player.battling == False:
                        if player.items[index].item_type == "Weapon":
                            print("You chose to equip the weapon: " + player.items[index].name)
                            affirmative = input("Are you sure you would like to use this weapon? (YES/NO)\n").lower()
                            if affirmative == "yes":
                                print("You equipped: " + player.items[index].name)
                                if player.equipped_weapon != items[0]:
                                    # if equipped weapon (before equipping new one) is not fists, add it to player's inventory
                                    player.items.append(player.equipped_weapon)
                                # equip weapon 
                                player.equipped_weapon = player.items[index]
                                # remove item from inventory
                                if player.equipped_weapon != items[0]:
                                    # if current equipped weapon is not fists, remove the old one from the player's inventory
                                    player.items.pop(index)
                            elif affirmative == "no":
                                print("Very well. Cancelling action.")
                            else:
                                print("Invalid command.")
                                affirmative = input("Are you sure you would like to use this weapon? (YES/NO)\n").lower
                        elif player.items[index].item_type == "Armor":
                            print("You chose to equip the armor: " + player.items[index].name)
                            affirmative = input("Are you sure you would like to use this armor? (YES/NO)\n").lower()
                            if affirmative == "yes":
                                print("You equipped: " + player.items[index].name)
                                # check if item is a shield or item
                                if player.items[index] == items[11] or player.items[index] == items[12] or player.items[index] == items[13]:          
                                    if player.equipped_shield != None:
                                        # add equipped shield to inventory
                                        player.items.append(player.equipped_shield)
                                    # equip shield
                                    player.equipped_shield = player.items[index]
                                else:
                                    if player.equipped_armor != None:
                                        # add equipped shield to inventory
                                        player.items.append(player.equipped_armor)
                                    # equip armor
                                    player.equipped_armor = player.items[index]
                                # remove item from inventory
                                player.items.pop(index)
                            elif affirmative == "no":
                                print("Very well. Cancelling action.")
                            else:
                                print("Invalid command.")
                                affirmative = input("Are you sure you would like to use this armor? (YES/NO)\n").lower()
                        elif player.items[index].item_type == "Consumable":
                            print("You chose to use the consumable: " + player.items[index].name)
                            affirmative = input("Are you sure you would like to use this consumable? (YES/NO)\n").lower()
                            if affirmative == "yes":
                                print("You used: " + player.items[index].name)
                                # use item
                                if player.items[index] == items[10]:
                                    # well there's no enemy so I guses this is what you use the bomb for
                                    print("You blew yourself up using the bomb.")
                                    change_health(player, player.items[index].power, player)
                                else:
                                    print("You drank the potion.")
                                    change_health(player, player.items[index].power, player)
                                # remove item from inventory
                                player.items.pop(index)
                            elif affirmative == "no":
                                print("Very well. Pick another consumable.")
                                view_inventory(player)
                            else:
                                print("Invalid command.")
                                affirmative = input("Are you sure you would like to use this consumable? (YES/NO)\n").lower()        
                    else:
                        if player.items[index].item_type == "Consumable":
                            print("You chose to use the consumable: " + player.items[index].name)
                            affirmative = input("Are you sure you would like to use this consumable? (YES/NO)\n").lower()
                            if affirmative == "yes":
                                print("You used: " + player.items[index].name)
                                # use item 
                                return player.items[index]
                                # remove item from inventory
                                player.items.pop(index)
                            elif affirmative == "no":
                                print("Very well. Pick another consumable.")
                                view_inventory(player)
                            else:
                                print("Invalid command.")
                                affirmative = input("Are you sure you would like to use this consumable? (YES/NO)\n").lower()
        elif affirmative == "no":
            print("Very well. Cancelling action.")
        else:
            print("Invalid command. Try again.")
            view_inventory(player)

    # dot_dot_dot, a little pause
    def dot_dot_dot():
        print(".")
        time.sleep(0.33)
        print("..")
        time.sleep(0.33)
        print("...")
        time.sleep(1)
    
    # dice_roll, rolls a dice of chance to determine what will happen
    def dice_roll(lower, upper, threshold):
        # lower is lower limit
        # upper is upper limit
        # threshold is number that the dice must roll higher to qualify

        # ex:
        # dice_roll(1, 5, 4)
        # dice must roll higher than three to qualify for threshold
        # if dice rolls 3 or lower, then dice did not qualify, returning False
        # if dice rolls 4 or higher, then dice qualified, returning True
        # 2/5 chance to qualify, which equals 40% chance to succeed
        dice = random.randint(lower, upper)
        if dice >= threshold:
            return True
        else:
            return False 

    # change_health, heals/damages a target's health depending on values given
    def change_health(player, health, target):
        # give message depending on health
        if health > 0: 
            # change target health
            new_health = target.health + health 
            if new_health > target.max_health:
                target.health = target.max_health
            else:
                target.health = new_health 
            if target == player:
                print("You were healed for " + str(health) + " HP!")
                print("You now have " + str(target.health) + " HP!")
            else:
                print(str(target) + " has been healed for " + str(health) + " HP!")
                print("Your target now has " + str(target.health) + " HP!")
        elif health < 0:
            # change target health depending on defense 
            damage = health + target.defense 
            if damage > 0:
                damage = 0
            target.health += damage
            if target == player:
                if target.defense:
                    # different messages if target has defense or not
                    print("You were attacked for " + str(health) + " HP!")
                    print("You defended the attack for " + str(target.defense) + " HP!")
                    print("You were damaged for " + str(damage) + "HP!")
                else:
                    print("You were damaged for " + str(damage) + "HP!")
                print("You now have " + str(target.health) + " HP!")
            else:
                if target.defense:
                    print(str(target.name) + " has been attacked for " + str(health) + " HP!")
                    print(str(target.name) + " has blocked the attack for " + str(target.defense) + " HP!")
                    print(str(target.name) + " has been damaged for " + str(damage) + " HP!")
                else: 
                    print(str(target.name) + " has been damaged for " + str(damage) + " HP!")
                print("Your target now has " + str(target.health) + " HP!")
    
    # level_up, levels up player by one and removes EXP
    def level_up(player):
        required_exp = 10 * player.level # 10 * player.level, ex: 10 * 3 is EXP you need to level up if you're level 3
        if player.exp >= required_exp:
            print("Level up! Your character has grown stronger!")
            player.level += 1
            player.exp - required_exp
            player.max_health = 100 + 5 * player.level # increases max_health by 100 + 5 * player.level, at level 3 you would have 115 max HP
            player.health = player.max_health # heals you to full
        
    # give_item, gives a target an item
    def give_item(player, item, target):
        target.items.append(item)
        if target == player:
            print("You acquired: " + item.name)
        else: 
            print(target.name + " acquired: " + item.name)

    # battle, continues the battle
    def battle(player, monster,  action):
        if action == "attack":
            # Attacks the monster!
            change_health(player, -player.power, monster)
            # The monster attacks now.
            print("Your opponent attacked you!")
            change_health(player, -monster.power, player)
        elif action == "defend":
            # Doubles your defense for a turn!
            player.defense *= 2
            # The monster attacks now.
            print("Your opponent hit you!")
            change_health(player, -monster.power, player)
            # Reduces your defense to default.
            player.defense /= 2
        elif action == "item":
            # Open inventory to choose from.
            consumable = view_inventory(player)
            if consumable:
                if consumable == items[10]:
                    print("You threw a bomb at the monster.")
                    change_health(player, consumable.power, monster)
                else:
                    print("You drank a potion.")
                    change_health(player, consumable.power, player)
            # The monster attacks now.
            print("Your opponent striked you!")
            change_health(player, -monster.power, player)
                    

    # end_battle, ends a battle when conditions have been met
    def end_battle(player, monster, room_num, action):
        if player.battling == True:
            # There are three different ways that a battle may end (other than player dying):
            # 1 - Opponent's health reaches zero 
            if monster.health <= 0:
                if monster != characters[4]:
                    # The monster is dead, end the battle!
                    print("The " + monster.name + " has been slain!")
                    print("You have earned " + str(monster.max_health) + " EXP!")
                    for room in rooms:
                        if room.room_num == room_num: 
                            room.room_complete = True 
                    player.battling = False 
                    time.sleep(0.5)
                    player.exp += monster.max_health 
                else:
                    # The dragon has been slain! The game has been won.
                    print("The " + monster.name + " has been slain!")
                    time.sleep(5)
                    print("Congratulations! You have slain the final boss and found the exit!")
                    time.sleep(1)
                    print("Unfortunately, this is where the game ends, but I have a secret to tell you.")
                    time.sleep(1)
                    print("If you type in the command 'hacker', it will ask you to use a password.")
                    time.sleep(1)
                    print("You'll have to figure out the rest yourself.")
                    time.sleep(1)
                    print("The password is 'alrayhthtraddisias'")
                    time.sleep(1)
                    print("Thank you for playing my game.")
                    time.sleep(1)
                    print("I bid you farewell.")
                    for room in rooms:
                        if room.room_num == room_num: 
                            room.room_complete = True 
                    player.battling = False 
            # 2 - Player runs away (this can fail)
            if action == "run":
                # room type 
                # check to see if player hasn't ran yet 
                if player.running == False:
                    print("You try to run from the monster...")
                    # run_roll, 50/50 chance
                    run_roll = dice_roll(1,2,2)
                    dot_dot_dot()
                    if run_roll == True:
                        print("You successfully ran away from the battle! ") 
                        # dice roll
                        dice = random.randint(1,2)
                        if (dice == 1):
                            go_to_room(player, room_num + 1)
                        else: 
                            go_to_room(player, room_num - 1)
                        player.battling = False
                    else:
                        print("You failed to run away from the battle...")
                        time.sleep(0.5)
                        print("You cannot run anymore.")
                        player.running = True
                elif monster.name == "Dragon":
                    print("You cannot escape a dragon.")
                    print("You were clawed for trying to run away!")
                    change_health(player, -monster.power, player)
                else:
                    print("You can no longer run anymore.")
                    print("Your opponent caught you for trying to run away!")
                    change_health(player, -monster.power, player)
            # 3 - Player successfully spares the monster (starts at 1% chance and is multiplied by monster's health missing)
            elif action == "spare":
                print("You try to spare the monster...")
                # spare_roll
                missing_health = monster.health / monster.max_health # this will give a decimal
                spare_chance = int(100 - ((1 - missing_health) * 100)) # subtract the decimal from 1, then multiply it by 100, then subtract that from 100 and round it
                spare_roll = dice_roll(0, 100, spare_chance)
                dot_dot_dot()
                if spare_roll == True:
                    if monster != characters[4]:
                        print("You successfully spared the " + monster.name + "!")
                        for room in rooms:
                            if room.room_num == room_num: 
                                room.room_complete = True
                        player.battling = False 
                        time.sleep(0.5)
                        print("You have earned " + str(monster.max_health) + " EXP!")
                        player.exp += monster.max_health 
                    else:
                        # The dragon has been slain! The game has been won.
                        print("You successfully spared the " + monster.name + "!")
                        time.sleep(5)
                        print("Congratulations! You have spared the final boss and found the exit!")
                        time.sleep(1)
                        print("Unfortunately, this is where the game ends, but I have a secret to tell you.")
                        time.sleep(1)
                        print("If you type in the command 'hacker', it will ask you to use a password.")
                        time.sleep(1)
                        print("You'll have to figure out the rest yourself.")
                        time.sleep(1)
                        print("The password is 'alrayhthtraddisias'")
                        time.sleep(1)
                        print("Thank you for playing my game.")
                        time.sleep(1)
                        print("I bid you farewell.")
                        for room in rooms:
                            if room.room_num == room_num: 
                                room.room_complete = True 
                        player.battling = False 
                else:
                    print("You failed to spare the monster...")
                    time.sleep(0.5)
                    print("Your opponent smacked you for your benevolence!")
                    change_health(player, -monster.power, player)

    # generate, can generate a room, a character, or an item
    def generate(player, generate_type, room_num):
        if generate_type == "Room":
            if room_num == -1 or room_num == 1:
                # first room for left & right will always be a treasure room
                item = generate(player, "Item", room_num)
                rooms.append(Room(room_num, "Treasure", item, None, True))
            else:
                # if player is level 20, next room will always be exit
                if player.level >= 20 and not player.level >= 1000:
                    rooms.append(Room(room_num, "Exit", None, None, False))
                    monster = generate(player, "Monster", room_num)
                    for room in rooms: 
                        if room.room_num == room_num: 
                            room.room_monster = monster 
                else:
                    # treasure room dice roll (33% chance)
                    treasure_roll = dice_roll(1, 3, 3)
                    if treasure_roll == True:
                        item = generate(player, "Item", room_num)
                        rooms.append(Room(room_num, "Treasure", item, None, True))
                    else: 
                        # challenge room dice roll (25% chance)
                        challenge_roll = dice_roll(1,4,4)
                        if challenge_roll == True:
                            item = generate(player, "Item", room_num)
                            rooms.append(Room(room_num, "Challenge", item, None, False))
                            monster = generate(player, "Monster", room_num)
                            for room in rooms: 
                                if room.room_num == room_num: 
                                    room.room_monster = monster 
                        else: 
                            # empty room dice roll (5% chance)
                            empty_roll = dice_roll(1,20,20)
                            if empty_roll == True:
                                rooms.append(Room(room_num, "Empty", None, None, True))
                            else:
                                rooms.append(Room(room_num, "Battle", None, None, False))
                                monster = generate(player, "Monster", room_num)
                                for room in rooms: 
                                    if room.room_num == room_num: 
                                        room.room_monster = monster 
        elif generate_type == "Monster":
            for room in rooms:
                if room.room_num == room_num:
                    if room.room_type == "Battle":
                        if player.level < 3: 
                            # Goblin
                            return characters[0]
                        elif player.level >= 3 and player.level < 7:
                            # orc_roll, 80% chance of getting an orc
                            orc_roll = dice_roll(1, 5, 1)
                            # Orc
                            if orc_roll == True:
                                return characters[1]
                            else: 
                                return characters[0]
                        elif player.level >= 7 and player.level < 16:
                            # ronin_roll, 80% chance of getting a ronin
                            ronin_roll = dice_roll(1, 5, 1)
                            # Ronin
                            if ronin_roll == True:
                                return characters[2]
                            else: 
                                return characters[1]
                        elif player.level >= 16:
                            # deatheater_roll, 80% chance of getting a deatheater
                            deatheater_roll = dice_roll(1, 5, 1)
                            # Deatheater
                            if deatheater_roll == True:
                                return characters[3]
                            else: 
                                return characters[2]
                        elif player.level >= 1000:
                            # Hacker
                            return characters[5]
                    elif room.room_type == "Challenge":
                        # In a challenge room, a monster has 1.5x their HP & Power.
                        if player.level < 3: 
                            # Goblin (but buffed)
                            buffed_goblin = characters[0]
                            buffed_goblin.health *= 1.5
                            buffed_goblin.power *= 1.5
                            return buffed_goblin
                        elif player.level >= 3 and player.level < 7:
                            # orc_roll, 80% chance of getting an orc
                            orc_roll = dice_roll(1, 5, 1)
                            # buffed characters
                            buffed_goblin = characters[0]
                            buffed_goblin.health *= 1.5
                            buffed_goblin.power *= 1.5
                            buffed_orc = characters[1]
                            buffed_orc.health *= 1.5
                            buffed_orc.power *= 1.5
                            # Orc
                            if orc_roll == True:
                                return buffed_orc
                            else: 
                                return buffed_goblin
                        elif player.level >= 7 and player.level < 16:
                            # ronin_roll, 80% chance of getting a ronin
                            ronin_roll = dice_roll(1, 5, 1)
                            # buffed characters
                            buffed_orc = characters[1]
                            buffed_orc.health *= 1.5
                            buffed_orc.power *= 1.5
                            buffed_ronin = characters[2]
                            buffed_ronin.health *= 1.5
                            buffed_ronin.power *= 1.5
                            # Ronin
                            if ronin_roll == True:
                                return buffed_ronin
                            else: 
                                return buffed_orc
                        elif player.level >= 16:
                            # deatheater_roll, 80% chance of getting a deatheater
                            deatheater_roll = dice_roll(1, 5, 1)
                            # buffed characters
                            buffed_ronin = characters[2]
                            buffed_ronin.health *= 1.5
                            buffed_ronin.power *= 1.5
                            buffed_deatheater = characters[3]
                            buffed_deatheater.health *= 1.5
                            buffed_deatheater.power *= 1.5
                            # Deatheater
                            if deatheater_roll == True:
                                return buffed_deatheater
                            else: 
                                return buffed_ronin
                        elif player.level >= 1000:
                            # Hacker
                            buffed_hacker = characters[5]
                            buffed_hacker.health *= 1.5
                            buffed_hacker.power *= 1.5
                            return player, characters[5]
                    elif room.room_type == "Exit":
                        print("The ground shakes...")
                        time.sleep(1)
                        print("You hear loud stomping in the distance...")
                        time.sleep(3)
                        print("A dragon stands before you.")
                        time.sleep(1)
                        dot_dot_dot()
                        print("Good luck.")
                        time.sleep(1)
                        return characters[4]
        elif generate_type == "Item":
            if player.level < 5:
                item_roll = random.randint(1,5)
                if item_roll == 1:
                    # club
                    return items[2]
                elif item_roll == 2:
                    # baseball bat
                    return items[3]
                elif item_roll == 3:
                    # leather armor
                    return items[14] 
                elif item_roll == 4:
                    # wooden shield
                    return items[11]
                elif item_roll == 5:
                    # lesser health potion
                    return items[7]
            elif player.level >= 5 and player.level < 14:
                item_roll = random.randint(1,5)
                if item_roll == 1:
                    # katana
                    return items[4]
                elif item_roll == 2:
                    # iron armor
                    return items[15]
                elif item_roll == 3:
                    # iron shield
                    return items[12]
                elif item_roll == 4:
                    # health potion
                    return items[8]
                elif item_roll == 5:
                    # bomb
                    return items[10]
            elif player.level >= 14 and player.level < 17:
                item_roll = random.randint(1,5)
                if item_roll == 1:
                    # katana (if user runs into bad luck and somehow gets no weapon, they can still get a solid weapon)
                    return items[3]
                elif item_roll == 2:
                    # diamond armor
                    return items[16]
                elif item_roll == 3:
                    # diamond shield 
                    return items[13]
                elif item_roll == 4:
                    # greater health potion
                    return items[9]
                elif item_roll == 5:
                    # bomb 
                    return items[10]
            elif player.level >= 17: 
                item_roll = random.randint(1,5)
                if item_roll == 1:
                    # excalibur
                    return items[6]
                elif item_roll == 2:
                    # diamond armor
                    return items[16]
                elif item_roll == 3:
                    # diamond shield 
                    return items[13]
                elif item_roll == 4:
                    # greater health potion
                    return items[9]
                elif item_roll == 4:
                    # bomb 
                    return items[10]
    
    # go_to_room, changes player's room
    def go_to_room(player, room_num):
        # if there is a room already there, real_room turns false
        real_room = True 
        for room in rooms: 
            if room.room_num == room_num: 
                real_room = False
        if real_room == True: 
            generate(player, "Room", room_num)

    # game_intro, prompts the user for input to complete their character
    def game_intro():
        # asks for player's name 
        name = input("Enter your character's name: ")
        # asks for player's age
        age = input("Enter your character's age: ")
        # makes sure that age is a whole number
        while True: # while yes, this is while True, while True only works as pressing enter bypasses while age:
            if age.isdigit(): 
                if int(age) <= 0:
                    print("Please type in a whole number more than 0")
                    age = input("Enter your character's age: ")
                    continue 
                else:
                    break 
            else:
                print("Please type in a whole number more than 0")
                age = input("Enter your character's age: ")
                continue
        # default variables for player character
        level = 1 # player's level, increases max HP by 5 * level every level up
        exp = 0 # player's exp, one exp = one HP, when exp is over 10, player levels up and exp threshold is equal to 10 * level + fully heals player to full
        max_health = 100 # player's max HP, player's health cannot go over this
        health = 100 # player's HP, if this reaches zero, player will die
        power = 5 # player's power, how much damage a player deals per attack, equal to current item's power
        defense = 0 # player's defense, reduces the amount of damage a player takes per attack
        player_items = [items[0]] # player's items, currently empty, but will contain the items a player has
        equipped_weapon = items[0] # fists
        equipped_armor = None # for now until player equips armor
        equipped_shield = None # for now until player equips a shield
        battling = False # player's battling boolean, is true when a player is battling
        running = False # player's running boolean, if this is true, a player cannot run no more
        room = rooms[0] # player's current room 
        hacker = False # player's hacker status
        # create player object
        player = Player(name, age, level, exp, max_health, health, power, defense, player_items, equipped_weapon, equipped_armor, equipped_shield, battling, running, room, hacker)
        # small pause for player 
        print("...")
        # time.sleep is a function that pauses the current program for x seconds
        time.sleep(0.5)
        print("Let's begin.")
        time.sleep(0.5)
        # begin game 
        start_game(player)
    
    # battle_prompts, helps with late variables that start off as None
    def battle_prompts(room_monster): 
        # list of battle prompts
        if room_monster and room_monster.name:
            battle_prompts = ["As you walk through the door, a " + room_monster.name + " lunges at you!", "You have found a " + room_monster.name + " and are now in a battle!", "You have found a " + room_monster.name + "... and that " + room_monster.name + " has found you.", "You have found yourself in an intense battle with a "+ room_monster.name + "!", "You are fighting a " + room_monster.name + "!"]
        return battle_prompts

    # start_game, starts the game
    def start_game(player):
        # begin introduction for player
        print('''
                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"
''')
        # small pause 
        time.sleep(1)
        # room stuff 
        room_num = 0
        room_type = None 
        room_monster = None
        room_item = None
        # list of greetings
        greetings = ["Greetings, " + player.name + "!" + " On a cave expedition, you slipped and fell down a ravine.","Upon awakening, you find that you are trapped in a mysterious dungeon.","Armed with nothing, you must gather items & weapons and find the exit to escape.","Be vigilant, you must be prepared to fight any monsters you will face.", "Good luck, brave adventurer!"]
        # list of prompts
        prompts = ["You look up and see a dark, creepy ceiling.", "You look up and see a murky, mossy ceiling.", "You look up and see a dim, dull ceiling.", "You look down and see a dirty, cobweb-covered floor.", "You look down and see a opaque, crummy floor.", "You look down and see a unkempt, messy floor.", "You look left and see a dungy, wooden door.", "You look left and see a muddy, sloppy door.", "You look left and see a dusty, smudged door.", "You look right and see a broken, destroyed door.", "You look right and see a sullied, spotted door.", "You look right and see a squalid, straggly door."]
        # prints greetings out for a random amount of time 
        for index, item in enumerate(greetings): 
            print(greetings[index])
            # random.random, function that returns a random float between 0 and 1
            if index == 5: 
                time.sleep(1)
            else:
                time.sleep(random.random())
        # small pause
        time.sleep(1)
        # finish introduction
        print("\nThe room is dimly lit by torches and covered with cobwebs.")
        # another small pause
        time.sleep(0.5)
        print("You stand in the middle of a empty, barren room.")
        # another another small pause
        time.sleep(0.5)
        print("To travel between rooms, use the commands left & right.")
        # another another another small pause
        time.sleep(1)
        # prompt user for actions
        while player:
            # update room variables
            for room in rooms:
                if room.room_num == room_num:
                    room_type = room.room_type
                    room_monster = room.room_monster 
                    room_item = room.room_item 
                    room_complete = room.room_complete
            # win condition check
            if room_type == "Exit" and room_complete == True:
                print("GAME OVER")
                time.sleep(0.5)
                break 
            # player stats check
            if player.hacker == False:
                player.power = player.equipped_weapon.power
                player.defense = 0
                if player.equipped_armor != None: 
                    player.defense += player.equipped_armor.power 
                if player.equipped_shield != None: 
                    player.defense += player.equipped_shield.power
                if player.health > player.max_health:
                    player.health = player.max_health 
            # player lvl up check
            required_exp = 10 * player.level
            if player.exp >= required_exp: 
                level_up(player)
            # player health check
            elif player.health <= 0:
                # death sequence
                print("...")
                time.sleep(0.5)
                print("Your grip grows loose as your life slowly fades away...")
                dot_dot_dot()
                print("GAME OVER")
                time.sleep(1)
                if player.hacker == True: 
                    print("GAME OVER..?")
                    time.sleep(1)
                    print("This is not the end.")
                    time.sleep(1)
                    resurrect = input("Would you like to resurrect?\n").lower()
                    if resurrect == "yes": 
                        print("Very well.")
                        time.sleep(1)
                        player.health = player.max_health
                    elif resurrect == "no":
                        print("Very well.")
                        time.sleep(0.5)
                        print("Goodbye.")
                        time.sleep(1)
                        break
                    else:
                        print("Invalid command. Try again.")
                        resurrect = input("Would you like to resurrect?").lower()
                else:
                    break 
            # prompt user for input
            elif player.battling == False:
                # check for battle 
                if room_type == "Battle" or "Challenge" or "Exit":
                    if room_complete == False and room_monster != None:
                        dice = random.randint(0,4)
                        battleprompts = battle_prompts(room_monster)
                        print(battleprompts[dice])
                        time.sleep(1)
                        player.battling = True 
                        continue
                # check for chest 
                if room_item != None and room_complete == True: 
                    print("In the middle of the room lies a mysterious chest.")
                # prompt user for actions 
                action = input("\nEnter your action: left, right, look up, look down, look left, look right, open chest, status, inventory, help, exit:\n").lower()
                if action == "left":
                    room_num -= 1
                    go_to_room(player, room_num)
                elif action == "right":
                    room_num += 1
                    go_to_room(player, room_num)
                elif action == "look up":
                    dice = random.randint(0,2)
                    print(prompts[dice])
                elif action == "look down":
                    dice = random.randint(3,5)
                    print(prompts[dice])
                elif action == "look left":
                    dice = random.randint(6,8)
                    print(prompts[dice])
                elif action == "look right":
                    dice = random.randint(9,11)
                    print(prompts[dice])
                elif action == "open chest":
                    if room_item != None and room_complete == True:
                        print("You opened the chest and found a " + room_item.name)
                        give_item(player, room_item, player)
                        # set room item to none so that chest cannot be opened again
                        for dungeon_room in rooms:
                            if dungeon_room.room_num == room_num:
                                dungeon_room.room_item = None
                    else:
                        print("There seems to be no chest here.")
                elif action == "status":
                    display_status(player, room_num, room_type, player)
                elif action == "inventory":
                    view_inventory(player)
                elif action == "help":
                    text = help_menu(player)
                    print(text)
                elif action == "die":
                    print("You fall over and smack your head on the stone floor.") 
                    time.sleep(0.5)
                    change_health(player, -999, player)
                elif action == "hacker":
                    if player.hacker == False:
                        print("Something is wrong...")
                        time.sleep(1)
                        print("A voice whispers to you...")
                        time.sleep(0.5)
                        secret = input("'What is the password?'\n")
                        if secret == "alrayhthtraddisias":
                            print("A large roar can be heard through the dungeon.")
                            time.sleep(1)
                            print("You feel powerful. Something has changed.")
                            time.sleep(1)
                            player.hacker = True 
                        else:
                            print("A large roar can be heard through the dungeon.")
                            time.sleep(1)
                            print("Your body begins to disintegrate.")
                            time.sleep(1)
                            for x in range(0,999): 
                                change_health(player, -x, player)
                                time.sleep(0.001)
                            if player.health > 0: 
                                print("What? How are you still alive?")
                                dot_dot_dot()
                                print("Fine.")
                                time.sleep(0.5)
                                print("Congratulations.")
                                time.sleep(0.5)
                                print("I guess you won.")
                                time.sleep(1)
                                break
                    else:
                        print("Welcome, " + player.name)
                        time.sleep(1)
                        while player:
                            hacking = input("\nHacker Menu: antivirus, change, teleport, item, custom, kill, close:\n").lower()
                            if hacking == "antivirus":
                                print("AntiVirus Detected A Hacker!")
                                time.sleep(1)
                                player.hacker = False 
                                player.health = -1337
                                player.maxhealth = -1337
                                print("Terminated")
                                break 
                            elif hacking == "change":
                                print("Which Stat Do You Want To Change")
                                print("Name: " + str(player.name))
                                print("Age: " + str(player.age))
                                print("Level: " + str(player.level))
                                print("EXP: " + str(player.exp))
                                print("Max Health: " + str(player.max_health))
                                print("Health: " + str(player.health))
                                print("Power: " + str(player.power))
                                print("Defense: " + str(player.defense))
                                print("Hacker: " + str(player.hacker))
                                hacker_stat = input("").lower()
                                if hacker_stat == "name":
                                    answer = input("What Is Your New Name\n").lower()
                                    player.name = str(answer) 
                                    print("Done")
                                if hacker_stat == "age":
                                    answer = input("What Is Your New Age\n").lower()
                                    if answer.isdigit():
                                        player.age = int(answer) 
                                        print("Done")
                                    else: 
                                        print("You Dont Know How To Type Numbers?")
                                        player.health = -1337
                                        break
                                if hacker_stat == "level":
                                    answer = input("What Is Your New Level\n").lower()
                                    if answer.isdigit():
                                        player.level = int(answer) 
                                        print("Done")
                                    else: 
                                        print("You Dont Know How To Type Numbers?")
                                        player.health = -1337
                                        break
                                if hacker_stat == "exp":
                                    answer = input("What Is Your New EXP\n").lower()
                                    if answer.isdigit():
                                        player.exp = int(answer) 
                                        print("Done")
                                    else: 
                                        print("You Dont Know How To Type Numbers?\n")
                                        player.health = -1337
                                        break
                                if hacker_stat == "max health":
                                    answer = input("What Is Your New Max Health\n").lower()
                                    if answer.isdigit():
                                        player.max_health = int(answer) 
                                        print("Done")
                                    else: 
                                        print("You Dont Know How To Type Numbers?")
                                        player.health = -1337
                                        break
                                if hacker_stat == "health":
                                    answer = input("What Is Your New Health\n").lower()
                                    if answer.isdigit():
                                        player.health = int(answer) 
                                        print("Done")
                                    else: 
                                        print("You Dont Know How To Type Numbers?")
                                        player.health = -1337
                                        break
                                if hacker_stat == "power":
                                    answer = input("What Is Your New Power\n").lower()
                                    if answer.isdigit():
                                        player.power = int(answer) 
                                        print("Done")
                                    else: 
                                        print("You Dont Know How To Type Numbers?")
                                        player.health = -1337
                                        break
                                if hacker_stat == "defense":
                                    answer = input("What Is Your New Defense\n").lower()
                                    if answer.isdigit():
                                        player.defense = int(answer) 
                                        print("Done")
                                    else: 
                                        print("You Dont Know How To Type Numbers?")
                                        player.health = -1337
                                        break
                                if hacker_stat == "hacker":
                                    print("You No Longer Hacker")
                                    player.hacker = False 
                                    break 
                            elif hacking == "teleport":
                                answer = input("Where Do You Want To Go, Type Room Number\n").lower()
                                if answer.isdigit():
                                    go_to_room(player, int(answer))
                                    print("Done")
                                else: 
                                    print("You Dont Know How To Type Numbers?")
                                    player.health = -1337
                                    break
                            elif hacking == "item":
                                answer = input("What Do You Want\n").lower()
                                for item in items: 
                                    if item.name.lower() == answer: 
                                        give_item(player, item, player)
                                        print("Done")
                            elif hacking == "custom":
                                answer = input("What Type Of Item: Armor, Weapon, Consumable\n")
                                answer2 = input("What Is The Name\n")
                                answer3 = input("What Is The Description\n")
                                answer4 = input("What Is The Power\n")
                                items.append(Item(answer, answer2, answer3, answer4))
                            elif hacking == "kill":
                                if player.battling == True:
                                    room_monster.health = -1337
                                else: 
                                    player.health = -1337
                                print("Terminated") 
                            elif hacking == "close":
                                print("Goodbye")
                                break
                elif action == "exit":
                    print("Goodbye, adventurer.")
                    time.sleep(1)
                    break
                else:
                    print("Invalid action. Type 'help' for a list of possible actions.")
            # prompt user for input: battle mode
            elif player.battling == True:  
                if room_monster.health <= 0:
                    # The monster has been slain! End the battle.
                    end_battle(player, room_monster, room_num, None)
                    continue 
                action = input("\nYou are currently in battle! Enter your action: attack, defend, item, run, spare, status, check, help, exit:\n").lower()
                if action == "attack":
                    print("You readied your weapon and attacked!")
                    time.sleep(0.5)
                    battle(player, room_monster, action) 
                elif action == "defend":
                    if player.defense == 0:
                        print("You tried to defend with your feeble arms, but it didn't work!")
                    else:
                        print("You defended against the oncoming attack!")
                    battle(player, room_monster, action) 
                elif action == "item":
                    battle(player, room_monster, action)
                elif action == "run":
                    end_battle(player, room_monster, room_num, action)
                elif action == "spare":
                    end_battle(player, room_monster, room_num, action)
                elif action == "status":
                    display_status(player, room_num, room_type, player)
                elif action == "check":
                    display_status(player, room_num, room_type, room_monster)
                elif action == "help":
                    text = help_menu(player)
                    print(text)
                elif action == "die":
                    print("You stare at your enemy and then proceed to kick the bucket.") 
                    time.sleep(0.5)
                    change_health(player, -999, player)
                elif action == "hacker":
                    if player.hacker == False:
                        print("Something is wrong...")
                        time.sleep(1)
                        print("A voice whispers to you...")
                        time.sleep(0.5)
                        secret = input("'What is the password?'\n")
                        if secret == "alrayhthtraddisias":
                            print("A large roar can be heard through the dungeon.")
                            time.sleep(1)
                            print("You feel powerful. Something has changed.")
                            time.sleep(1)
                            player.hacker = True 
                        else:
                            print("A large roar can be heard through the dungeon.")
                            time.sleep(1)
                            print("Your body begins to disintegrate.")
                            time.sleep(1)
                            for x in range(0,999): 
                                change_health(player, -x, player)
                                time.sleep(0.001)
                            if player.health > 0: 
                                print("What? How are you still alive?")
                                dot_dot_dot()
                                print("Fine.")
                                time.sleep(0.5)
                                print("Congratulations.")
                                time.sleep(0.5)
                                print("I guess you won.")
                                time.sleep(1)
                                break
                    else:
                        print("Welcome, " + player.name)
                        time.sleep(1)
                        while player:
                            hacking = input("\nHacker Menu: antivirus, change, teleport, item, custom, kill, close:\n").lower()
                            if hacking == "antivirus":
                                print("AntiVirus Detected A Hacker!")
                                time.sleep(1)
                                player.hacker = False 
                                player.health = -1337
                                player.maxhealth = -1337
                                print("Terminated")
                                break 
                            elif hacking == "change":
                                print("Which Stat Do You Want To Change")
                                print("Name: " + str(player.name))
                                print("Age: " + str(player.age))
                                print("Level: " + str(player.level))
                                print("EXP: " + str(player.exp))
                                print("Max Health: " + str(player.max_health))
                                print("Health: " + str(player.health))
                                print("Power: " + str(player.power))
                                print("Defense: " + str(player.defense))
                                print("Hacker: " + str(player.hacker))
                                hacker_stat = input("").lower()
                                if hacker_stat == "name":
                                    answer = input("What Is Your New Name\n").lower()
                                    player.name = str(answer) 
                                    print("Done")
                                if hacker_stat == "age":
                                    answer = input("What Is Your New Age\n").lower()
                                    if answer.isdigit():
                                        player.age = int(answer) 
                                        print("Done")
                                    else: 
                                        print("You Dont Know How To Type Numbers?")
                                        player.health = -1337
                                        break
                                if hacker_stat == "level":
                                    answer = input("What Is Your New Level\n").lower()
                                    if answer.isdigit():
                                        player.level = int(answer) 
                                        print("Done")
                                    else: 
                                        print("You Dont Know How To Type Numbers?")
                                        player.health = -1337
                                        break
                                if hacker_stat == "exp":
                                    answer = input("What Is Your New EXP\n").lower()
                                    if answer.isdigit():
                                        player.exp = int(answer) 
                                        print("Done")
                                    else: 
                                        print("You Dont Know How To Type Numbers?\n")
                                        player.health = -1337
                                        break
                                if hacker_stat == "max health":
                                    answer = input("What Is Your New Max Health\n").lower()
                                    if answer.isdigit():
                                        player.max_health = int(answer) 
                                        print("Done")
                                    else: 
                                        print("You Dont Know How To Type Numbers?")
                                        player.health = -1337
                                        break
                                if hacker_stat == "health":
                                    answer = input("What Is Your New Health\n").lower()
                                    if answer.isdigit():
                                        player.health = int(answer) 
                                        print("Done")
                                    else: 
                                        print("You Dont Know How To Type Numbers?")
                                        player.health = -1337
                                        break
                                if hacker_stat == "power":
                                    answer = input("What Is Your New Power\n").lower()
                                    if answer.isdigit():
                                        player.power = int(answer) 
                                        print("Done")
                                    else: 
                                        print("You Dont Know How To Type Numbers?")
                                        player.health = -1337
                                        break
                                if hacker_stat == "defense":
                                    answer = input("What Is Your New Defense\n").lower()
                                    if answer.isdigit():
                                        player.defense = int(answer) 
                                        print("Done")
                                    else: 
                                        print("You Dont Know How To Type Numbers?")
                                        player.health = -1337
                                        break
                                if hacker_stat == "hacker":
                                    print("You No Longer Hacker")
                                    player.hacker = False 
                                    break 
                            elif hacking == "teleport":
                                answer = input("Where Do You Want To Go, Type Room Number\n").lower()
                                if answer.isdigit():
                                    go_to_room(player, int(answer))
                                    print("Done")
                                else: 
                                    print("You Dont Know How To Type Numbers?")
                                    player.health = -1337
                                    break
                            elif hacking == "item":
                                answer = input("What Do You Want\n").lower()
                                for item in items: 
                                    if item.name.lower() == answer: 
                                        give_item(player, item, player)
                                        print("Done")
                            elif hacking == "custom":
                                answer = input("What Type Of Item: Armor, Weapon, Consumable\n")
                                answer2 = input("What Is The Name\n")
                                answer3 = input("What Is The Description\n")
                                answer4 = input("What Is The Power\n")
                                items.append(Item(answer, answer2, answer3, answer4))
                            elif hacking == "kill":
                                if player.battling == True:
                                    room_monster.health = -1337
                                else: 
                                    player.health = -1337
                                print("Terminated") 
                            elif hacking == "close":
                                print("Goodbye")
                                break 
                elif action == "exit":
                    print("Goodbye, adventurer.")
                    time.sleep(1)
                    break
                else:
                    print("Invalid action. Type 'help' for a list of possible actions.")
    # execute functions 
    game_intro()
       
main()