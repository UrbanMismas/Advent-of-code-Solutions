f = open("2020/Day 6.txt","r")

currentGroup = None
total = 0
for line in f:
    line = line.rstrip()
    if line == "":
        total = total + len(currentGroup)
        currentGroup = None
    else:
        if currentGroup == None:
            currentGroup = set(line)
        else:
            currentGroup = currentGroup & set(line)

if currentGroup != "":
    total = total + len(currentGroup)
    currentGroup = None

print(total)