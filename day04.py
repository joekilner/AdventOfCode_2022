import re

data = open("day04.txt").read().splitlines()

full_overlaps, partial_overlaps = (0, 0)
for line in data:
    low_1, high_1, low_2, high_2 = map(int, re.split("[-,]", line))
    full_overlaps += 1 if (low_1 <= low_2 and high_1 >= high_2) or (low_2 <= low_1 and high_2 >= high_1) else 0
    partial_overlaps += 1 if (low_1 <= low_2 <= high_1) or (low_2 <= low_1 <= high_2) else 0

print(f"Fully overlapping work orders = {full_overlaps}, partially overlapping = {partial_overlaps}")
