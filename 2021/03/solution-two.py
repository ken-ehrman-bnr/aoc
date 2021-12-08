# Advent of Code 
# Day 3 / Puzzle 1

# MY SOLUTION ASSUMES BINARY NUMBERS WHICH IS NOT WHAT THE REQUIREMENTS READ

def data_reader(file_name):
    for row in open(file_name, 'r'):
        yield(row.strip())

def get_sub_list(data, digit, get_most_common):
    r = sum([int(i[digit]) for i in data]) / len(data)
    if r < .5:
        test_value = 0 if get_most_common else 1
    else:
        test_value = 1 if get_most_common else 0
    return [i for i in data if int(i[digit]) == test_value]


input = list(data_reader('./input.txt'))

i = 0
o2 = get_sub_list(input, i, True)
while len(o2) > 1:
    i += 1
    o2 = get_sub_list(o2, i, True)

i = 0
co2 = get_sub_list(input, i, False)
while len(co2) > 1:
    i += 1
    co2 = get_sub_list(co2, i, False)

# wrong answer
# ['111010101100'] ['010011101100'] 4732560
print(o2, co2, int(o2[0], 2) * int(co2[0], 2))
