def foo(file_name):
    for row in open(file_name, 'r'):
        yield {'direction': row.split()[0], 'distance': int(row.split()[1])}

move_reader = foo('input.txt')
moves = {}

for move in move_reader:
    if move['direction'] in moves:
        moves[move['direction']] += move['distance']
    else:
        moves[move['direction']] = move['distance']

print('-'*80)    
print(moves)
print(moves['forward'] * (moves['down'] - moves['up']))
print('-'*80)    

