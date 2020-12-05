

f = open("Day 1.txt","r")
numbers = []

for x in f:
    numbers.append(int(x))

for x in range(len(numbers)-1):
    for y in range(x+1, len(numbers)):
        if (numbers[x] + numbers[y]) == 2020:
            print("x: {}".format(x))
            print("value: {}".format(numbers[x]))
            print("y: {}".format(y))
            print("value: {}".format(numbers[y]))
            print("answer: {}".format(numbers[x]*numbers[y]))
