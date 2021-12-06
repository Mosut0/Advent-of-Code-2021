def binary_diagnostic2(file):
    bits = open(file).read().splitlines()

    gamma = ""
    epsilon = ""
    reports = []
    for i in range(len(bits)):
        for j in range(len(bits[0])):
            if i == 0:
                reports.append(bits[i][j])
            else:
                reports[j] += bits[i][j]

    oxygen = []
    CO2 = []
    i = 0
    while i != len(bits[0]) - 1:
        if reports[0].count("0") > reports[i].count("1"):
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"


    return int(gamma, 2) * int(epsilon, 2)
