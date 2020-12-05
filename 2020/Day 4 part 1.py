

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
for document in documents:
    valids += all(field in document for field in required_fields)
    
print (valids)
