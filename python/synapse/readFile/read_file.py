import ast

map = {"Date" : { "schedule" : "hi",
                  "goal" : "hey" }
      }
# Create File and Writing
# create file name and open file
# "w+" and "a+" creates file if no file is found
file_name = 'read_in_file.txt'
# f = open(file_name, "w+")

# # write has to be type string
# f.write(str(map))
# f.close()

# Reading
# open file, in read mode, "r+" allows to update as well
f = open(file_name, "r+")
s = f.read()

# try and except for Syntax error
# this checks if file_name is empty or not
try:
    # using ast import, literal.eval
    # to convert s as str to type
    # ast == abstract syntax tree
    d = ast.literal_eval(s)
    
    # adding keys to map 
    # CORRECTION: This does not add to map, but a copy of map aka d
    d['Lunch'] = {'food' : 'Burger'}
    print(d)
    print(d['Lunch']['food'])
    
except SyntaxError:
    print("Empty file")      # if empty print empty file