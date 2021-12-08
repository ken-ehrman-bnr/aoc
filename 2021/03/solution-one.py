# Advent of Code 
# Day 3 / Puzzle 1

def data_reader(file_name):
    for row in open(file_name, 'r'):
        yield(row.strip())

data = data_reader('./input.txt')
count = 0
scores = []

for byte in data:
    count += 1
    for i in range(0, len(byte)):
        try:
            scores[i] += int(byte[i])
        except:
            scores.append(int(byte[i]))

most_common_bits = ''.join('1' if i >= int(count / 2) else '0' for i in scores)

gamma = int(most_common_bits, 2)
epsilon = int(most_common_bits, 2) ^ (2**len(most_common_bits)-1)

print(scores)
print(most_common_bits)
print(gamma, epsilon, gamma * epsilon)        
