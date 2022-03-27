from tkinter  import *
import math
import random

random.seed()
roomAmount = 0
    
class PlayerClass:
    #Level Player starts out a
    HP = 150
    AP = 10
    Bag = 0
    EXP = 0

class BossClass:
    #Boss class parameters that will be filled later
    def __init__(self, HP, AP, EXP):
        self.HP = HP
        self.AP = AP
        self.EXP = EXP

class TreasureClass:
    #Treasure found in shop
    def __init__(self, num):
        self.coins = num

class ItemClass:
    
    #Number item to give to item to see what it will be
    #0 - Nothing, 1 - HP, 2 - AP 3 - DP
    #cost is the amount the item is
    #upgrade is the amount added to the player when dropped
    def __init__(self, stock, cost, upgrade):
        self.stock = stock
        self.cost = cost
        self.upgrade = upgrade
    
    
#For the player to buy and upgrade their sword and health
class ShopClass:
    def __init__(self,stock1, cost1, upgrade1, stock2, cost2, upgrade2):#, stock3, cost3, upgrade3):
        self.item1 = ItemClass(stock1, cost1, upgrade1)
        self.item2 = ItemClass(stock2, cost2, upgrade2)
        #self.item3 = ItemClass(stock3, cost3, upgrade3)

class EmptyRoom:
    x = -1

def createRoom(typeR):
    if typeR in range(0, 5):
        bossHP = random.randrange(15, 40)
        bossAP = random.randrange(5, 25)
        bossXP = 100 - bossHP
        bossObj = BossClass(bossHP, bossAP, bossXP)
        #print("This boss has HP: ", int(bossObj.HP))
        #print("Boss created")
        return bossObj
    elif typeR in range(6, 8):
        coinNum = random.randrange(15, 50)
        coinObj = TreasureClass(coinNum)
        #print("Treasure created")
        return coinObj
    elif typeR in range(9, 10):
        costList = [0] * 3
        upgradeList = [0] * 3
        for i in range(3):
            costList[i] = random.randrange(5, 15)
            upgradeList[i] = random.randrange(5, 10)
        shopObj = ShopClass(1, costList[0], upgradeList[0], 1, costList[1], upgradeList[1])#, 1, costList[2], upgradeList[2])
        #print("Shop created")
        return shopObj
    else:
        emptyObj = EmptyRoom()
        return emptyObj 
        
        
class RoomClass:
    def __init__(self, typeNum):
        self.roomType = int(typeNum)

def BossAttack(m):
    choiceAP = 0
    if(m == 1):
        choiceAP = random.randrange(0,10)
        if choiceAP in range(0,4):
            return 0
        elif choiceAP in range(5, 8):
            return 1
        else:
            return 2
    else:
        choiceAP = random.randrange(0,10)
        if choiceAP in range(0,6):
            return 0
        elif choiceAP in range(7, 9):
            return 1
        else:
            return 2

def yourAttack():
    choiceAP = random.randrange(0, 10)
    if choiceAP in range(0, 5):
        return 0
    elif choiceAP in range(6, 8):
        return 1
    else:
        return 2
        
def printPlayer(player):
    print("Player Stats:\nHP:", player.HP)
    print("AP: ", player.AP)

def printBoss(boss):
    print("Boss HP: ", boss.HP)

def printBossMenu():
    print("Choose an Option: ")
    print("A - Attack\nD-Dodge\nE-Escape")

def printShopMenu():
    print("What are you buying?")
    #print("A - Item1\nS-Item2\nD - Item3\nF - Move on")
    print("A - Item1\nS-Item2\nF - Move on")


def startButton():
    new = Tk()
    amountVar = StringVar()
    amountVar.set("")
    new.geometry("500x500")
    
    canvas1 = Canvas(new, width = 500, height = 500, bg = "black")
    canvas1.create_text(250, 150, text = "How many rooms will you tranverse?", fill = "white", font = ('Helvetica 15 bold'))

    b10 = Button(canvas1, text = "Ten Rooms", command=lambda m = "10":
                 inputButton(m))
    b10.place(x=100, y = 250)

    b50 = Button(canvas1, text = "Fifty Rooms", command=lambda m = "50":
                 inputButton(m))
    b50.place(x=250, y = 250)

    b100 = Button(canvas1, text = "Hundred Rooms", command=lambda m = "100":
                  inputButton(m))
    b100.place(x=400, y = 250)

    canvas1.pack()

    master.destroy()
    new.mainloop


