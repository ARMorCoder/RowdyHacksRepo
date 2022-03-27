from tkinter  import *
import math
import random


random.seed()

#canvas1.create_text(250, 250, text = "Game start", fill = "white", font = ('Helvetica 15 bold'))

roomAmount = 0
    
class PlayerClass:
    #Level Player starts out a
    HP = 25
    AP = 10
    DP = 2
    Coins = 0
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
    def __init__(self, item, cost, upgrade):
        self.item = item
        self.cost = cost
        self.upgrade = upgrade
    
    

class ShopClass:
    def __init__(self, item1, cost1, upgrade1, item2, cost2, upgrade2, item3, cost3, upgrade3):
        self.item1 = ItemClass(item1, cost1, upgrade1)
        self.item2 = ItemClass(item2, cost2, upgrade2)
        self.item3 = ItemClass(item3, cost3, upgrade3)

    

def createRoom(typeR):
    if typeR in range(0, 5):
        bossHP = random.randrange(15, 40)
        bossAP = random.randrange(5, 25)
        bossXP = 100 - bossHP
        bossObj = BossClass(bossHP, bossAP, bossXP)
        print("Boss created")
        return bossObj
    elif typeR in range(6, 8):
        coinNum = random.randrange(15, 50)
        coinObj = TreasureClass(coinNum)
        print("Treasure created")
        return coinObj
    elif typeR in range(9, 10):
        itemList = [0] * 3
        costList = [0] * 3
        upgradeList = [0] * 3
        for i in range(3):
            itemList[i] = random.randrange(0, 2)
            costList[i] = random.randrange(5, 15)
            upgradeList[i] = random.randrange(5, 10)
        shopObj = ShopClass(itemList[0], costList[0], upgradeList[0], itemList[1], costList[1], upgradeList[1], itemList[2], costList[2], upgradeList[2])
        print("Shop created")
        return shopObj
    else:
        print("Empty room created") 
        
        
class RoomClass:
    def __init__(self, typeNum):
        self.roomType = int(typeNum)
        
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
    print(len(room_type))
    g = 0
    while g < roomAmount:
        room_type[g] = random.randrange(0,11)
        g += 1

    print(room_type)
    i = 0
    for n in room_type:
        roomObj = createRoom(int(n))
        room_list[i] = roomObj
    roomWindow = Tk()
    r = 0
    while r < roomAmount:
        thisRoom = room_list[r]
        print("This room is type ",room_type[r])

        if int(room_type[r]) in range(0, 5):
            print("This room is Boss!")
            roomWindow.geometry("500x500")
            canvasWin = Canvas(roomWindow, width = 500, height = 500, bg = "black")
            bWin = Button(canvasWin, text = "Next", command = testButton)
            bWin.place(x = 250, y = 250)
            canvasWin.pack()
            roomWindow.mainloop()
        elif int(room_type[r]) in range(6, 8):
            print("This room is treasure!")
            roomWindow.geometry("500x500")
            canvasWin = Canvas(roomWindow, width = 500, height = 500, bg = "black")
            bWin = Button(canvasWin, text = "Next", command = testButton)
            bWin.place(x = 250, y = 250)
            canvasWin.pack()
            roomWindow.mainloop()
        elif int(room_type[r]) in range(9, 10):
            print("This room is shop!")
            roomWindow.geometry("500x500")
            canvasWin = Canvas(roomWindow, width = 500, height = 500, bg = "black")
            bWin = Button(canvasWin, text = "Next", command = testButton)
            bWin.place(x = 250, y = 250)
            print("This room is shop!")
            canvasWin.pack()
        else:
            print("This room is empty!")
            roomWindow.geometry("500x500")
            canvasWin = Canvas(roomWindow, width = 500, height = 500, bg = "black")
            bWin = Button(canvasWin, text = "Next", command = testButton)
            bWin.place(x = 250, y = 250)
            print("This room is empty!")
            canvasWin.pack()
            roomWindow.mainloop()
        r += 1
    
def testButton():
    print("This is a test. Stop here pls!")

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













