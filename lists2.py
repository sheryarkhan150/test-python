thislist = ["Apple","Banana", "Cherry"]
thislist.remove("Banana")
print(thislist)

thislist2 = ["Apple","Banana", "Cherry","Apple","Banana", "Cherry"]
thislist2.remove("Apple")
print(thislist2)

thislist2.pop(1)
print(thislist2)
print("\n")

for x in thislist2:
    print(x)
print("\n")

for i in range(len(thislist2)):
    print(thislist2[i])