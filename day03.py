data = open("day03.txt").read().splitlines()

lowercase_offset = ord('a') - 1
uppercase_offset = ord('A') - 1
priority_map = {}
for index in range(1, 27):
    priority_map[chr(lowercase_offset + index)] = index
    priority_map[chr(uppercase_offset + index)] = index + 26

priorities = []
for line in data:
    middle = len(line) // 2
    priorities.append(priority_map[set(line[:middle]).intersection(set(line[middle:])).pop()])

print(sum(priorities))

priorities = []
for group in zip(data[::3], data[1::3], data[2::3]):
    priorities.append(priority_map[set(group[0]).intersection(group[1]).intersection(group[2]).pop()])

print(sum(priorities))
