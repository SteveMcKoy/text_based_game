from player import Player
from enemy import Enemy
from items import Item
import numpy
import random
import sys

def role_selection():
	name = input("What is your pawn's name? \n> ").strip()
	print(name + ". Yes, good. That is a very nice name. ")
	is_valid = False
	while is_valid == False: #Loops the question untill the player gives a valid answer
		q = input("Please give " + name + " a role. \n1. Fighter \n2. Caster \n3. Marauder \n4. Mesmerist \n5. Palidin \n6. Articifer \n> ").strip() #First Question
		if q == "1":
			is_valid = True #Idenifies this answer as valid an moves on to the next question
			false_role = "fighter"
			print("A " + false_role + "? A good choice indeed.")
		elif q == "2":
			is_valid = True
			false_role = "caster"
			print("A " + false_role + "? A good choice indeed.")
		elif q == "3":
			is_valid = True
			false_role = "marauder"
			print("A " + false_role + "? A good choice indeed.")
		elif q == "4":
			is_valid = True
			false_role = "mesmerist"
			print("A " + false_role + "? A good choice indeed.")
		elif q == "5":
			is_valid = True
			false_role = "palidin"
			print("A " + false_role + "? A good choice indeed.")
		elif q == "6":
			is_valid = True
			false_role = "articifer"
			print("A " + false_role + "? A good choice indeed.")
		else:
			print ("You have failed to answer the question validly. Try again.")
	is_valid = False
	while is_valid == False:
		q = input("Please choose " + name + "'s race. \n1. Human \n2. Lich \n3. Lycanthrope \n4. Dragoniod \n5. Dullahan \n6. Golem \n> ").strip()
		if q == "1":
			is_valid = True
			false_race = "human"
			print("I see, so you picked a " + false_race + ". Intresting, that is a rare choice.")
		elif q == "2":
			is_valid = True
			false_race = "lich"
			print("I see, so you picked a " + false_race + ". Intresting, that is a rare choice.")
		elif q == "3":
			is_valid = True
			false_race = "lycanthrope"
			print("I see, so you picked a " + false_race + ". Intresting, that is a rare choice.")
		elif q == "4":
			is_valid = True
			false_race = "dragoniod"
			print("I see, so you picked a " + false_race + ". Intresting, that is a rare choice.")
		elif q == "5":
			is_valid = True
			false_race = "dullahan"
			print("I see, so you picked a " + false_race + ". Intresting, that is a rare choice.")
		elif q == "6":
			is_valid = True
			false_race = "golem"
			print("I see, so you picked a " + false_race + ". Intresting, that is a rare choice.")
		else:
			print("You have failed to answer the question validly. Try again.")
	is_valid = False
	while is_valid == False: #Change this later
		q = input("Please come up with a background for " + name + ". \n1. Average citizen called to adventure" +
			"\n2. Orphan that was taken in by a powerful crime lord and must do jobs for him in extange for a home" +
			"\n3. Noble looking for a more exciting life outside of the castle" +
			"\n4. Alchemist's aprentice that who wants to know everything about the world around them" +
			"\n5. Refugee from a fallen kingdom looking for a way to exact revenge agaist the empire that conqured it" +
			"\n6. Traveling entertainer looking for a more intresting story to tell \n> ").strip()
		if q == "1":
			is_valid = True
			print("So that is the story of your pawn. Very creative, I'm invested in seeing what happens to them next.")
		elif q == "2":
			is_valid = True
			print("So that is the story of your pawn. Very creative, I'm invested in seeing what happens to them next.")
		elif q == "3":
			is_valid = True
			print("So that is the story of your pawn. Very creative, I'm invested in seeing what happens to them next.")
		elif q == "4":
			is_valid = True
			print("So that is the story of your pawn. Very creative, I'm invested in seeing what happens to them next.")
		elif q == "5":
			is_valid = True
			print("So that is the story of your pawn. Very creative, I'm invested in seeing what happens to them next.")
		elif q == "6":
			is_valid = True
			print("So that is the story of your pawn. Very creative, I'm invested in seeing what happens to them next.")
		else:
			print("You have failed to answer the question validly. Try again.")

	player = Player(name, "human adventurer", 20, 20, 20, 20, 20, 20, 20, 6, 2, 0)

	input_check = False
	while input_check == False:
		print("")
		character_acknowledge = input("Your pawn is now fully developed. All that is left to do is bind these traits to "
			+ player.name + ". Do you fully acknowledge "
			+ player.name + " as your creation, and vow to fairly lead their life in the direcion chosen by the dice? \n> ").strip()
		if character_acknowledge == "yes":
			print("")
			input_check = True
			return player
		elif character_acknowledge == "no":
			test = input("Oh dear. Do you want to recreate your pawn? \n> ").strip()

			input_check = True
			if test == "yes":
				print("Alright, let's try this again")
				print("")
				player = role_selection()
			elif test == "no":
				print("Well then I don't know what else to do. I guess this isn't your type of game, so I suggest you should just shut it down. \n Game Over")
				sys.exit()
				#else:
					#print ("You have failed to answer the question validly. Try again.")
		else:
			print ("You have failed to answer the question validly. Try again.")
			input_check == False

	return player
