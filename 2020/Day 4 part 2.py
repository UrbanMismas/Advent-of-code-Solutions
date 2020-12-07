import string
f = open("2020/Day 4.txt","r")

documents = [{}]
index= 0


for line in f:
    line = line.rstrip()
    if line == "":
        index = index + 1
        documents.append({})
    else:
        line = line.split()
        for element in line:
            element = element.split(":")
            documents[index][element[0]] = element[1]

valids = 0
required_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
fails = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

for document in documents:
    valid = True
    for field in required_fields:
        if field not in document.keys():
            valid = False
            break
    
    if valid == False:
        fails[0]+=1
        continue

    if not 1920 <= int(document["byr"]) <= 2002:
        fails[1]+=1
        continue

    if not 2010 <= int(document["iyr"]) <= 2020:
        fails[2]+=1
        continue

    if not 2020 <= int(document["eyr"]) <= 2030:
        fails[3]+=1
        continue


    if document["hgt"].endswith("cm"):
        if not 150 <= int(document["hgt"].removesuffix("cm")) <= 193:
            fails[4]+=1
            continue

    elif document["hgt"].endswith("in"):
        if not 59 <= int(document["hgt"].removesuffix("in")) <= 76:
            fails[5]+=1
            continue
    
    else:
        fails[6]+=1
        continue
    
    if not (document["hcl"].startswith("#") and all(c in string.hexdigits for c in document["hcl"].removeprefix("#")) and len(document["hcl"]) == 7):
        fails[7]+=1
        continue

    if document["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        fails[8]+=1
        continue

    if len(document["pid"]) != 9:
        fails[9]+=1
        continue
    
    valids = valids + 1

print (valids)
