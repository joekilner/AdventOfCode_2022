data = open("day03.txt").read().splitlines()

priorities = []
for line in data:
    middle = len(line) // 2
    priorities.append((ord(set(line[:middle]).intersection(set(line[middle:])).pop()) - 96) % 58)
print(sum(priorities))

priorities = []
for group in zip(data[::3], data[1::3], data[2::3]):
    priorities.append((ord(set(group[0]).intersection(group[1]).intersection(group[2]).pop()) - 96) % 58)
print(sum(priorities))