print('')

#ITEM LIST HERE
minor_health_potion = Item("minor health potion", 0, None, 0, None, 15, 0, 0, "An opaque, rust collored mixture. It has no taste, but has a consistancy disgustingly similar to mucus. It's dull color is a reflection of its poor quality due to cheap materials.")
empty_potion_bottle = Item("empty potion bottle", 0, None, 0, None, 0, 0, 0, "An empty glass bottle.")

def enemy_generator(pLevel): #takes enemys from the enemy file and gives them stats
	enemy_name = open(r"enemy_names.py")
	random_name = enemy_name.readlines()
	enemy_name.close()
	name_roll = random.randint(0, 4)
	name = random_name[name_roll].rstrip()
	if name == "crawling claw":
		archetype = "tiny evil undead"
		attack = random.randint(1, 4)
		loot = Item("nothing", 0, None, 0, None, 0, 0, 0, "literally nothing.")
		xp_amount = 1
		crit_chance = 50
		hit_rate = 1
		health = 15 * pLevel
		description = "The severed hands of a past murderer animated via dark magic. Due to the fact that they require very little skill to create and are bound completly to the will of thier their creator, they are commonly used by fledgling necromancers."
	elif name == "lemure":
		archetype = "medium evil devil"
		attack = random.randint(1, 4)
		loot = Item("lemure fat", 0, None, 0, None, 2, 0, 0, "Fat from a lemure. Can be used to make a bad healing potion.")
		xp_amount = 2
		crit_chance = 50
		hit_rate = 1
		health = 25 * pLevel
		description = "A devil in the form of a molten, stinking blob of flesh. They are among the weakest devils in existance, and only their only abilty a slow, weak regeneration ability. Due to the fact that they are almost completly mindless and cannot make decisions for themselves, lemures are often exploited as shock troops or slave labor by summoners or other devils. They can also be harvested for their fat, which can be used to make a weak healing potion."
	elif name == "goblin skeleton":
		archetype = "small evil undead humaniod"
		attack = random.randint(1, 6)
		loot = Item("nothing", 0, None, 0, None, 0, 0, 0, "literally nothing.")
		xp_amount = 2
		crit_chance = 50
		hit_rate = 1
		health = 20 * pLevel
		description = "The reanimated bones of a goblin. The same dark magic that infuses its bones and binds joints together also gives the goblins rudimentery intelligence and decision making skills, alhough these are mainly reactionary behaviors in battle. Though dead, goblin skeletons retain their malicious nature, and have been known to turn on weaker masters."
	elif name == "homunculus":
		archetype = "tiny evil construct"
		attack = random.randint(1, 6)
		loot = Item("nothing", 0, None, 0, None, 0, 0, 0, "literally nothing.")
		xp_amount = 1
		crit_chance = 2
		hit_rate = 1
		health = 25 * pLevel
		description = "A tiny humaniod doll made of a mixture of clay, ash, mandrake root, and blood. Ordered by it's creator to complete a task, the homunculus will not stop trying untill it completes it's goal. It seems this one has been charged with a fire spell..."
	elif name == "grey ooze":
		archetype = "small mindless slime"
		attack = random.randint(3, 9)
		loot = Item("nothing", 0, None, 0, None, 0, 0, 0, "literally nothing.")
		xp_amount = 3
		crit_chance = 15
		hit_rate = 1
		health = 20 * pLevel
		description = "Stone turned liquid and by chaos magic. Thriving in darkness and attracted to movement and warmth, reckless adventurers often fall to its acidic attacks. It's body can dissove most organtic materials with relavitive ease. I wonder if that can be used for something..."

	enemy = Enemy(name, health, archetype, attack, loot, xp_amount, crit_chance, hit_rate, description) #spell/attack list out
	return enemy

