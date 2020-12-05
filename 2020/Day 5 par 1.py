
f = open("2020/Day 5.txt","r")

sitIDs = []

for line in f:
    binaryID = line.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0")
    ID = int(binaryID, 2)
    sitIDs.append(ID)

print(max(sitIDs))
