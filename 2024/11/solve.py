from math import log10
from functools import cache

with open('input.txt') as inp:
    data = inp.read()

nums = [int(x) for x in data.split(" ")]

@cache
def count_after_blinks(val, blinks):
    if blinks == 0: # no blinks left, doesn't matter what val is, only matters that it's a single number
        return 1
    if val == 0: 
        return count_after_blinks(1, blinks - 1)
    length = (int(log10(val)) + 1)
    if not (length % 2):
        return count_after_blinks(val // (10 ** (length//2)), blinks - 1) + count_after_blinks(val % (10 ** (length//2)), blinks - 1)
    return count_after_blinks(val * 2024, blinks - 1)

total_25 = 0
total_75 = 0

for num in nums:
    total_25 += count_after_blinks(num, 25)
    total_75 += count_after_blinks(num, 75)

print(total_25)
print(total_75)