def player_attack(pLevel, hit_rate, crit_chance, max_damage): #how much damage the player does apon attacking
	roll = random.randint(0, 20)
	hit = roll * hit_rate
	if hit <= 6:
		damage_dealt = 0
	if hit > 6:
		dmg_roll = random.randint(1, max_damage)
		damage_dealt = pLevel * dmg_roll
		crit_roll = random.randint(0, crit_chance)
		if crit_roll == crit_chance:
			print("Critical hit!")
			damage_dealt = dmg_roll * pLevel * 2

	return damage_dealt

def enemy_damage(pLevel, enemy): #how much damage the enemy does apon attacking
	roll = random.randint(0, 20)
	hit = roll * enemy.hit_rate
	if hit <= 6:
		damage_dealt = 0
	if hit > 6:
		dmg_roll = random.randint(1, enemy.attack)
		damage_dealt = pLevel * dmg_roll
		crit_roll = random.randint(0, enemy.crit_chance)
		if crit_roll == enemy.crit_chance:
			print("Critical hit!")
			damage_dealt = dmg_roll * pLevel * 2

	return damage_dealt

def enemy_encounter(): #decides if you fight an enemy apon taking an action
	encounter_roll = random.randint(0, 1)
	if encounter_roll >= 1:
		enemy_interaction(player)

def enemy_attack(enemy_damage, pLevel, enemy, keep_interacting):
	if enemy.health >= 1:
		enemy_damage = enemy_damage(player.level, enemy)
		if player.health > 0 and enemy.health > 0 and enemy_damage > 0:
			player.health = player.health - enemy_damage
			print("The " + enemy.name + " hits you for " + str(enemy_damage) + " damage. Your health is now  " + str(player.health) + ".")
		elif enemy_damage == 0:
			print("The enemy attacks... it missed!")
		elif player.health <= 0:
			player.health = player.health - enemy_damage
			print("The " + enemy.name + "hits you for " + str(enemy_damage) + " damage. \nGame Over")
		elif enemy.health <= 0:
			keep_interacting = False

	return keep_interacting

def enemy_interaction(pLevel): #the actual fight
	enemy = enemy_generator(player.level)
	print("You encounter a " + enemy.name)
	keep_interacting = True
	while (enemy.health > 0 or player.health > 0) and keep_interacting == True:
		player_input_valid = False
		while player_input_valid == False and keep_interacting == True:
			choice = input("\nWhat do you want to do? \n1. attack\n2. item\n3. examine\n4. run\n> ").strip()
			if choice == "attack": #attack
				print(player.attacks)
				which_attack = input("How do you want to attack?\n> ").strip() #choose which attack
				if which_attack == "sword swing":
					player.stamina = player.stamina - 2
					damage_dealt = player_attack(player.level, player.hit_rate, player.crit_chance, player.max_damage)
					enemy.health = enemy.health - damage_dealt
					if damage_dealt > 0 and enemy.health > 0:
						print("You hit the " + enemy.name + " for " + str(damage_dealt) + " damage. It's health is now " + str(enemy.health) + ".")
						enemy_attack(enemy_damage, pLevel, enemy, keep_interacting)
					elif damage_dealt == 0:
						print("You missed!")
						enemy_attack(enemy_damage, pLevel, enemy, keep_interacting)
					elif enemy.health <= 0:
						print("You deal the finishing blow to the " + enemy.name + ".")
						player.xp = player.xp + enemy.xp_amount
						print("You got " + str(enemy.xp_amount) + " xp.")
						if enemy.loot.name != "nothing":
							player.add_item(enemy.loot)
						print("The enemy dropped " + str(enemy.loot.name) + ".")
						keep_interacting = False
				if which_attack == "magic arrow":
					player.mana = player.mana - 2
					damage_dealt = player_attack(player.level, player.hit_rate, player.crit_chance, player.max_damage)
					enemy.health = enemy.health - damage_dealt
					if damage_dealt > 0 and enemy.health > 0:
						print("You hit the " + enemy.name + " for " + str(damage_dealt) + " damage. It's health is now " + str(enemy.health) + ".")
						enemy_attack(enemy_damage, pLevel, enemy, keep_interacting)
					elif damage_dealt == 0:
						print("You missed!")
						enemy_attack(enemy_damage, pLevel, enemy, keep_interacting)
					elif enemy.health <= 0:
						print("You deal the finishing blow to the " + enemy.name + ".")
						player.xp = player.xp + enemy.xp_amount
						print("You got " + str(enemy.xp_amount) + " xp.")
						if enemy.loot.name != "nothing":
							player.add_item(enemy.loot)
						print("The enemy dropped " + str(enemy.loot.name) + ".")
						keep_interacting = False
					player_input_valid = True
			elif choice == "item": #item
				print(player.items)
				which_item = input("Which item do you want to use?\n> ").strip()
				if which_item == "minor health potion":
					player.delete_item("minor health potion")
					player.add_item("empty potion bottle")
					player.health = player.health + 15
					if player.health > player.max_health:
						player.health = player.max_health
					print("You used a minor health potion. Your health is now " + str(player.health) + ".")
					enemy_attack(enemy_damage, pLevel, enemy, keep_interacting)
				else:
					print("You do not have that item.")
				player_input_valid = True
			elif choice == "examine": #examine
				print(enemy.description)
				player_input_valid = True
			elif choice == "run": #run
				print("You run away")
				player_input_valid = True
				keep_interacting = False
			else:
				print("That is not an action you can take")

