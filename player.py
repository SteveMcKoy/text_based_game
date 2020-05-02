class Player:

	def __init__(self, name, role, health, max_health, mana, max_mana, stamina, max_stamina, crit_chance, hit_rate, alignment):
		self.name = name
		self.role = role
		self.health = health
		self.max_health = max_health
		self.mana = mana
		self.max_mana = max_mana
		self.stamina = stamina
		self.max_stamina = max_stamina		
		self.crit_chance = crit_chance
		self.hit_rate = hit_rate
		self.level = 1
		self.xp = 0
		self.xp_cap = 20 #amount of xp needed before leveling up, should increase upon leveling up
		self.alignment = 0
		self.weapon = "iron shortsword"
		self.offhand = "glowing glove of magic arrows"
		self.head_gear = "tin plate helmet"
		self.body_armour = "tin plate armour"
		self.attacks = ["[|(2)]sword swing", "[*(2)]magic arrow"]
		self.items = ["minor health potion", "minor health potion", "minor health potion"]

	def decrement_health(self, health_down):
		self.health = self.health - health_down
	def increment_health(self, health_up):
		self.health = self.health + health_up

	def decrement_mp(self, mana_down):
		self.mana = self.mana - mana_down
	def increment_mp(self, mana_up):
		self.mana = self.mana + mana_up

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

	def increment_crit_chance(self, crit_chance_up):
		self.crit_chance = self.crit_chance + crit_chance_up

	def decrement_hit_rate(self, hit_rate_down): #enemy cast an accuracy debuff
		self.hit_rate = self.hit_rate - hit_rate_down

	def decrement_alignment(self, alignment_down):
		self.alignment = self.alignment - alignment_down
	def increment_alignment(self, alignment_up):
		self.alignment = self.alignment + alignment_up

	def add_attack(self, attack_added):
		self.attacks.append(attack_added)
	def delete_attack(self, attack_deleted):
		self.attacks.remove(item_deleted)

	def add_item(self, item_added):
		self.items.append(item_added)
	def delete_item(self, item_deleted):
		self.items.remove(item_deleted)
