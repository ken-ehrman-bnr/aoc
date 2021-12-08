import functools

data_file = open("./input.txt", "r")
items = data_file.readlines()
increase_count = 0
for i in range(1,len(items)):
    if int(items[i]) > int(items[i-1]):
        increase_count += 1
    
print(increase_count)
