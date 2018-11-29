from random import randint
from Enemy import Enemy

class Vampire(Enemy):
    def __init__(self):
        randomPower = randint(8,11)
        randomHealth = randint(13,17)
        self.name = "Vampire"
        self.health = randomHealth
        self.power = randomPower
        self.gold = 15
        super(Vampire,self).__init__()
    def getMonsterAction(self, theHero, monster, defaultAction = None):
        message = theHero.getOptionsText()
        print (message % (theHero.health,theHero.power,monster.name, monster.health, monster.power))
        if defaultAction == None:
            self.monsterAction = randint(1,6)
        else:
            self.monsterAction = defaultAction
        if (self.monsterAction == 1 or self.monsterAction == 2 or self.monsterAction == 3):
            monsterActionText = "attack!"
        if (self.monsterAction == 4 or self.monsterAction == 5):
            monsterActionText = "gather strength!"
        if (self.monsterAction == 6):
            monsterActionText = "heal!"
        print ("The monster prepares to " + monsterActionText)
        return self.monsterAction
    def performMonsterAction(self, theHero, monster):
        if monster.is_alive():
            if (self.monsterAction == 1 or self.monsterAction == 2 or self.monsterAction == 3):
                theHero.take_damage(monster.power)
                print ("The monster hits you for %d damage." % monster.power)
                print ("Your health is now %d" % theHero.health)
            if (self.monsterAction == 4 or self.monsterAction == 5):
                mpowerIncrease = 2
                monster.power += mpowerIncrease
                print ("The monster gathers strength! Power increased by %d." % mpowerIncrease)
            if (self.monsterAction == 6):
                healAmount = randint(3,7)
                monster.health += healAmount
                print ("The monster uses dark energy to fortify itself! Health recovered by %d." % healAmount)