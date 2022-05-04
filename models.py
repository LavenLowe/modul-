from random import randint

class Player:
	score = 0
	def allowed_attacks(self, enemy_lives):
		player_attack = int(input('Enter you attack type: '))
		if player_attack == 0:
			print('You have chosen to attack the enemy')
			attack = enemy_lives - 1
			print('Enemy lifebar: ', enemy_lives)
			if enemy_lives == 1 or enemy_lives == 2:
				pass

			elif enemy_lives <= 0:
				print('Enemy dead')
				
		elif player_attack == 1:
			print('You chose to defend')



class Enemy:
	def __init__(self, players_lives, type_attack):
		self.players_lives = players_lives
		self.type_attack = type_attack		
		super().__init__(players_lives, type_attack)


	def select_attack(self):
		if type_attack == 0:
			print('Enemy attack you')
			attack = players_lives - 1
			print('Player lifebar: ', attack)

			if players_lives == 0:
				#class GameOver
				print('GameOver')
			else:
				pass
		elif type_attack == 1:
			print('Enemy defend')

name = input("Fullname: ")
if __name__ == '__main__':
	players_lives = 10
	while players_lives >= 0:
		type_attack = randint(0, 1)
		enm = Enemy(10, type_attack)
		pl = Player(randint(0,2))
