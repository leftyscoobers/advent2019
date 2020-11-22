"""
Steps:
1. Turn astroid map into coordinates for each asteroid.
2. Calculate the "new coordinates" for each other asteroid as if that candidate asteroid is the new center.
3. For each asteroid, collect other asteroids that match along any slope AND quadrant/axis (only one per slope-quadrant)
"""
import sys

# Test answers
# 1: 8 at 3,4
# 2: 33 at 5,8
# 3: 35 at 1,2
# 4: 41 at 6,3
# 5: 210 at 11,13

# PART 1

# Reed in the file and record coordinates (note these are 'upsidedown' -
# problem coordinates are 0,0 at upper left not lower left, which we can just fix at the end
input_txt = sys.argv[1]

asteroid_locs = []
with open(input_txt, 'r') as input:
    linect = 0
    for line in input.readlines():
        parsed = list(line.strip())
        asteroid_indices = [(i, linect) for i, x in enumerate(parsed) if x == '#']
        linect += 1
        asteroid_locs = asteroid_locs.copy() + asteroid_indices

input.close()


# Calculate new points as if candidate asteroid is the new center
def get_new_coords(candidate, all_asteroids):
    x_off = candidate[0]
    y_off = candidate[1]
    return [(asteroid[0]-x_off, asteroid[1]-y_off) for asteroid in all_asteroids]


def represent_quadrant(coord):
    x_val = coord[0]
    y_val = coord[1]
    def compare(raw_value):
        if raw_value > 0:
            return 1
        elif raw_value:
            return -1
        else:
            return 0
    return (compare(x_val), compare(y_val))


def slope_hack(coord):
    if coord[0] == 0:
        return 0
    else:
        return coord[1]/coord[0]

# Broken - doesn't account for asteroid intersects in opposite directions (only keeps one of each slope)
asteroid_intersects = []
for asteroid in asteroid_locs:
    new_coords = get_new_coords(asteroid, asteroid_locs)
    quads = [represent_quadrant(coord) for coord in new_coords]
    slopes = [slope_hack(coord) for coord in new_coords]

    quads_to_slopes = zip(quads, slopes)
    slope_matches = list(set(quads_to_slopes)) # This will include a match to the asteroid itself.

    asteroid_intersects = asteroid_intersects.copy() + [[(asteroid[0], asteroid[1]), len(slope_matches)-1]]

max_matches = max([pairs[1] for pairs in asteroid_intersects])
best_candidate = [pair[0] for pair in asteroid_intersects if pair[1] == max_matches]


print(f'Most matches: {max_matches} at {best_candidate}')

