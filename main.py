from player import Player 
from enemy import Enemy
import numpy
import random
import sys

def role_selection():
	name = input("What is your pawn's name? \n> ")
	print (name + ". Yes, good. That is a very nice name. ")
	is_valid = False 
	while is_valid == False: #Loops the question untill the player gives a valid answer
		q = input ("Please give " + name + " a role. \n1. Fighter \n2. Caster \n3. Marauder \n4. Mesmerist \n5. Palidin \n6. Articifer \n> ") #First Question
		if q == "1":	
			is_valid = True #Idenifies this answer as valid an moves on to the next question
			false_role = "fighter"
			print ("A " + false_role + "? A good choice indeed.")
		elif q == "2":
			is_valid = True
			false_role = "caster"
			print ("A " + false_role + "? A good choice indeed.")
		elif q == "3":
			is_valid = True
			false_role = "marauder"
			print ("A " + false_role + "? A good choice indeed.")
		elif q == "4":
			is_valid = True
			false_role = "mesmerist"
			print ("A " + false_role + "? A good choice indeed.")
		elif q == "5":
			is_valid = True
			false_role = "palidin"
			print ("A " + false_role + "? A good choice indeed.")
		elif q == "6":
			is_valid = True
			false_role = "articifer"
			print ("A " + false_role + "? A good choice indeed.")
		else:
			print ("You have failed to answer the question validly. Try again.")	
	is_valid = False
	while is_valid == False:
		q = input ("Please choose " + name + "'s race. \n1. Human \n2. Lich \n3. Lycanthrope \n4. Dragoniod \n5. Dullahan \n6. Golem \n> ")
		if q == "1":
			is_valid = True
			false_race = "human"
			print ("I see, so you picked a " + false_race + ". Intresting, that is a rare choice.")
		elif q == "2":
			is_valid = True
			false_race = "lich"
			print ("I see, so you picked a " + false_race + ". Intresting, that is a rare choice.")
		elif q == "3":
			is_valid = True
			false_race = "lycanthrope"
			print ("I see, so you picked a " + false_race + ". Intresting, that is a rare choice.")
		elif q == "4":
			is_valid = True
			false_race = "dragoniod"
			print ("I see, so you picked a " + false_race + ". Intresting, that is a rare choice.")
		elif q == "5":
			is_valid = True
			false_race = "dullahan"
			print ("I see, so you picked a " + false_race + ". Intresting, that is a rare choice.")
		elif q == "6":
			is_valid = True
			false_race = "golem"
			print ("I see, so you picked a " + false_race + ". Intresting, that is a rare choice.")
		else:
			print ("You have failed to answer the question validly. Try again.")
	is_valid = False
	while is_valid == False: #Change this later
		q = input ("Please come up with a background for " + name + ". \n1. Average citizen called to adventure" + 
			"\n2. Orphan that was taken in by a powerful crime lord and must do jobs for him in extange for a home" + 
			"\n3. Noble looking for a more exciting life outside of the castle" + 
			"\n4. Alchemist's aprentice that who wants to know everything about the world around them" + 
			"\n5. Refugee from a fallen kingdom looking for a way to exact revenge agaist the empire that conqured it" + 
			"\n6. Traveling entertainer looking for a more intresting story to tell \n> ")
		if q == "1":
			is_valid = True
			print ("So that is the story of your pawn. Very creative, I'm invested in seeing what happens to them next.")
		elif q == "2":
			is_valid = True
			print ("So that is the story of your pawn. Very creative, I'm invested in seeing what happens to them next.")
		elif q == "3":
			is_valid = True
			print ("So that is the story of your pawn. Very creative, I'm invested in seeing what happens to them next.")
		elif q == "4":
			is_valid = True
			print ("So that is the story of your pawn. Very creative, I'm invested in seeing what happens to them next.")
		elif q == "5":
			is_valid = True
			print ("So that is the story of your pawn. Very creative, I'm invested in seeing what happens to them next.")
		elif q == "6":
			is_valid = True
			print ("So that is the story of your pawn. Very creative, I'm invested in seeing what happens to them next.")
		else:
			print ("You have failed to answer the question validly. Try again.")

	player = Player(name, "human", 20, 20, 20, 20, 2, 0)

	input_check = False
	while input_check == False:
		print("")
		character_acknowledge = input("Your pawn is now fully developed. All that is left to do is bind these traits to " 
			+ player.name + ". Do you fully acknowledge " 
			+ player.name + " as your creation, and vow to fairly lead their life in the direcion chosen by the dice? \n> ")
		if character_acknowledge == "yes":
			print("")
			input_check = True
			return player		
		elif character_acknowledge == "no":
			test = input("Oh dear. Do you want to recreate your pawn? \n> ")

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

