with open('calories.dat', 'r') as f:
    elves = []
    elf = None
    for line in f.readlines():
        
        line = line.strip()

        if not line.isnumeric():
            if elf is not None:
                elves.append(elf)        
            elf = None
            continue

        c = int(line)
        if elf is None:
            elf = {'total': c, 'items': [c]}
        else:
            elf['total'] += c
            elf['items'].append(c)

print('total elf count:', len(elves))
ranked = sorted(elves,  key = lambda e: e['total'], reverse=True)
print('winning total by sort:', ranked[0]['total'])

top_three = 0
for i in range(3):
    top_three += ranked[i]['total']

print ('top three:', top_three)