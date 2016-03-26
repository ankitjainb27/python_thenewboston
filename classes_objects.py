class Enemy:
    life = 3

    def __init__(self, x):
        self.life = x

    def attack(self):
        print "ouch!"
        self.life -= 1

    def checklife(self):
        if self.life <= 0:
            print 'I am dead'
        else:
            print str(self.life) + " life left"


enemy1 = Enemy(20)
enemy2 = Enemy(18)

enemy1.attack()
enemy1.attack()
enemy1.checklife()
enemy2.checklife()
