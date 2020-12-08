
f = open("2020/Day 8.txt","r")

lines = f.readlines()
index = 0
value = 0
previous_commands = set()

while index < len(lines):
    if index in previous_commands:
        break

    previous_commands.add(index)
    command = lines[index].strip().split(" ")

    if command[0] == "acc":
        value += int(command[1])
    elif command[0] == "jmp": 
        index += int(command[1])
        continue
    
    index += 1

print(value)