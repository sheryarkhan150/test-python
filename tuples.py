thistuple = ("Sheri","Ali","Khan")
print(thistuple)

thistuple2 = ("Sheri","Ali","Khan","Sheri","Ali")
print(thistuple2)

print(len(thistuple2))

thistuple3 = ("Sheri",)
print(type(thistuple3))

thistuple4 = tuple(("Sheri","Ali","Khan"))
print(thistuple4)

"""print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])


y = list(thistuple)
y[0] = "Sheryar"
thistuple = tuple(y)
print(thistuple)
"""
y1 = list(thistuple)
y1.append("Shery")
thistuple = tuple(y1)
print(thistuple)

y2 = ("Sheryar Khan",)
thistuple += y2
print(thistuple)


y3 = list(thistuple)
y3.remove("Ali")
thistuple = tuple(y3)
print(thistuple)

del thistuple
#print(thistuple)

fruits = ("Apple","Banana","Cherry")
(green,yellow,red) = fruits
print(green,yellow,red)

for x in thistuple2:
    print(x)

for i in range(len(thistuple2)):
    print(thistuple2[i])

i = 0
while i < len(thistuple3):
    print(thistuple3[i])
    i = i + 1


#Join Tuples

tuple1 = (1,5,6)
tuple2 = ("Ali","Sheri","Khan")

tuple3 = tuple1 + tuple2
print(tuple3)

fruits2 = ("Apple", "Strawberry")
mytuple = fruits2 * 2
print(mytuple)

#Tuples Methods
x1 = mytuple.count("Apple")
print(x1)

x2 = mytuple.index("Strawberry")
print(x2)