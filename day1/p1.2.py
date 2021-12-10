def sonar_sweep2(file):

    numbers = open(file).read().splitlines()
    numbers = [int(x) for x in numbers]

    counter = 0

    for i in range(1, len(numbers)):
        if i+1 == len(numbers) or i+2 == len(numbers):
            print(counter)
            break
        previous = numbers[i - 1] + numbers[i] + numbers[i + 1]
        current = numbers[i] + numbers[i + 1] + numbers[i + 2]
        
        if current > previous:
            counter += 1


