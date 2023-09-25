thislist = ["Sheri", "Ali", "Khan"]
print(thislist)


thislist2 = ["Sheri", "Ali", "Khan", "Sheri", "Ali"]
print(thislist2)

print(len(thislist))
print(len(thislist2))

print(type(thislist2))

thislist3 = list(("Sheri","Ali","Khan"))
print(thislist3)

print(thislist[1])
print(thislist3[-1])
print(thislist2[2:5])
print(thislist2[:4])
print(thislist2[2:])

if "Sheri" in thislist:
    print("Yes, 'Sheri' is present in the list! ")
if "Sheryar" not in thislist:
    print("No, 'Sheri' is not present in the list! \n\n")    

thislist2[1] = ["Sheryar"]
print(thislist2)
