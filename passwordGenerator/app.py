import random

lowerCase = ("abcdefghijklmnopqrstuvwxyz")
upperCase = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
NUMBER =  "0123456789"
Symbol = "[]{}#()*;._-"

all = lowerCase + upperCase + NUMBER + Symbol
print(all)
length = 9
password = "".join(random.sample(all, length))
print(" The Password You Generated is :", password)
