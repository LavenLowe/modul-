
class GameOver(Exception):
	def gameover(self, name):
		scores = open('scores.txt', 'w')
		scores.write('NAME: ')
		scores.write(name)
		scores.write('\nYOUR SCORE: ')
		scores.write('10')

		

class EnemyDown(Exception):
	def Score(self, name):
		save_scores = open('scores.txt', 'a')
		save_scores.write('Best scores:\n')
		scores.write('NAME: ')
		scores.write(name)
		scores.write('\nSCORE: ')
		scores.write('10')

name = input('Enter your name:')
gg = GameOver()
gg.gameover(name)
ed.EnemyDown()
ed.Score(name)