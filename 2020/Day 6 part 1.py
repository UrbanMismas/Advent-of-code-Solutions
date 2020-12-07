f = open("2020/Day 6.txt","r")

currentGroup = ""
total = 0
for line in f:
    line = line.rstrip()
    if line == "":
        total = total + len(set(currentGroup))
        currentGroup = ""
    else:
        currentGroup = currentGroup + line

if currentGroup != "":
    total = total + len(set(currentGroup))
    currentGroup = ""

print(total)