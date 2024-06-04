#matthew rodriguez
import turtle
import random
from turtle import *

# Define a map and let the player move around it
#Define our map: 1 = wall, 0 = path
#0,0 is the top left of the map, therefore...
#moving up decreases the y location and
#moving left decreases the x location and vice versa

Map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 0, 1, 1, 1, 1, 1, 7, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 9, 0, 0, 8],
      [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
      [1, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 1, 1, 1, 0, 9, 1, 1],
      [1, 1, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 9, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 0, 0, 9, 0, 9, 1],
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
screen = Screen()
screen.title("Map Grid")
screen.bgcolor("white")
screen.setup(1100,1100)
screen.tracer(0)

ball = turtle.Turtle()
grid = turtle.Turtle()
grid.speed(0)
size = 40
grid.penup()
screenad = 200
currX = 1
currY = 1

Key = False



#Define a function to print our Map and current Player location

def drawMap(currX, currY):
    #print ("map size is : ", len(Map), " rows by ", len(Map[0]), " columns")
    print()
    for y in range (0, len(Map)):
        for x in range (0,len(Map[y])):
            if (currX == x) and (currY == y):   #print * if they are in this square
                print("*  ", end="")
            else:
                print (Map[y][x]," ", end ="")
        print()
    print()



def drawsquare(x, y, size, grid, color):
    grid.penup()
    grid.goto(x, y)
    grid.pendown()
    grid.fillcolor(color)
    grid.begin_fill()
    for square in range(4):
        grid.forward(size)
        grid.left(90)
    grid.end_fill()


def drawplayer(x, y):
    ball.penup()
    ball.goto(x,y)
    ball.shape("circle")
    ball.color("red")

def drawGrid(currX, currY, size, grid):
    for y in range (0, len(Map)):
        for x in range (0,len(Map[y])):
            c = (size* x-400)
            r = (size* -y+200)
            if (currX == x) and (currY == y):   #print * if they are in this square
                drawplayer(c+size/2, r+size/2)
                drawsquare(c, r, size, grid, "white")
            else:
                if Map[y][x] == 0:
                    drawsquare(c, r, size, grid, "white")
                elif Map[y][x] == 1:
                    drawsquare(c, r, size, grid, "black")
                elif Map[y][x] == 2:
                    drawsquare(c, r, size, grid, "gold")
                elif Map[y][x] == 3:
                    drawsquare(c, r, size, grid, "brown")
                elif Map[y][x] == 4:
                    drawsquare(c, r, size, grid, "cyan")
                elif Map[y][x] == 5:
                    drawsquare(c, r, size, grid, "grey")
                elif Map[y][x] == 6:
                    drawsquare(c, r, size, grid, "orange")
                elif Map[y][x] == 8:
                    drawsquare(c, r, size, grid, "green")
                elif Map[y][x] == 7:
                    drawsquare(c, r, size, grid, "gold")
                elif Map[y][x] == 9:
                    drawsquare(c, r, size, grid, "grey90")









#Define our function that will move the player
#The function will first check if the player can move or hits a wall
def movePlayer(x,y,moveDir):
    #assume invalid move is attempted
    badMove = True

    if moveDir == "w":
        if Map[y-1][x] == 0:
            return (x, y-1)
        if Map [y-1] [x]==4:
            print("you have found a computer")
            print("enter password to open gate, heres a hint his neighbour lives in a pinapple")
            password = "squidward"
            encrypted_password = encrypt(password)
            print("Encrypted message: ", encrypted_password)
            passwrd=input("translate")
            if passwrd==password:
                print("correct")
                return(x, y-1)
        if Map [y-1] [x]==5:
            print("a great musicians name from bakini bottoms spelled 3 letters back, a=d")
        if Map[y-1][x] == 7:
            print("sorry this key is broken find a nother one")
                    


            
    if moveDir == "s":
        if Map[y+1][x] == 0:

            return (x, y+1)
        if Map [y+1] [x]==4:
            print("you have found a computer")
            print("enter password to open gate, heres a hint his neighbour lives in a pinapple")
            password = "squidward"
            encrypted_password = encrypt(password)
            print("Encrypted message: ", encrypted_password)
            passwrd=input("translate")
            if passwrd==password:
                print("correct")
                return(x, y+1)
        if Map[y+1][x] == 2:
            return(x, y+1)

    if moveDir == "a":
        if Map[y][x-1] == 0:
            return (x-1, y)
        

    if moveDir == "d":
        if Map[y][x+1] == 0:
            return (x+1, y)
        if Key== True and Map[y][x+1] == 3:
            return (x+1, y)
        if Map[y][x+1] == 3 and Key== False:
            print ("you have to find the key first!")
        if Map [y] [x+1]==8:
            musicman=input("whos the best musician from bakini bottom")
            if musicman ==("squidward"):
                print("you win")
                exit()
            else:
                print("wrong,you lose")
                exit()
     
       
    #they attempted a bad move
    if badMove: 
        print ("**Invalid move** Try again.")
        return (x,y)   #return the same location they are in since no move


def encrypt(password):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_password = ""
    for x in password:
        if x.isalpha():
            encrypted_x = alphabet[(alphabet.index(x) + 3) % 26]
            encrypted_password += encrypted_x
    return encrypted_password

def pickupkey (x, y):
    global Key
#Select the cordinates of where you want your hidden item to be
    if Map[y][x] ==2:
        if Key == False:
            print ("You have found a key!")
            Key = True
            return (Key)
        if Key == True:
            return

#draw the map the first time before asking for a move

drawGrid(currX, currY, size, grid)

#Forever just let the player move around the map on the path
while True:
    screen.update()
    moveDir = input("Enter direction (w,a,s,d): ")
    pickupkey(currX, currY)
    currX, currY = movePlayer(currX, currY, moveDir)
    drawGrid(currX, currY, size, grid)
    drawMap(currX, currY)
