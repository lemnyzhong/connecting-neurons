# main function
from logIn import *

print("Please create an account")
createAcc(input("Please enter an ID number: "), input("Please enter a password: "))

print()
print("Please log in...")
logIn(input("Please enter your ID number: "), input("Please enter your password: "))
