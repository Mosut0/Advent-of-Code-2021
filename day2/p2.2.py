def aim(file):
    directions = numbers = open(file).read().splitlines()

    horizontal = 0
    depth = 0
    aim = 0
    for i in directions:
        instruction = i.split(" ")
        if instruction[0] == "forward":
            horizontal += int(instruction[1])
            depth += aim * int(instruction[1])
        elif instruction[0] == "down":
            aim += int(instruction[1])
        else:
            aim -= int(instruction[1])

    return horizontal * depth
