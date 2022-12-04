data = open("day03.txt").read().splitlines()

priorities = []
for line in data:
    middle = len(line) // 2
    priorities.append((ord(set(line[:middle]).intersection(set(line[middle:])).pop()) - 96) % 58)
print(sum(priorities))

print(sum([(ord(set.intersection(x).pop()) - 96) % 58 for x in map(set, zip(data[::3], data[1::3], data[2::3]))]))
