
def slide(lines, right, down=1):
    x = 0
    trees = 0

    for i in range(0, len(lines), down):
        line = lines[i].rstrip()
        x = x % len(line)
        if line[x] == "#":
            trees = trees + 1
        x = x + right
    
    return trees

f = open("Day 3.txt","r")
lines = f.readlines()

answer = slide(lines, 1) * slide(lines, 3) * slide(lines, 5) * slide(lines, 7) * slide(lines, 1, 2)
print("answer: {}".format(answer))
