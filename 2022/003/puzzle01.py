FILE_NAME = './puzzle01-input.dat'
total = 0
with open(FILE_NAME, 'r') as f:
    for line in f:
        line = line.strip();
        left = line[0 : int(len(line)/2)]
        right = line[int(len(line)/2) : len(line)]
        for item in left:
            if right.find(item) != -1:
                if 'a' <= item <= 'z':
                    score = (ord(item) - ord('a') + 1)
                else:
                    score = (ord(item) - ord('A') + 27)
                print(item, ' = ', score)
                total += score
                break
    print(total)