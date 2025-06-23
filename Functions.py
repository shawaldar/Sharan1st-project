num1=int(input("Enter 1st number"))
num2=int(input("enter 2nd number"))
choice=int(input("Enter a choice from below:/n1 addition/n2 subtraction/n3 multipication/n4 devision/n"))
def addition():
    res_sum=num1+num2
    print(res_sum)
def subtraction():
    res_subtraction=num2-num1
    print(res_subtraction)
def mult():
    res_prod=num1+num2
    print(res_prod)
def division():
    res_division=num2/num1
    print(res_division)
if (choice==1):
    addition ()
if (choice==2):
    subtraction()
if (choice==3):
    mult()
if (choice==4):
    division()
else:
    print("Wrong choice made:")


