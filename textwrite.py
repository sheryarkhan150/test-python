"""f = open("text.txt","a")
f.write("\nNow it has more content in it")
f.close()

f = open("text.txt", "r")
print(f.read())

f = open("text.txt","w")
f.write("I deleted the content!")
f.close

f = open("text.txt","r")
print(f.read())
"""
f = open("text3.txt","x")

import os
os.remove("text3.txt")

if os.path.exists("text3.txt"):
    os.remove("text3.txt")
else:
    print("The file does not exist")