def inputButton(m):
    print("You want " + m + " rooms!")
    roomAmount = int(m)
    fakeBoss = BossClass(0, 0, 0)
    myObj = (0, fakeBoss) 
    myRoom = RoomClass(0)
    room_type = [myRoom.roomType] * roomAmount
    room_list = [myObj] * roomAmount
    #print(len(room_type))
    levelCap = 100
    g = 0
    while g < roomAmount:
        room_type[g] = random.randrange(0,11)
        g += 1

    #print(room_type)
    i = 0
    #for n in room_type:
     #   roomObj = createRoom(int(n))
      #  room_list[i] = roomObj

    #roomWindow = Tk()
    player = PlayerClass()
    attackRoll = 0
    dodgeChance = 0
    r = 0
    #print(room_list)
    while r < roomAmount:
        #thisRoom = room_list[r]
        roomObj = createRoom(int(room_type[r]))
        #print("This room is type ",room_type[r])
        
        if int(room_type[r]) in range(0, 5):
            Health = int(roomObj.HP)
            Attack = int(roomObj.AP)
            XP = int(roomObj.EXP)
            print("This room has a Boss!")
            while Health > 0:
                printBossMenu()
                printPlayer(player)
                printBoss(roomObj)
                userInput = input()
                if(userInput == 'A' or userInput == 'a'):
                    attackRoll = yourAttack()
                    dodgeRoll = 0
                    if attackRoll == 0:
                        print("You attacked and hit!");
                        Health = Health - random.randrange(3, int(player.AP))
                        roomObj.HP = Health
                    elif attackRoll == 1:
                        print("You did a critical attack!")
                        Health -= int(player.AP)
                        roomObj.HP = Health
                    else:
                        print("You missed!")
                elif(userInput == 'D' or userInput == 'd'):
                    print("You try to dodge the attack!")
                    dodgeChance = 1
                else:
                    print("You have left the dungeons in fear...")
                    exit()

                print("The Boss attacked!")
                attackRoll = BossAttack(dodgeChance)
                if attackRoll == 0:
                    print("Boss hit!")
                    loss = random.randrange(1, Attack)
                    player.HP -= loss
                    dodgeRoll = 0
                    if player.HP <= 0:
                        print("You have died. GAME OVER!")
                        exit()
                elif attackRoll == 1:
                    print("Boss missed!")
                    dodgeRoll = 0
                else:
                    print("Boss has done critical hit!")
                    player.HP -= Attack
                    if player.HP <= 0:
                        print("You have died. GAME OVER!")
                        exit()
                    dodgeRoll = 0
            
            print("The boss is down and you gained ", XP,"! You move on...")
            player.EXP += XP
            if(player.EXP > levelCap):
                print("Level up!")
                player.AP += 1
                levelCap += levelCap
            

        elif int(room_type[r]) in range(6, 8):
            print("This room has Treasure!")
            coins = int(roomObj.coins)
            print("You open the treasure and find", coins, "!")
            player.Bag += coins
        elif int(room_type[r]) in range(9, 10):
            print("This room has a Shop!")
            shopInput = ""
            while shopInput != 'f' and shopInput != 'F':
                printShopMenu()
                item1 = roomObj.item1
                item2 = roomObj.item2
                #item3 = roomObj.item3
                print("HP: ", item1.upgrade, "Cost: ", item1.cost)
                print("Sword upgrade: ", item2.upgrade, "Cost: ", item2.cost)
                print("You have ", player.Bag, " coins!")
                shopInput = input()
                if(shopInput == 'A' or shopInput == 'a'):
                    if(player.Bag == 0):
                        print("Not enough coins, stranger!")
                    else:
                        if(item1.stock == 0):
                            print("OUT OF STOCK!")
                        else:
                            item1.stock = 0
                            player.HP += int(item1.upgrade)
                            player.Bag -= int(item1.cost)

                elif(shopInput == 'S' or shopInput == 's'):
                    if(player.Bag <= 0):
                        print("Not enough coins, stranger!")
                    else:
                        if(item2.stock == 0):
                            print("OUT OF STOCK")
                        else:
                            item2.stock = 0
                            player.AP += int(item2.upgrade)
                            player.Bag -= int(item2.cost)
            
            print("Have a great day stranger!")
        else:
            print("This room is empty!")
            print("Moving on...")
        r += 1
    print("CONGRATULATIONS! You have completed Rynth's Dungeon!")
#def testButton():
#    print("This is a test. Stop here pls!")

def endButton():
    exit()

#First Screen Creation
master = Tk()
master.geometry("500x500")

canvas = Canvas(master, width = 500, height = 500, bg = "SpringGreen2")
canvas.create_text(250, 100, text = "Rynth's Dungeons", fill = "red", font = ('Helvetica 15 bold'))
canvas.create_arc(50, 150, 500, 250, fill = "gray")
canvas.create_oval(100, 150, 150, 200, fill = "purple") 

canvas.pack()

b = Button(canvas, text = "End Me", command=endButton)
b.place(x = 200, y = 250)
b1 = Button(canvas, text = "Start", command=startButton)
b1.place(x=200, y =200)

master.mainloop()













