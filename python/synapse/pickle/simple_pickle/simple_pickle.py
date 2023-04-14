from foo_list import *

class Foo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printX(self):
        print(self.x)

    def printMe(self):
        print(f'{self}')

ans = input('\nchoose\n')
load()
while ans != 'q':
    match ans:
        case 'append':
            x_ans = input('x:\n')
            y_ans = input('y:\n')

            list_of_foos.append(Foo(x_ans, y_ans))
            
            ans = input('\nchoose\n')
        
        case 'create':
            create()

            ans = input('\nchoose\n')

        case 'list':
            for i in list_of_foos:
                print(i)
            
            ans = input('\nchoose\n')

        case 'clear':
            clear_all()

            ans = input('\nchoose\n')

        case 'clear saved':
            clear_all()
            create()

            ans = input('\nchoose\n')
            
        case other:
            ans = input('\nchoose\n')
