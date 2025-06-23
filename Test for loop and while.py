guess = 3
num= int (input("Enter a number between 1,9"))
for i in range (1,4):
    if(num==guess):
        print("you won the game")
        break
    else:
        print ("Wrong guess. Giving you another chance:")
        num=int(input("Enter a number between 1,9"))

