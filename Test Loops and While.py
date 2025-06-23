guess = 8
i=1
num=int(input("Enter a number between 1,9:"))
while(i<=3):
    if(num==guess):
        print("yuo won the game")
        break
    else:
        print("Wrong guess. Giving you another chance:")
        num =int(input("Enter a number:"))
    i+=1
