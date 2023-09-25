thisdict = {
    "brand": "Suzuki",
    "model": "Cultus",
    "year": 2014
}
print(thisdict)

print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))


thisdict2 = dict(name = "Sheri",age = 26, country = "Pakistan")
print(thisdict2)

x = thisdict["model"]
print(x)
x1 = thisdict.get("model")
print(x1)

x3 = thisdict.keys()
print(x3)
thisdict["color"] = "white"
print(x3)

x3 = thisdict.values()
print(x3)
thisdict["year"] = 2020
print(x3)

thisdict["year"] = 2021
print(thisdict)
thisdict.update({"year":2024})
print(thisdict)

thisdict.pop("model")
print(thisdict)

mydict = thisdict.copy()
print(mydict)

mydict2 = dict(thisdict2)
print(mydict2)

"""myfamily = {
    "child1" : {
        "name" : "Sheri",
        "year" : 1996
    },
    "child2" :{
        "name" : "Muaaz"
        "year" : 1992
    }
}
"""
child1 = {
        "name" : "Ali",
        "year" : 1990
}
child2 = {
        "name" : "Khan",
        "year" : 1988
}

myfamily2 = {
    "child1" : child1,
    "child2" : child2
}

print(myfamily2["child2"]["name"])