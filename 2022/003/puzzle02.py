#FILE_NAME = './puzzle02-input.test.dat'
FILE_NAME = './puzzle01-input.dat'

def get_badge(a, b, c) :
    for item in a:
        if b.find(item) >=0 and c.find(item) >= 0:
            return item

def get_priority(item):
    if 'a' <= item <= 'z':
        return (ord(item) - ord('a') + 1)
    elif 'A' <= item <= 'Z':
        return (ord(item) - ord('A') + 27)
    else:
        raise Exception("dude, wtf?")


total = 0
obj = open(FILE_NAME, 'r')
dat = obj.readlines()

for i in range(0, len(dat), 3):
    badge = get_badge(dat[i], dat[i + 1], dat[i + 2])
    total += get_priority(badge)
    print('badge:', badge, ' total:', total)
    


