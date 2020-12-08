
def total_children(color, colors):
    children = 0

    for unique_child in colors[color]["children"]:
        children += int(colors[color]["children"][unique_child]) * total_children(unique_child, colors)

    return 1 + children

f = open("2020/Day 7.txt","r")

colors = {}

for line in f:
    line = line.strip().split("bags contain")
    color = line[0].strip()
    
    if color not in colors.keys():
        colors[color] = {}
        colors[color]["parents"] = []
        colors[color]["children"] = {}
    
    if line[1].strip() == "no other bags.":
        continue

    children = line[1].split(",")

    for child in children:
        child = child.strip().split(" ")
        amount = child[0]
        child_color = child[1] + " " + child[2]
        colors[color]["children"][child_color] = amount

        if child_color not in colors.keys():
            colors[child_color] = {}
            colors[child_color]["parents"] = []
            colors[child_color]["children"] = {}
        colors[child_color]["parents"].append(color)


print (total_children("shiny gold", colors)-1)
