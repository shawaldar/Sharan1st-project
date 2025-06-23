try:
    x=int(input('please enter a number'))
    print(x)
except ValueError:
    print('enter a valid number....')
except NameError:
    print('x is invalid')
try:
    y=[10,20,30]
    print(y[0])
    print(y[1])
    print(y[2])
    print(y[3])
except IndexError:
    print('you are accessing wrong position')
