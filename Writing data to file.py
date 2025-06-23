try:
    f = open('d:/abc.txt','r')
    list1=f.readlines()
    print(list1)
    f.close()
except FileNotFoundError:
    print('no such file..try again')
    f.close()
except IndexError:
    print('trying to print wrong position')
    f.close()
finally:
    f.close()
