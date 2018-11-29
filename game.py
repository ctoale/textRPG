import os
import time
# from [NAMEOFFILE] import [CLASS]
from Hero import Hero
from Goblin import Goblin
from Vampire import Vampire
from WallCrawler import WallCrawler
from random import randint
from TaurusDemon import TaurusDemon


hero_name = input("What is your name, brave one? ")
theHero = Hero(hero_name)
theHero.cheer_hero()
theHero.choose_class()
os.system("clear")

game_On = True
has_rested = False
monsters_slain = 0
health_cost = 30
power_cost = 30
potion_cost = 30
heal_cost = 10
taurus_killed = False

# Current problems:
# Berserker can use special more than once

while(game_On == True):
    print ("""Choose your next action.
        1. Explore deeper.
        2. Rest for a while.
        3. Visit Mysterious Shop.""")
    choice = input()
    os.system("clear")
    if choice == "1":
        randMonster = randint(1,2)
        if monsters_slain < 6 and taurus_killed == True:
            if randMonster == 1:
                monster = WallCrawler()
            if randMonster == 2:
                monster = Mimic()
            valid = True
            print ("You have encountered the %s!" % monster.name)
            while(theHero.is_alive() and monster.is_alive()):
                player_can_move = True
                if valid == True:
                    monsterResult = monster.getMonsterAction(theHero, monster)
                else:
                    monsterResult = monster.getMonsterAction(theHero, monster, monsterResult)
                valid = True
                if monsterResult == "stun":
                    player_can_move = False
                if player_can_move == True:
                    heroResult = theHero.getHeroAction(theHero, monster)
                    if heroResult == "error":
                        valid = False
                    if heroResult == "flee":
                        is_alive = theHero.getHeroAction(theHero, monster)
                        if is_alive == False:
                            game_On = False
                            break
                        break
                if valid == True:
                    monster.performMonsterAction(theHero, monster)
                    if theHero.is_alive() == False:
                        print ("You have been slain. Your adventure comes to an end.")
                        game_On = False
                    if monster.is_alive() == False:
                        # os.system("say Hooray. Thou hast killed the monster!")
                        print ("You have killed the monster!")
                        Hero.reset_buffs(theHero)
                        has_rested = False
                        monster.giveGold(theHero)
                        monsters_slain += 1
                        input("""
                        Hit enter to continue.""")
                        os.system("clear")
                        break
                    input("""
                        Hit enter to continue.""")
                os.system("clear")
        if monsters_slain < 3:
            if randMonster == 1:
                monster = Goblin()
            if randMonster == 2:
                monster = Vampire()
            valid = True
            print ("You have encountered the %s!" % monster.name)
            while(theHero.is_alive() and monster.is_alive()):
                player_can_move = True
                if valid == True:
                    monsterResult = monster.getMonsterAction(theHero, monster)
                else:
                    monsterResult = monster.getMonsterAction(theHero, monster, monsterResult)
                valid = True
                if monsterResult == "stun":
                    player_can_move = False
                if player_can_move == True:
                    heroResult = theHero.getHeroAction(theHero, monster)
                    if heroResult == "error":
                        valid = False
                    if heroResult == "flee":
                        is_alive = theHero.getHeroAction(theHero, monster)
                        if is_alive == False:
                            game_On = False
                            break
                        break
                if valid == True:
                    monster.performMonsterAction(theHero, monster)
                    if theHero.is_alive() == False:
                        print ("You have been slain. Your adventure comes to an end.")
                        game_On = False
                    if monster.is_alive() == False:
                        # os.system("say Hooray. Thou hast killed the monster!")
                        print ("You have killed the monster!")
                        Hero.reset_buffs(theHero)
                        has_rested = False
                        monster.giveGold(theHero)
                        monsters_slain += 1
                        input("""
                        Hit enter to continue.""")
                        os.system("clear")
                        break
                    input("""
                        Hit enter to continue.""")
                os.system("clear")
        
        if monsters_slain == 3 and taurus_killed == False:
            os.system("clear")
            print("You have angered the monster's boss!")
            time.sleep(2)
            os.system("clear")
            monster = TaurusDemon()
            print ("You have encountered the monster boss, %s!" % monster.name)

            while(theHero.is_alive() and monster.is_alive()):
                player_can_move = True
                if monsterResult == "stun":
                    player_can_move = False
                    print("You are stunned and cannot act!")
                    input("""
                    Hit enter to continue.""")
                if valid == True:
                    monsterResult = monster.getMonsterAction(theHero, monster)
                else:
                    monsterResult = monster.getMonsterAction(theHero, monster, monsterResult)
                valid = True
                if player_can_move == True:
                    heroResult = theHero.getHeroAction(theHero, monster)
                    if heroResult == "error":
                        valid = False
                    if heroResult == "flee":
                        is_alive = theHero.getHeroAction(theHero, monster)
                        if is_alive == False:
                            game_On = False
                            break
                        break
                if valid == True:
                    monster.performMonsterAction(theHero, monster)
                    if theHero.is_alive() == False:
                        print ("You have been slain. Your adventure comes to an end.")
                        game_On = False
                if monster.is_alive() == False:
                    # os.system("say Hooray. Thou hast killed the monster!")
                    print ("You have killed the monster boss!")
                    Hero.reset_buffs(theHero)
                    has_rested = False
                    monster.giveGold(theHero)
                    taurus_killed = True
                    input("""
                    Hit enter to continue.""")
                    theHero.getRelic()
                    os.system("clear")
                    break
                input("""
                        Hit enter to continue.""")
                os.system("clear")
    if choice == "2" and has_rested == True:
        os.system("clear")
        print("You cannot rest again at the moment.")
        time.sleep(2)
    if choice == "2" and has_rested == False:
        os.system("clear")
        print("You stop for a short rest.")
        rest_amount = randint(3,7)
        theHero.health += rest_amount
        print("You recovered %d health." % rest_amount)
        has_rested = True
        time.sleep(2)
    if choice == "3":
        os.system("clear")
        print("Old Woman: Welcome to my shop...")
        print("You have %d gold." % theHero.gold)
        print ("""
        1. Increase Stats
        2. Buy Reviving Elixir (30 Gold)
        3. Rest (10 Gold)
        4. Leave""")
        shop_option = input()
        if shop_option == "1":
            os.system("clear")
            print("""Which stat do you wish to increase?
            """)
            print("1. Health + 5 (%d Gold)" % health_cost)
            print("2. Power + 1 (%d Gold)" % power_cost)
            print("3. Cancel")
            upgrade_choice = input()
            if upgrade_choice == "1":
                theHero.increaseHealth(health_cost)
            if upgrade_choice == "2":
                theHero.increasePower(power_cost)
        if shop_option == "2":
            theHero.addPotion(potion_cost)
        if shop_option == "3":
            theHero.fullHeal(heal_cost)
        if shop_option == "4":
            pass
    os.system("clear")