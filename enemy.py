class Enemy:
	def __init__ (self, name, health, archetype, attack, loot, xp_amount, crit_chance, hit_rate): #spell/attact list out
		self.archetype = archetype 
		self.name = name
		self.health = health
		self.attack = attack 
		self.loot = loot #comes from a giant item table and selected with a random number generator
		self.xp_amount = xp_amount #Varies based on tier
		self.crit_chance = crit_chance
		self.hit_rate = hit_rate

	def decrement_health(self, health_down):
		self.health = self.health - health_down
	def increment_health(self, health_up):
		self.health = self.health + hp_health

	def decrement_attack(self, attack_down): #player cast an attack debuff
		self.attack = self.attack - attack_down
	def increment_attack(self, attack_up): #enemy cast an attack buff
		self.attack = self.attack + attack_up

	def decrement_hit_rate(self, hit_rate_down): #player cast an accuracy debuff
		self.hit_rate = self.hit_rate - hit_rate_down




