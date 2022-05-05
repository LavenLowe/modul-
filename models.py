from random import randint, randrange
from exceptions import GameOver, EnemyDown
import time
class Player:
	
	def __init__(self):
		self.enemy_lives = randint(1, 3)
	def allowed_attacks(self):
		player_attack = int(input('Enter you attack type: '))
		if player_attack == 0:
			print('You have chosen to attack the enemy')
			self.enemy_lives -= 1
			print('Enemy lifebar: ', self.enemy_lives)
			if self.enemy_lives == 1 or self.enemy_lives == 2:
				pass

			elif self.enemy_lives <= 0:
				print('Enemy dead')
				
				
		elif player_attack == 1:
			print('You chose to defend')
		else:
			print('Wrong key!!!')
			exit()

class Enemy:
	
	def __init__(self):
		self.player_lives = 10

	def select_attack(self):
		
		type_attack = randint(0, 1)
		if type_attack == 0:
			print('Enemy attack you')
			self.player_lives -= 1
			print('Player lifebar: ', self.player_lives)
		elif type_attack == 1:
			print('Enemy defend')
		if self.player_lives <= 0:
			print('Yor scores: ', 10)
			time.sleep(2)
			print('See you next time!')
			time.sleep(2)
			raise GameOver


