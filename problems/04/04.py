input = '273025-767253'

"""
Password criteria:
-- 6 digit number in the range above.
-- Two adjacent digits are the same but... examples suggest it can be more than two of the same and
it's unclear if it can be more than one unique number that can be repeated (so '111111' is ok and '112234'?)
-- From left to right, the digits never decrease.

Goal: Find how many passwords within the range provided meet this criteria? 
"""
test_examples = ['111111', '122345', '556789', '123889']

"""
Initial thoughts
-- Could use sort to check if the digits decrease so sort(mylist) == mylist.
-- For first five digits check adjacent digits via index to see if they're the same AND only 1 match. Seems slow as hell.
"""
import numpy as np

# Part 1
def string_to_list(string_password):
    return list(string_password)


def list_to_string(list_of_digits):
    return ''.join(list_of_digits)


all_the_options = [str(p) for p in np.arange(273025, 767253)] # 494228 options
print(f'There are {len(all_the_options)} numbers in the given range.')
ascending_options = [s for s in all_the_options if ((list_to_string(sorted(string_to_list(s))) == s) and (len(list(set(string_to_list(s)))) < 6))]
print(f'{len(ascending_options)} are ascending and contain a duplicate.') # 910


# Part 2
"""
New rule is that there has to be at least one pair of doubles but that pair is ONLY a pair
-- 112233 good
-- 123444 bad
-- 111122 good
"""

# Only 910 options so start with a dumb way.
def count_digits(digit_list):

    def count_single_digit(digit_list, digit):
        return len([d for d in digit_list if d == digit])

    unique_digits = list(set(digit_list))
    counts = [count_single_digit(digit_list, d) for d in unique_digits]
    return counts

new_candidates = []
for p in ascending_options:
    plist = string_to_list(p)
    counts = count_digits(plist)
    if 2 in counts:
        new_candidates.append(p)

print(f'Part 2 candidates: {len(new_candidates)}')