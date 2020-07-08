Board={
    1: " ",2:" ",3: " ",
    4: " ",5:" ",6: " ",
    7: " ",8:" ",9: " "

}
player=1
playerOne=input("Enter the first player name: ")
playerTwo=input("Enter the second player name: ")



totalMoves=0
End=0
def GameOver():
    # Horizontal Conditions for player one
    if  ( Board[1]=="x" and Board[2]=="x" and Board[3]=="x" ) or (Board[4]=="x" and Board[5]=="x" and Board[6]=="x") or (Board[7]=="x" and Board[8]=="x" and Board[9]=="x"):
        print(playerOne," has won")
        End=1
        return End
    # Vertical condtions
    elif (Board[1]=="x" and Board[4]=="x" and Board[7]=="x") or (Board[2]=="x" and Board[5]=="x" and Board[8]=="x") or (Board[3]=="x" and Board[6]=="x" and Board[9]=="x"):
        print(playerOne," has won")
        End = 1
        return End
    #Diagonal conditions
    elif (Board[1]=="x" and Board[5]=="x" and Board[9]=="x") or (Board[3]=="x" and Board[5]=="x" and Board[7]=="x"):
        print(playerOne," has won")
        End = 1
        return End
    # Horizontal Conditions for player two

    elif ( Board[1]=="o" and Board[2]=="o" and Board[3]=="o" ) or (Board[4]=="o" and Board[5]=="o" and Board[6]=="o") or (Board[7]=="o" and Board[8]=="o" and Board[9]=="o"):
        print(playerTwo," has won")
        End=1
        return End
    # Vertical condtions
    elif (Board[1]=="o" and Board[4]=="o" and Board[7]=="o") or (Board[2]=="o" and Board[5]=="o" and Board[8]=="o") or (Board[3]=="o" and Board[6]=="o" and Board[9]=="o"):
        print(playerTwo," has won")
        End = 1
        return End
    #Diagonal conditions
    elif (Board[1]=="o" and Board[5]=="o" and Board[9]=="o") or (Board[3]=="o" and Board[5]=="o" and Board[7]=="o"):
        print(playerTwo," has won")
        End = 1
        return End
    return 0


print("............Example...............")
print("x |o |o")
print("--+--+--")
print("0 |x |0")
print("--+--+--")
print("0 |0 |x")
print("------------------------------------")

while True:

    #End=GameOver()
    if totalMoves == 9 or End==1:
        print("Game over")
        break
    print(Board[1] + " |" + Board[2] + " | " + Board[3])
    print("--+--+--")
    print(Board[4] + " |" + Board[5] + " |" + Board[6])
    print("--+--+--")
    print(Board[7] + " |" + Board[8] + " |" + Board[9])
    while True:
        if player==1:
            inputOne=int(input("First player "))
            if inputOne in Board.keys() and Board[inputOne]== " ":
                Board[inputOne]="x"
                End=GameOver()
                #print(GameOver())
                player=2
                break
            else:
                print("Wrong input")
                continue
        else:
            inputTwo = int(input("Second player:"))
            if inputTwo in Board.keys() and Board[inputTwo] == " ":
                Board[inputTwo] = "o"
                End=GameOver()
                #print(GameOver())
                player = 1
                break
            else:
                print("Wrong input")
                continue
    totalMoves+=1
    print("---------------------------------------------------------")
    print()
