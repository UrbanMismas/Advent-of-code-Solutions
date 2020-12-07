

f = open("2020/Day 3.txt","r")
x = 0
trees = 0
for line in f:
    line = line.rstrip()
    x = x % len(line)
    if line[x] == "#":
        trees = trees + 1
    x = x + 3

print(trees)
