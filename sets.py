thisset = {"Apple","Banana","Cherry"}
print(thisset)

thisset2 = {"Apple","Banana","Cherry","Apple"}
print(thisset2)

thisset3 = {"Apple","Banana","Cherry",True,1,2}
print(thisset3)

print(len(thisset3))
print(type(thisset3))

thisset4 = set(("Apple","Cherry"))
print(thisset4)

for x in thisset:
    print(x)
print("Apple" in thisset)

thisset.add("Pakistan")
print(thisset)

thisset41 = {"A","B","C"}
thisset.update(thisset41)
print(thisset)

myList = ["Kiwi","GreenApple"]
thisset41.update(myList)
print(thisset41)

thisset41.remove("A")
print(thisset41)