def help():
	print("\ncommand list: " +
		"\n[help]- displays a list of commands" +
		"\n[compendium](category){entry}- displays information about various things in the world" +
		"\n[profile]- displays information about your character" +
		"\n[look](object)- decribes the object you want looked at" +
		"\n[examine](item)- describes an item in your inventory or a currently equipped weapon or gear." +
		"\n[use](item)- uses an item in your inventory"+
		"\n[walk](direction)- moves you in a cardinal direction of your choosing."
		"\n\ngeneral tips: " +
		"\n-you can press the \"up\" and \"down\" keys to scroll through a list of your previously used commands" +
		"\n-attacks with a [|(x)] sign are physical and attacks with a [*(x)] sign are magical. The number inside the parenthesis is the attack's cost. Physical attacks cost stamina points while magical attacks cost mana points. Both are fully regained after battle, but be sure to monitor your resoucres, lest you find youself in the middle of a fight with no way to attack... ")

def profile(player):
	xp_until_level_up = player.xp_cap - player.xp
	print("\nname: " + player.name +
		"\nalignment: " + str(player.alignment) +
		"\nlevel: " + str(player.level) +
		"\nxp until level up: " + str(xp_until_level_up) +
		"\nhealth: " + str(player.health) + "/" + str(player.max_health) +
		"\nmagic: " + str(player.mana) + "/" + str(player.max_mana) +
		"\nstamina: " + str(player.stamina) + "/" + str(player.max_stamina) +
		"\nweapon: " + str(player.weapon) +
		"\noffhand: " + str(player.offhand) +
		"\nhead gear: " + str(player.head_gear) +
		"\nbody armour: " + str(player.body_armour))
	print("items:")
	for item in player.items:
		print(item.name)

def look():
	look_at_what = input("\nWhat do you want to look at?\n> ").strip()
	if look_at_what == "door":
		print("A flimsy, unlocked, iron door. It won't be hard to open it.")
	elif look_at_what == "wall":
		print("A wall made from fibrous mycelium packed into a material as durable as wood, often called mushroom wood. This wall was roughly made, and probaly not put up by anthing too stong or smart.")
	elif look_at_what == "cavern":
		print("A dimly lit cavern with glowing mushrooms and lichens covering the walls. You are not that far underground, and the path out is pretty easy to navigate.")
	else:
		print("That is not something you can look at.")

def examine(player):
	examine_what = input("\nWhat do you want to examine?\n> ")
	for item in player.items:
		if examine_what == item.name:
			print(item.description)
			break
	'''if examine_what == "iron shortsword":
		print("A simple shortsword that makes for the most basic of weapons in the caves. Due to the confined nature of the underground, larger, more unweildly weapons aren't generally used unless the user is exeptionally skilled.")
	elif examine_what == "glowing glove of magic arrows":
		print("A leather glove stitched together with enchanted string. The enchantment allows the user to gather mana from the air and shape it into an arrow to pierce that target. It also causes the air around it to glow, providing a nice amount of light for your work in the dark caverns.")
	elif examine_what == "tin plate helmet":
		print("A helmet made from tin plates.")
	elif examine_what == "Tin plate armour":
		print("A set of armour made from tin plates. Includes a chestplate, arm braces, and greaves.")
	elif examine_what == "minor health potion":
		print(player.minor_health_potion.description)
	else:
		print("That is not a thing you can examine.")'''

