def most_common(rows, digit):
    """
    Returns most common value after arranging by column
    Credit: Akaiyan Duquet
    """
    most_common_bit = 0
    for num in rows:
        most_common_bit += 2 * int(num[digit]) - 1

    return '0' if most_common_bit < 0 else '1'


def binary_diagnostic2(file):
    bits = open(file).read().splitlines()

    oxygen = []
    CO2 = []

    for i in bits:
        if i[0] == most_common(bits, 0):
            oxygen.append(i)
        else:
            CO2.append(i)

    k = 1
    while len(oxygen) > 1 or len(CO2) > 1:
        new_oxygen = []
        new_CO2 = []

        if len(oxygen) > 1:
            for i in oxygen:
                if i[k] == most_common(oxygen, k):
                    new_oxygen.append(i)
            oxygen = new_oxygen

        if len(CO2) > 1:
            for i in CO2:
                if i[k] != most_common(CO2, k):
                    new_CO2.append(i)
            CO2 = new_CO2

        k += 1

    return int(oxygen[0], 2) * int(CO2[0], 2)


print(binary_diagnostic2("data3.txt"))
