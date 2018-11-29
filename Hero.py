import random
import os
import time

relics = ["Shroud of Night","Hand of Midas"]

class Hero(object):
    # what does every class have?
    def __init__(self,name,health = 10,power = 5,gold = 0):
        self.name = name
        self.base_health = health
        self.health = self.base_health
        self.power = power
        self.base_power = power
        self.gold = gold
        self.shroud_of_night = False
        self.hand_of_midas = False
        self.revive_potion = False
    def cheer_hero(self):
        print ("Welcome, brave %s!" % self.name)
    def take_damage(self,amount_of_damage):
        if self.shroud_of_night == True:
            if random.random() < 0.15:
                print("The Shroud of Night glistens, and you avoid the monster's attack!")
            else:
                self.health -= amount_of_damage
        else:    
            self.health -= amount_of_damage
    def is_alive(self):
        # if("elixer_of_life" in self.potions):
        #     return True
        # else:
        if self.health <= 0 and self.revive_potion == True:
            self.revive_potion = False
            print("You used your potion to survive the blow!")
            self.health = self.base_health
            return True
        else:
            return self.health > 0
    def choose_class(self):
        print ("""Choose a class (1, 2, 3, or 4)
        1. The Berserker
            Known for brute strength and resilience, but not much else.
        2. The Mage
            Capable of very powerful spells, but not consistency.
        3. The Rogue
            Looking to get rich. Values money almost as much as their own life.
        4. The Paladin
            Protected by a higher power. Possesses extraordinary healing capabilities.""")
        self.class_choice = input()
        if (self.class_choice == "1"):
            self.base_health = 30
            self.base_power = 8
            self.power = 8
            self.gold = 0
            self.health = self.base_health
        if (self.class_choice == "2"):
            self.base_health = 20
            self.base_power = 9
            self.power = self.base_power
            self.gold = 30
            self.health = self.base_health
        if (self.class_choice == "3"):
            self.base_health = 20
            self.base_power = 7
            self.power = self.base_power
            self.gold = 90
            self.health = self.base_health
        if (self.class_choice == "4"):
            self.base_health = 30
            self.base_power = 7
            self.power = self.base_power
            self.gold = 30
            self.health = self.base_health
    def getOptionsText(self):
        if(self.class_choice == "1"):
            message = """You have %d health and %d power.
            The %s has %d health and %d power.
            What do you want to do?
            1. Attack
            2. Meditate
            3. Adrenaline Rush
            4. Flee""" 
            return message
        if(self.class_choice == "2"):
            message = """You have %d health and %d power.
            The %s has %d health and %d power.
            What do you want to do?
            1. Attack
            2. Meditate
            3. Cast Spell
            4. Flee""" 
            return message
        if(self.class_choice == "3"):
            message = """You have %d health and %d power.
            The %s has %d health and %d power.
            What do you want to do?
            1. Attack
            2. Meditate
            3. Steal
            4. Flee""" 
            return message
        if(self.class_choice == "4"):
            message = """You have %d health and %d power.
            The %s has %d health and %d power.
            What do you want to do?
            1. Attack
            2. Greater Heal
            3. Flee""" 
            return message 
    def getSpecial(self,monster):
        if(self.class_choice == "1"):
            print("The thrill of battle invigorates you! Power doubled.")
            self.power = self.power * 2
            self.special_used = True
        if(self.class_choice == "2"):
            outcome = random.randint(1,3)
            if(outcome == 1):
                print ("Oh no! Your chant failed.")
            if(outcome == 2):
                print ("You cast a terrifying pillar of flame!")
                return monster.take_damage(self.power * 100)
            if(outcome == 3):
                print ("Your spell backfires! Your health is reduced.")
                self.health -= 5
        if(self.class_choice == "3"):
            monster.giveGold(self)
    def getHeroAction(self, theHero, monster):
        user_input = input()
        os.system("clear")
        if user_input == "1":
            monster.take_damage(theHero.power)
            print ("You have done %d damage to the monster!" % theHero.power)
        elif user_input == "2":
            if(theHero.class_choice == "4"):
                healAmount = random.randint(10,15)
                if ((self.health + healAmount) > self.base_health):
                    theHero.health = self.base_health
                else:
                    theHero.health += healAmount
            else:
                healAmount = random.randint(3,7)
                if ((self.health + healAmount) > self.base_health):
                    theHero.health = self.base_health
                else:
                    theHero.health += healAmount
            print ("Through some strange power, you recover %d health!" % healAmount)
        elif user_input == "3":
            if (theHero.class_choice == "4"):
                os.system("clear")
                flee_result = random.randint(1,2)
                if flee_result == 1:
                    os.system("clear")
                    print ("The monster strikes you as you flee!")
                    Hero.take_damage(self, monster.power)
                    print ("Your health is now %d." % self.health)
                    print("Hit enter to continue.")
                    if theHero.is_alive() == False:
                        print ("You have been slain. Your adventure comes to an end.")
                        game_On = False
                if flee_result == 2:
                    gold_lost = random.randint(10,15)
                    self.gold -= gold_lost
                    if self.gold < 0:
                        self.gold = 0
                    print("In your hurry to escape, you drop %d gold!" % gold_lost)
                    print("You now have %d gold." % self.gold)
                    print("""
                    Hit enter to continue.""")
                return "flee"
            else:
                theHero.getSpecial(monster)
        elif user_input == "4" and self.class_choice != "4":
            flee_result = random.randint(1,2)
            if flee_result == 1:
                os.system("clear")
                print ("The monster strikes you as you flee!")
                Hero.take_damage(self, monster.power)
                print ("Your health is now %d." % self.health)
                print("""
                    Hit enter to continue.""")
                if theHero.is_alive() == False:
                    print ("You have been slain. Your adventure comes to an end.")
                    game_On = False
            if flee_result == 2:
                gold_lost = random.randint(10,15)
                self.gold -= gold_lost
                if self.gold < 0:
                    self.gold = 0
                print("In your hurry to escape, you drop %d gold!" % gold_lost)
                print("You now have %d gold." % self.gold)
                print("""
                    Hit enter to continue.""")
            return "flee"
        else:
            return "error"
    def getRelic(self):
            if (len(relics) != 0):
                rand = random.randint(0,len(relics)-1)
                relic_drop = relics[rand]
                if relic_drop == "Shroud of Night":
                    self.shroud_of_night = True
                    relics.pop(rand)
                    os.system("clear")
                    print("You picked up the Shroud of Night, giving you a 15% chance to avoid enemy attacks!")
                    input("""
                        Hit enter to continue.""")
                if relic_drop == "Hand of Midas":
                    self.hand_of_midas = True
                    relics.pop(rand)
                    os.system("clear")
                    print("You picked up the Hand of Midas, giving you 50% more gold wherever you may find it!")
                    input("""
                        Hit enter to continue.""")
    def reset_buffs(self):
        self.power = self.base_power
        if self.health > self.base_health:
            self.health = self.base_health
    def increaseHealth(self,health_cost):
        os.system("clear")
        if self.gold >= health_cost:
            self.base_health += 5
            self.health += 5
            self.gold -= health_cost
            print("Health increased by 5!")
            print("You now have %d gold." % self.gold)
            input("""
            Hit enter to continue.""")
        else:
            print("You do not have enough gold.")
            input("""
            Hit enter to continue.""")
    def increasePower(self,power_cost):
        os.system("clear")
        if self.gold >= power_cost:
            self.base_power += 1
            self.power += 1
            self.gold -= power_cost
            print("Power increased by 1!")
            print("You now have %d gold." % self.gold)
            input("""
            Hit enter to continue.""")
        else:
            print("You do not have enough gold.")
            input("""
            Hit enter to continue.""")
    def addPotion(self,potion_cost):
        if self.revive_potion == True:
            os.system("clear")
            print("You are already carrying a potion.")
            input("""
            Hit enter to continue.""")
        if self.gold >= potion_cost:
            self.gold -= potion_cost
            self.revive_potion = True
            os.system("clear")
            print("You bought the potion.")
            print("You now have %d gold." % self.gold)
            input("""
            Hit enter to continue.""")
        if self.gold < potion_cost and self.revive_potion == False:
            os.system("clear")
            print("You do not have enough gold.")
            input("""
            Hit enter to continue.""")
    def fullHeal(self,heal_cost):
        os.system("clear")
        print("The old woman guides you to a cozy room at the back of the shop.")
        print("Health fully restored.")
        self.gold -= heal_cost
        input("""
            Hit enter to continue.""")