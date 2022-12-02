calories_list = sorted([sum([int(snack) for snack in elf.split()]) for elf in open("day01.txt").read().strip().split("\n\n")])
print(calories_list[-1], sum(calories_list[-3:]))
