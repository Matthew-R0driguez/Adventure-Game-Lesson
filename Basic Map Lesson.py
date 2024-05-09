
## Define a map and let the player move around it
#Define our map: 1 = wall, 0 = path
#0,0 is the top left of the map, therefore...
#moving up decreases the y location and
#moving left decreases the x location and vice versa

Map = [
[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
[ 1, 0, 1, 1, 1, 0, 0, 0, 1, 2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1 ],
[ 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1  ],
[ 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1  ],
[ 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1  ],
[ 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1  ],
[ 1, 1, 0, 0, 0, 0, 0, 3, 0, 4, 0, 0, 3, 0, 0, 0, 0, 1, 1, 1  ],
[ 1, 1, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1  ],
[ 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1  ],
[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  ]
                                           ]


#Define a function to print our Map and current Player location

def drawMap(currX, currY):
    #print ("map size is : ", len(Map), " rows by ", len(Map[0]), " columns")
    print()
    for y in range (0, len(Map)):
        for x in range (0,len(Map[y])):
            if (currX == x) and (currY == y):   #print * if they are in this square
                print("🐵 ", end="")
            else:
                print (Map[y][x]," ", end ="") 
        print()
    print()

#Define our function that will move the player
#The function will first check if the player can move or hits a wall
#If the player can move, then the current location will be updated
##If the player cannot move due to a wall, the location will not be updated
def Usekey(x, y, key, Map):
    answer = input("do you want to use your keycard on this door? you only have one. ")
    if answer == "Yes":
        print("You unlocked the lab")
        key = key -1
        Map[y][x] = 0
        return (key)
    elif answer == "No":
        return(keycard)
    
    
def movePlayer(x,y,moveDir):
    global keynum

    if moveDir == "w": 
        if Map[y-1][x] == 3:
            if keynum > 0:
                keynum = Usekey(x, y-1, keynum, Map)
                return(x, y)
            else:
                print("you dont have the keycard")
                return(x, y)
        if Map[y-1][x] == 0:
            return (x, y-1)
                                 

    if moveDir == "s":
        if Map[y+1][x] == 3:
            if keynum > 0:
                answer = input("would you like to use 1 of yours keys? Y/N: ")
                keynum = Usekey(x, y+1, keynum, Map)
            else:
                    print("you dont have the keycard")
                    return(x, y)
        if Map[y+1][x] == 0:
            return (x, y+1)
        if Map[y+1][x] == 2:
            print("you have found a keycard")
            keynum=keynum+1
            return (x, y+1)
        if Map[y+1][x] == 4 and passwordcolected=True:
            print("you have found a loked box find the combination")
            return (x, y+1)

    if moveDir == "a":
        if Map[y][x-1] == 3:
            if keynum >0:
                Usekey(x-1, y, keynum, Map)
            else:
                print("you dont have the keycard")
                return(x, y)
        if Map[y][x-1] == 0:
            return (x-1, y)

    if moveDir == "d":
        if Map[y][x+1] == 3:
            if keynum > 0:
                keynum = Usekey(x+1, y, keynum, Map)
            else:
                print("you dont have the keycard")
                return(x, y)

        if Map[y][x+1] == 0:
            return (x+1, y)

        
       
        
    #they attempted a bad move
    print ("**Invalid move** Try again.")
    return (x,y)   #return the same location they are in since no move



#Set our starting location
currX = 1
currY = 1 

#draw the map the first time before asking for a move
drawMap(currX, currY)

#Forever just let the player move around the map on the path
keynum = 0

while True:
    moveDir = input("Enter direction (w,a,s,d): ")
    currX, currY = movePlayer(currX, currY, moveDir)
    drawMap(currX, currY)
    print("you have", keynum,"keycards")

