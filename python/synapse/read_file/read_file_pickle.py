import pickle

map = {"Date" : { "schedule" : "hi",
                  "goal" : "hey" }
      }

file = open("read_file_2.txt", "wb")

# add to map to file
pickle.dump(map, file)
file.close()

# read data from file
with open("read_file_2.txt", "rb") as rFile:
    data = rFile.read()

# try/except incase file is empty
try:
    # load information read from file
    d = pickle.loads(data)

    # does not add to file
    # adds to copy of dictionary from file
    map = d
    map["Lunch"] = "food"

    # getters using accessors
    print(d)
    print(d['Date'])
    print(d['Lunch'])
    print(d['Date']['schedule'])
    print(d['Date']['goal'])

except EOFError:
    print("File empty")