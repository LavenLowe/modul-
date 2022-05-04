import models
import time
class GameOver:
	def gameover(self, players_lives, name):
		try:
			if players_lives == 9:
				print('Yor scores: 'scores)
				time.sleep(2)
				print('Try next time better')
				time.sleep(2)
				break


		except:
			scores = open('scores.txt', 'w')
			scores.write('NAME: ')
			scores.write(name)
			scores.write('\nSCORES: ')

class EnemyDown:
	pass
	#scores += 1

if __name__ == '__main__':
	go = GameOver()
	go.gameover(models.players_lives, models.name)