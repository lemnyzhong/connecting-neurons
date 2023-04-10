import pickle

list_of_foos = []

class Foo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printX(self):
        print(self.x)

    def printMe(self):
        print(f'{self}')

def create():
    with open('pickled_ob.pkl', 'wb') as f:
        pickle.dump(list_of_foos, f)

def read():
    try:
        with open('pickled_ob.pkl', 'rb') as f:
            z = pickle.load(f)
            for i in z:
                print(f'{i}\n')
                i.printX()
                print()
    except:
        print('No files')

def load():
    with open('pickled_ob.pkl', 'rb') as f:
        for i in pickle.load(f):
            list_of_foos.append(i)

# list_of_foos.append(Foo(1000, 1000))
# create()

load()
for i in list_of_foos:
  i.printMe()

print(list_of_foos[3].x)
print(list_of_foos[3].y)
print(list_of_foos[0].x)
print(list_of_foos[0].y)


# list_of_foos.append(Foo(88, 88))
# list_of_foos.append(Foo(-3, -3))
# create()

