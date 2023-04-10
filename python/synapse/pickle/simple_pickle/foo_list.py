import pickle

list_of_foos = []

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

def clear_all():
    list_of_foos.clear()