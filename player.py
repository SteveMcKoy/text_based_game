class Player:

	def __init__(self, name, role, health,  magic, stamina, crit_chance, hit_rate, alignment):
		self.name = name
		self.role = role
		self.health = health
		self.magic = magic
		self.stamina = stamina
		self.crit_chance = crit_chance
		self.hit_rate = hit_rate
		self.inventory_space = 8
		self.level = 1
		self.xp = 0
		self.xp_cap = 20 #amount of xp needed before leveling up, should increase upon leveling up
		self.alignment = 0
		self.items = ["health_potion", "health_potion", "health_potion"]

	def decrement_health(self, health_down):
		self.health = self.health - health_down
	def increment_health(self, health_up):
		self.health = self.health + health_up

	def decrement_mp(self, magic_down):
		self.magic = self.magic - magic_down
	def increment_mp(self, magic_up):
		self.magic = self.magic + magic_up

	def decrement_stamina(self, stamina_down):
		self.stamina = self.stamina - stamina_down
	def increment_stamina(self, stamina_up):
		self.stamina = self.stamina + stamina_up

	def increment_xp(self, xp_up):
		self.xp = self.xp + xp_up
	def increment_level(self):
		self.level = self.level + 1
		self.xp = 0
	def xp_cap(self):
		self.xp_cap = self.level ** 2 + 20

	def increment_inventory_space(self, inventory_space_up):
		self.inventory_space = 8 + inventory_space_up

	def increment_crit_chance(self, crit_chance_up):
		self.crit_chance = self.crit_chance + crit_chance_up

	def decrement_hit_rate(self, hit_rate_down): #enemy cast an accuracy debuff
		self.hit_rate = self.hit_rate - hit_rate_down

	def decrement_alignment(self, alignment_down):
		self.alignment = self.alignment - alignment_down
	def increment_alignment(self, alignment_up):
		self.alignment = self.alignment + alignment_up

	def add_item(self, item_added):
		self.items.append(item_add)
	def delete_item(self, item_deleted):
		self.items.remove(item_deleted)
#attributes: name, level, xp, role, hp, mp, stamina, crit chance, inventory space

#name
	#get name
	#set name

#role
	#get role
	#set role

#HP
	#get HP
	#set HP
	#increment HP
	#decrement HP

#MP
	#get MP
	#set MP
	#increment MP
	#decrement MP

#Stamina
	#get stamina
	#set stamina
	#increment stamina
	#decrement stamina

#crit chance
	#get crit chance
	#set crit chance
	#increment crit chance

'''inventory space, the one thing that isnt passed in our init function
	get space
	start with 8 spaces
	increment space'''
