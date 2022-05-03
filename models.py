from random import randint

class Player:
	name = input("Fullname: ")
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

	def select_attack(self, players_lives: int, type_attack = int):
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

if __name__ == '__main__':
	players_lives = 10
	type_attack = randint(0, 1)
	while players_lives >= 0:
		enm = Enemy()
		pl = Player()
		pl.allowed_attacks(randint(0,2))
		enm.select_attack(players_lives, type_attack)
