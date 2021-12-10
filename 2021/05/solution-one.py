from collections import namedtuple
from bresenham import bresenham
import math

# Advent of Code 2021
# Day 05
# Problem 01

# Description:
# Given: 
#   A set of endpopairs (a, b) in set A denoting a line pt_pairment on grid G
# Problem:
#   Determine which cells on the grid are crossed by the line pt_pairments and how many times.
#   Find points which have been crossed at least two times.
#   Count these points.
# Note:
# I Will be using this ray-tracing algorithm 
# http://playtechs.blogspot.com/2007/03/raytracing-on-grid.htmlehrman

Point = namedtuple('Point', 'x y')

class Grid:
    def __init__(self, max_x, max_y) -> None:
        self.__grid = [[0]*max_y for i in range(max_x)]

    def visit(self, grid_col, grid_row) :
        self.__grid[grid_row][grid_col] += 1

    def __str__(self) -> str:
        out = ''
        for y in self.__grid:
            for x in y:
                if x == 0:
                    out += '.'
                elif x < 10:
                    out += str(x)
                else:
                    out += '9'
            out += '\n'
        return out

    def calculate_score(self, threshold) -> int:
        score = 0
        for grid_row in self.__grid:
            score += sum([1 if cell >= threshold else 0 for cell in grid_row])
        return score

    def plot_line(self, p0, p1) -> None:
        for pt in bresenham(p0.x, p0.y, p1.x, p1.y):
            self.visit(pt[0], pt[1])


    def ray_trace(self, p0, p1) -> None:
        dx = abs(p1.x - p0.x)
        dy = abs(p1.y - p0.y)
        x = p0.x
        y = p0.y
        n = 1 + dx + dy
        x_inc = 1 if (p1.x > p0.x) else -1
        y_inc = 1 if (p1.y > p0.y) else -1
        error = dx - dy
        dx *= 2
        dy *= 2

        for i in range(0, n):
            self.visit(x, y)
            if (error > 0):
                x += x_inc
                error -= dy
            else:
                y += y_inc
                error += dx

def data_reader(file_name):
    for y in open(file_name, 'r'):
        l = y.replace(' -> ', ',').split(',')
        yield([Point(int(l[0]),int(l[1])), Point(int(l[2]),int(l[3]))])

settings = {'w': 1000, 'h': 1000, 'file_name' : './input.txt', 'threshold': 2, 'diagonals': True}
#settings = {'w': 10, 'h': 10, 'file_name': './input-test.txt', 'threshold': 2, 'diagonals': True}

input = data_reader(settings['file_name'])
grid = Grid(settings['w'], settings['h'])

for pt_pair in input:
    if settings['diagonals'] or (pt_pair[0].x == pt_pair[1].x or pt_pair[0].y == pt_pair[1].y):
        grid.plot_line(pt_pair[0], pt_pair[1])

score = grid.calculate_score(settings['threshold'])
print(score)

with open('output.txt', 'w') as text_file:
    text_file.write(str(grid))