class Enemy(object):
    def __init__(self):
        pass
    def take_damage(self,amount_of_damage):
        self.health -= amount_of_damage
    def is_alive(self):
        return self.health > 0
    def giveGold(self, theHero):
        if theHero.hand_of_midas == True:
            print ("You got %s gold!" % int(self.gold * 1.5))
            theHero.gold += (self.gold * 1.5)
            print ("You now have %s gold." % int(theHero.gold))
        else:
            print ("You got %s gold!" % self.gold)
            theHero.gold += self.gold
            print ("You now have %s gold." % theHero.gold)