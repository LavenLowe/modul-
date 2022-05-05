from models import Player, Enemy

if __name__ == '__main__':
    enm = Enemy()
    pl = Player()
    while True:
        pl.allowed_attacks()
        enm.select_attack()




