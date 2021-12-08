
data_file = open("./input.txt", "r")

counter = 0
items = list(map(lambda x: int(x), data_file.readlines()))
for i in range(0,len(items)-1):
    if items[i] < items[i+1]:
        counter += 1

print('increases: ', counter)

counter = 0
for i in range(0, len(items)-1):
    if sum(items[i:i+3]) < sum(items[i+1:i+4]):
        counter += 1

print('increases: ', counter)
