def move_reader(file_name):
    for row in open(file_name, 'r'):
        yield {'direction': row.split()[0], 'distance': int(row.split()[1])}

horizontal = 0
depth = 0
aim = 0

for move in move_reader('input.txt'):
    if move['direction'] == 'forward':
        horizontal += move['distance']
        depth += move['distance'] * aim
    elif move['direction'] == 'up':
        aim -= move['distance']
    elif move['direction'] == 'down':
        aim += move['distance']


print('-'*80)    
print(horizontal, depth, aim, horizontal * depth)
print('-'*80)    