def use(player):
	print("items:")
	for item in player.items:
		print(item.name)
	use_what = input("\nWhat do you want to use?\n> ")
	item_exist = player.check_item(use_what)
	if use_what == "minor health potion" and item_exist == True:
		player.delete_item("minor health potion")
		player.add_item(empty_potion_bottle)
		player.health = player.health + 15
		if player.health > player.max_health:
			player.health = player.max_health
		print("You used a minor health potion. Your health is now " + str(player.health) + ".")
	else:
		print("You do not have that item.")

def move():
	print("e")



##############################################################################################
print("Once upon a time, in the days when the stars shone far fewer in " +
	"the sky than they do now, the gods of light and order and destiny " +
	"vied with the gods or darkness and chaos and chance to see who would control the world. " +
	"They waged this struggle with dice. There were victories and defeats, but " +
	"there was no resolution. The gods tired of dice, so they created pawns and " +
	"a board to place them on. They created a world, and the many tribes to populate it. " +
	"These pawns adventure, they achieve victory, suffer defeat, find treasure " +
	"or happiness, and ultimately die. In time, the gods came to love these " +
	"characters and their doings. The dice fall against them sometimes, but that's " +
	"just how it goes. Into this world there appeared on particular adventurer. They were " +
	"unexceptional, a human with no distinguishing traits at all. They were " +
	"liked by all the gods, but great things were not expected of them. "+
	"But this adventurer was different from the others. They were always " +
	"thinking, strategizing, and acting. They did not let the gods roll the dice. " +
	"They were not highborn, not especially capable, neither did they have " +
	"any “cheating” powers. This surprised the gods very much. They would not save the " +
	"world. They might not even change anything. They were just another pawn. " +
	"But even so, they did not let the gods roll the dice. Hence, even the gods " +
	"did not know how their adventures would end. \n")

player = role_selection()



is_valid = False
while is_valid == False:
	cont_1 = input("Then it is done. These core atributes are now-\n.\n.\n.\n I'm sorry, it seem that your pawn as rejected your gifts. Would you like to try again?\n> ").strip()
	if cont_1 =="yes":
		print("")
		is_valid = True
	elif cont_1 == "no":
		print("Um... ok?  Well there's nothing else to do, so you can just leave I guess... \n\n Game Over")
		sys.exit()
	else:
		print("\nYou have failed to answer the question validly. Try again.")

is_valid = False
while is_valid == False:
	cont_1 = input("Then let us try this again.... something something core atr- WHY?! Your pawn refuses to exept your gifts!\n.\n.\n.\n" +
	"Okay, here is what we'll do. I'm commanding you to watch over this pawn, and wait until it is weak enough to be taken under you command. " +
	"Once they are, it should be a simple matter to get them to obey the dice. In the mean time, you may roll for their enemies instead. Do you think you will be able to do that?\n> ").strip()
	if cont_1 =="yes":
		print("Good. I trust that you will be able to get this willful pawn under control. Go on and regain the controll that was stollen from you.\n\n")
		is_valid = True
	elif cont_1 == "no":
		print("...Well I guess being a new god, this is kind of a tough task for you. Do not worry about it, I will get someone else to do it. \n\n Game Over")
		sys.exit()
	else:
		print("\nYou have failed to answer the question validly. Try again.")

#player = Player("sfdalasd", "human", 20, 20, 20, 20, 20, 20, 20, 6, 2, 0) #test object

encounter = enemy_encounter()
is_valid = False
while is_valid == False:
	desc = input("\nYou're standing in front of a rusted iron door. " +
		"The fibrous, purple-grey wall surrounding it was seemingly built into the mouth of the cave that stands before you, one of the many in the dank, dimly lit cavern you stand in now. " +
		"Behind the door is the home of your target. " +
		"[type \"help\" to view a list of commands]\n> ").strip()
	if desc == "help":
		help()
	elif desc == "compendium":
		print("e")
	elif desc == "examine":
		examine(player)
	elif desc == "profile":
		profile(player)
	elif desc == "look":
		look()
	elif desc == "use":
		use(player)
	elif desc == "move":
		print("e")
	else:
		print("That is not an action you can take.")

#player = Player("sfdalasd", "human", 1, 20, 20, 20, 20, 20, 20, 2, 0) #test object
#encounter = enemy_encounter()
