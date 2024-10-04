import random

class adventureGame:
    def __init__(self):
        self.player_sword = 0
        self.player_hp = 100
        self.player_dmg = 10
        self.player_gold = 10
        self.slime_hp = 50
        self.slime_dmg = 15
        self.dragon_hp = 1000
        self.dragon_dmg = 30

    def menu(self):
        while True:
            choose = int(input(f"Good luck with monsters adventurer!\nYour gold: {self.player_gold}\n1-Go to shop\n2-Go to cave\n3-Quit\n"))
            if choose == 1:
                buy_sell = int(input("What do you wanna do?\n1-Buy\n2-Sell\n3-Return\n"))
                if buy_sell == 1:
                    self.buy_shop()
                elif buy_sell == 2:
                    self.sell_shop()
                elif buy_sell == 3:
                    continue
            elif choose == 2:
                monster_num = int(input("Which monster do you wanna fight?\n1-Slime\n2-Dragon\n"))
                if monster_num == 1:
                    action = int(input("What do you wanna do?\n1-Attack\n2-Run\n"))
                    if action == 1:
                        self.slime_attack()  
                    elif action == 2:
                        self.run_slime()
                elif monster_num == 2:
                    action1 = int(input("What do you wanna do?\n1-Attack\n2-Run\n"))
                    if action1 == 1:
                        self.dragon_attack()  
                    elif action1 == 2:
                        self.run_dragon()
            elif choose == 3:
                print("Game over ;)")
                break

    def buy_shop(self):
        if self.player_sword == 0:
            sword_num = int(input("Hi adventurer, what do you wanna buy?\n1-Wooden sword 20 GOLD (+20 dmg)\n2-Silver Sword 50 GOLD (+50 dmg)\n3-Iron Sword 100 GOLD (+100 dmg)\n4-Shield 20 GOLD (-20 dmg)\n"))
            if sword_num == 1 and self.player_gold >= 20:
                print("You got wooden sword!")
                self.player_dmg += 20
                self.player_gold -= 20
                self.player_sword = 1
            elif sword_num in [2, 3, 4]:
                print("You should buy the wooden sword first!")
            else:
                print("You don't have enough gold!")
        elif self.player_sword == 1:
            sword_num2 = int(input("Hi adventurer, what do you wanna buy?\n2-Silver Sword 50 GOLD (+50 dmg)\n3-Iron Sword 100 GOLD (+100 dmg)\n4-Shield 20 GOLD (-20 dmg)\n"))
            if sword_num2 == 2 and self.player_gold >= 50:
                print("You got silver sword!")
                self.player_dmg += 30  
                self.player_gold -= 50
                self.player_sword = 2
            elif sword_num2 == 3:
                print("You should buy the silver sword first!")
            elif sword_num2 == 4:
                print("You should buy the silver sword first!")
            else:
                print("You don't have enough gold!")
        elif self.player_sword == 2:
            sword_num3 = int(input("Hi adventurer, what do you wanna buy?\n3-Iron Sword 100 GOLD (+100 dmg)\n4-Shield 20 GOLD (-20 dmg)\n"))
            if sword_num3 == 3 and self.player_gold >= 100:
                print("You got iron sword!")
                self.player_dmg += 50  
                self.player_gold -= 100
                self.player_sword = 3
            elif sword_num3 == 4:
                print("You should buy the iron sword first!")
            else:
                print("You don't have enough gold!")
        elif self.player_sword == 3:
            sword_num4 = int(input("Hi adventurer, what do you wanna buy?\n4-Shield 20 GOLD (-20 dmg)\n"))
            if sword_num4 == 4 and self.player_gold >= 20:
                print("You got shield!")
                self.dragon_dmg -= 20  
                self.player_gold -= 20
                self.player_sword = 4
            else:
                print("You don't have enough gold!")
        else:
            print("You bought everything!")

    def sell_shop(self):
        sell_num = int(input(f"Hi adventurer, enter the number of sword you wanna sell!\nYour gold: {self.player_gold}\n1-Wooden sword\n2-Silver sword\n3-Iron sword\n4-Shield\n"))
        if sell_num == 1 and self.player_sword >= 1:
            print("You sold wooden sword!")
            self.player_gold += 20
            self.player_dmg -= 20
            self.player_sword = 0
        elif sell_num == 2 and self.player_sword >= 2:
            print("You sold silver sword!")
            self.player_gold += 50
            self.player_dmg -= 50
            self.player_sword = 1
        elif sell_num == 3 and self.player_sword >= 3:
            print("You sold iron sword!")
            self.player_gold += 100
            self.player_dmg -= 100
            self.player_sword = 2
        elif sell_num == 4 and self.player_sword == 4:
            print("You sold shield!")
            self.player_gold += 20
            self.dragon_dmg += 20 
            self.player_sword = 3
        else:
            print("Are you sure that you have this sword?")
    
    def slime_attack(self):
        print("Player attacks slime")
        self.slime_hp -= self.player_dmg
        if self.slime_hp <= 0:
            print("Slime is dead!")
            self.player_gold += 10
            self.slime_hp = 50
            print("WOW! Player heals himself with slime soul!")
            self.player_hp= 100
            self.menu()
            return
        print(f"Player hp: {self.player_hp} Slime hp: {self.slime_hp}")
        print("Slime attacks!")
        self.player_hp -= self.slime_dmg
        if self.player_hp <= 0:
            print("You died! Game over.")
            exit()
        print(f"Player hp: {self.player_hp} Slime hp: {self.slime_hp}")
    
    def run_slime(self):
        number = random.randint(1, 2)
        if number == 1:
            print("You couldn't escape!")
            self.player_hp -= self.slime_dmg
        else:
            print("You escaped successfully!")
        print(f"Player hp: {self.player_hp} Slime hp: {self.slime_hp}")

    def dragon_attack(self):
        print("Player attacks dragon")
        self.dragon_hp -= self.player_dmg
        if self.dragon_hp <= 0:
            print("THE WINNER IS THE ADVENTURER!")
            exit()
        print(f"Player hp: {self.player_hp} Dragon hp: {self.dragon_hp}")
        print("Dragon attacks!")
        self.player_hp -= self.dragon_dmg
        if self.player_hp <= 0:
            print("You died! Game over.")
            exit()
        print(f"Player hp: {self.player_hp} Dragon hp: {self.dragon_hp}")
    
    def run_dragon(self):
        number = random.randint(1, 2)
        if number == 1:
            print("You couldn't escape!")
            self.player_hp -= self.dragon_dmg
        else:
            print("You escaped successfully!")
        print(f"Player hp: {self.player_hp} Dragon hp: {self.dragon_hp}")


game = adventureGame()

game.menu()