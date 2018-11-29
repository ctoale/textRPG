from random import randint
from Enemy import Enemy

class TaurusDemon(Enemy):
    def __init__(self):
        self.name = "Taurus Demon"
        self.health = 50
        self.power = 10
        self.gold = 50
        super(TaurusDemon,self).__init__()
    def getMonsterAction(self, theHero, monster, defaultAction = None):
        message = theHero.getOptionsText()
        print (message % (theHero.health,theHero.power,monster.name, monster.health, monster.power))
        if defaultAction == None:
            self.monsterAction = randint(1,5)
        else:
            self.monsterAction = defaultAction
        if (self.monsterAction == 1 or self.monsterAction == 2 or self.monsterAction == 3):
            monsterActionText = "attack!"
        if (self.monsterAction == 4 or self.monsterAction == 5):
            monsterActionText = "slam the ground!"
            self.monsterAction = "stun"
        print ("The monster prepares to " + monsterActionText)
        return self.monsterAction
    def performMonsterAction(self, theHero, monster):
        if monster.is_alive():
            if (self.monsterAction == 1 or self.monsterAction == 2 or self.monsterAction == 3):
                theHero.take_damage(monster.power)
                print ("The monster hits you for %d damage." % monster.power)
                print ("Your health is now %d." % theHero.health)
            if (self.monsterAction == "stun"):
                print ("The monster slams the ground, stunning and slightly damaging you!")
                theHero.take_damage(3)
                return "stun"