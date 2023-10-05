f = open("text.txt")
"""print(f.read())
"""
f2 = open("/home/sheryar/Documents/text2.txt")
"""print(f2.read())

print(f.read(5))
print(f2.readline())
print(f2.readline())
"""
for x in f2:
    print(x)
f.close()
f2.close()
