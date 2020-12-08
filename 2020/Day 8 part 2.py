def loop(lines, index = 0, value = 0, previous_commands = set(), switch_free = True, step=0):
    print("value: {}".format(value))
    print("index: {}".format(index))
    print("step: {}".format(step))
    print("")

    if not (-1 < index < len(lines)):
        return value 

    if index in previous_commands:
        return None

    previous_commands.add(index)
    command = lines[index].strip().split(" ")

    step += 1

    if command[0] == "acc":
        return loop(lines, index + 1, value + int(command[1]), previous_commands, switch_free, step)

    elif command[0] == "jmp": 

        result = loop(lines, index + int(command[1]), value, previous_commands, switch_free, step)

        if result == None and switch_free == True:
            return loop(lines, index + 1, value, previous_commands, False, step)

        return result
        
    else:

        result = loop(lines, index + 1, value, previous_commands, switch_free, step)

        if result == None and switch_free == True:
            return loop(lines, index + int(command[1]), value, previous_commands, False, step)
            
        return result



f = open("2020/Day 8.txt","r")
lines = f.readlines()

print(loop(lines))