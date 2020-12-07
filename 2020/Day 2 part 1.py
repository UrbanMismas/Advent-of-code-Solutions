

f = open("2020/Day 2.txt","r")
paswords = []


for x in f:
    y = x.split()
    pasword = y[2]
    character = y[1].removesuffix(":")
    rule = y[0].split("-")
    paswords.append({"min": int(rule[0]), "max": int(rule[1]), "character": character, "password": pasword})

corrrect = 0

for x in paswords:
    num = x["password"].count(x["character"])
    if x["min"] <= num <= x["max"]:
        corrrect = corrrect + 1

print(corrrect)
