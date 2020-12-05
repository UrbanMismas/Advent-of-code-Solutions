f = open("2020/Day 5.txt","r")

sitIDs = []

for line in f:
    binaryID = line.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0")
    ID = int(binaryID, 2)
    sitIDs.append(ID)

sitIDs.sort()

lastID = ""
myID = 0

for ID in sitIDs:
    if lastID != "" and abs(lastID - ID) == 2:
        myID = int((lastID + ID) / 2)
        break

    lastID = ID

print(myID)