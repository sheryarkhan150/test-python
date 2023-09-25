thisset = {"Sheri","Ali","Khan"}
for x in thisset:
    print(x)


set1 = {"a","b"}
set2 = {1,2,3}
set3= set1.union(set2)
print(set3)

set4 = {10,12}
set1.update(set4)
print(set1)

x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}
x.intersection_update(y)

print(x)

x1 = {"apple","banana","cherry"}
y1 = {"google","microsoft","apple"}
x1.intersection_update(y1)
print(x1)

x.symmetric_difference(y)
print(x)

x.symmetric_difference(y)
print(x)

x2 = {"s","a","b","c"}
x2.add("orange")
print(x2)