def enemy_generator(pLevel):
	enemy_name = open(r"enemy_names.py")
	random_name = enemy_name.readlines()
	enemy_name.close()
	name_roll = 4 #random.randint(0, 4)
	name = random_name[name_roll].rstrip()
	if name == "crawling claw":
		archetype = "tiny evil undead"
		attack = random.randint(1, 4) 
		loot = "none"
		xp_amount = 1
		crit_chance = 50
		hit_rate = 1
		health = 15 * pLevel
	elif name == "lemure":
		archetype = "medium evil devil"
		attack = random.randint(1, 4) 
		loot = "none"
		xp_amount = 2
		crit_chance = 50
		hit_rate = 1
		health = 25 * pLevel
	elif name == "goblin skeleton":
		archetype = "small evil undead humaniod"
		attack = random.randint(1, 6) 
		loot = "none"
		xp_amount = 2
		crit_chance = 50
		hit_rate = 1
		health = 20 * pLevel
	elif name == "homunculus":
		archetype = "tiny evil undead"
		attack = random.randint(1, 6) 
		loot = "none"
		xp_amount = 1
		crit_chance = 2
		hit_rate = 1
		health = 25 * pLevel
	elif name == "grey ooze":
		archetype = "small mindless slime"
		attack = random.randint(3, 9) 
		loot = "none"
		xp_amount = 3 
		crit_chance = 15
		hit_rate = 1
		health = 20 * pLevel

	enemy = Enemy(name, health, archetype, attack, loot, xp_amount, crit_chance, hit_rate) #spell/attack list out
	return enemy

def player_attack(pLevel, hit_rate, crit_chance):
	roll = random.randint(0, 20)
	hit = roll * hit_rate
	if hit <= 6:
		print("you missed")
		damage_dealt = 0
	if hit > 6:
		dmg_roll = random.randint(1, 20)
		damage_dealt = pLevel * dmg_roll
		crit_roll = random.randint(0, crit_chance)
		if crit_roll == crit_chance:
			print("Critical hit!")
			damage_dealt = dmg_roll * pLevel * 2

	return damage_dealt

def enemy_attack(pLevel, enemy):
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

def enemy_interaction(pLevel):
	enemy = enemy_generator(player.level)
	print("You encounter a " + enemy.name)
	is_valid = False
	while is_valid == False or enemy.health > 0:
		choice = input("What do you want to do? \n1. attack\n2. item\n3. examine\n4. run\n> ")
		if choice == "1":
			damage_dealt = player_attack(player.level, player.hit_rate, player.crit_chance)
			enemy.health = enemy.health - damage_dealt
			if enemy.health > 0:
				print("You hit the " + enemy.name + ". It's health is now " + str(enemy.health) + ".")
			elif enemy.health <= 0:
				print("You deal the finishing blow to the " + enemy.name + ".")
			is_valid = True
		elif choice == "2":
			print(player.items)
			player.delete_item("health_potion")
			print(player.items)
			is_valid = True
		elif choice == "3":
			print("")
		elif choice == "4":
			print("You run away")
			is_valid = True
			break
		elif player.health <= 0:
			print("\nGame Over")
			break
		else:
			print("That is not an action you can take")

		enemy_damage = enemy_attack(player.level, enemy)
		player.health = player.health - enemy_damage
		if player.health > 0:
			print("The " + enemy.name + " hits you for " + str(enemy_damage) + ". Your health is now  " + str(player.health) + ".")
		elif enemy.health <= 0:
			print("The " + enemy.name + "hits you for " + str(enemy_damage) + ". \nGame Over")

def enemy_encounter():
	encounter_roll = 1#random.randint(0, 1)
	if encounter_roll >= 1:
		enemy_interaction(player)

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
#player = Player("sdfas", "human", 100, 20, 20, 2, 100, 0) #test object


is_valid = False
while is_valid == False:
	cont_1 = input("Then it is done. These core atributes are now-\n.\n.\n.\n I'm sorry, it seem that your pawn as rejected your gifts. Would you like to try again?\n> ")
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
	"Once they are, it should be a simple matter to get them to obey the dice. In the mean time, you may roll for their enemies instead. Do you think you will be able to do that?\n> ")
	if cont_1 =="yes":
		print("Good. I trust that you will be able to get this willful pawn under control. Go on and regain the controll that was stollen from you.\n\n\n")
		is_valid = True
	elif cont_1 == "no":
		print("...Well I guess being a new god, this is kind of a tough task for you. Do not worry about it, I will get someone else to do it. \n\n Game Over")
		sys.exit()
	else:
		print("\nYou have failed to answer the question validly. Try again.")

#player = Player("sdfas", "human", 40, 20, 20, 20, 2, 0) #test object
encounter = enemy_encounter()






