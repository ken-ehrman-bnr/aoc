# Advent of Code
# Day 4 / Solution One
# Bingo

# let's grok the input

def data_reader(file_name):
    for row in open(file_name, 'r'):
        yield row

input = list(data_reader('./input.txt'))        
