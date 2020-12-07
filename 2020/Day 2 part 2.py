

f = open("2020/Day 2.txt","r")
paswords = []


for x in f:
    y = x.split()
    pasword = y[2]
    character = y[1].removesuffix(":")
    rule = y[0].split("-")
    paswords.append({"first": int(rule[0]), "second": int(rule[1]), "character": character, "password": pasword})

corrrect = 0

for x in paswords:
    pasword = x["password"]
    first = x["first"]-1
    second = x["second"]-1
    character = x["character"]
    if (pasword[first] == character and pasword[second] != character) or (pasword[first] != character and pasword[second] == character):
        corrrect = corrrect + 1

print(corrrect)