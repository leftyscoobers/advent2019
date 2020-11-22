# Test case 1:
t1w1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
t1w2 = "U62,R66,U55,R34,D71,R55,D58,R83"
test1a_solution = 159
test1b_solution = 610

# Test case 2:
t2w1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
t2w2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
test2a_solution = 135
test2b_solution = 410

"""
-- For a given wire, calculate the list of coordinates, counting the starting point as 0,0
-- From the two wires' paths, look for intersections
-- Calculate the Manhattan distance for each intersection
-- Return the shortest distance
"""

import numpy as np


# So ugly....
def walk_to_next_point(start_coord, instruction_string):
    direction = instruction_string[0]
    steps = int(instruction_string[1:])
    new_path_points = [start_coord] * steps
    if direction == 'U':
        new_path_points = [[coord[0], coord[1] + s] for coord, s in
                           zip(list.copy(new_path_points), np.arange(1, steps + 1))]
    if direction == 'D':
        new_path_points = [[coord[0], coord[1] - s] for coord, s in
                           zip(list.copy(new_path_points), np.arange(1, steps + 1))]
    if direction == 'R':
        new_path_points = [[coord[0] + s, coord[1]] for coord, s in
                           zip(list.copy(new_path_points), np.arange(1, steps + 1))]
    if direction == 'L':
        new_path_points = [[coord[0] - s, coord[1]] for coord, s in
                           zip(list.copy(new_path_points), np.arange(1, steps + 1))]
    return new_path_points


def get_path(wire_string):
    parse_directions = wire_string.strip().split(',')
    path_coords = [[0, 0]]
    for dir in parse_directions:
        start_point = list.copy(path_coords[-1])
        new_points = walk_to_next_point(start_point, dir)
        path_coords = list.copy(path_coords) + new_points
    return path_coords


def coords_to_strings(coord_list):
    return [f'{coord[0]}_{coord[1]}' for coord in coord_list]


def strings_to_coords(string_list):
    def parse_coord(coord_string):
        x, y = coord_string.split('_')
        return [int(x), int(y)]

    return [parse_coord(xy) for xy in string_list]


def find_intersections(path1, path2):
    intersection_strings = list(set(coords_to_strings(path1)) & set(coords_to_strings(path2)))
    intersection_points = strings_to_coords(intersection_strings)
    return intersection_points


def get_manhattan(point1, point2):
    x_dist = abs(point1[0] - point2[0])
    y_dist = abs(point1[1] - point2[1])
    return x_dist + y_dist


# Problem 1:
with open('input03.txt') as p3:
    wire_directions = p3.readlines()
p3.close()

path1 = get_path(wire_directions[0])
path2 = get_path(wire_directions[1])
inter_of_wires = find_intersections(path1, path2)
distances = sorted([get_manhattan([0, 0], coord) for coord in inter_of_wires])
print(f'Manhattan distance of closest intersection to origin: {distances[1]}')


# Part 2
"""
-- For each intersection point (except origin), find wire length to this point for BOTH wires, 
-- Sum length for each wire for each intersection.
-- Report shortest summed distance.
"""


def len_to_point(path, intersection_coord):
    return path.index(intersection_coord)

total_lengths = []
for intersection in inter_of_wires:
    total_path = len_to_point(path1, intersection) + len_to_point(path2, intersection)
    total_lengths.append(total_path)

total_lengths.sort()
print(f'Best length(s) to intersection: {total_lengths[1]}')

# import matplotlib.pyplot as plt
#
# plt.plot([x[0] for x in path1], [x[1] for x in path1], '-')
# plt.plot([x[0] for x in path2], [x[1] for x in path2], '-')
# plt.plot([x[0] for x in inter_of_wires], [x[1] for x in inter_of_wires], 'o')
# plt.show()
