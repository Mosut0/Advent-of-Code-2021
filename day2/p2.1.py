def dive(file):
    directions = numbers = open(file).read().splitlines()

    horizontal = 0
    depth = 0
    for i in directions:
        instruction = i.split(" ")
        if instruction[0] == "forward":
            horizontal += int(instruction[1])
            continue
        elif instruction[0] == "down":
            depth += int(instruction[1])
            continue
        else:
            depth -= int(instruction[1])

    return horizontal * depth
