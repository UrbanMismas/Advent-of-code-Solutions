
def get_set_of_parrents(color, colors):
    parents = set()

    for parent in colors[color]["parents"]:
        if parent not in parents:
            parents = parents.union(get_set_of_parrents(parent, colors))

            
    parents = parents.union(set([color]))
    return parents


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



print(len(get_set_of_parrents("shiny gold", colors))-1)

