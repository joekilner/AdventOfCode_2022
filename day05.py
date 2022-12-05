data = open("day05.txt").read().splitlines()


def parse_stacks(data, index_line):
    stacks = [[] for x in data[index_line].split()]
    for line in reversed(data[:index_line]):
        for index, stack in enumerate(stacks):
            crate_index = (index * 4) + 1
            if crate_index < len(line) and line[crate_index].strip():
                stack.append(line[crate_index])
    return stacks


index_line = 0
for line_index, line in enumerate(data):
    if line.strip()[0] != "[":
        index_line = line_index
        break

stacks = parse_stacks(data, index_line)

for line in data[index_line + 2:]:
    count, source, destination = map(int, line.split()[1::2])
    for i in range(count):
        stacks[destination - 1].append(stacks[source - 1].pop())
print(f"If you have a CrateMover 9000 the top blocks are {''.join([x[-1] for x in stacks])}")

stacks = parse_stacks(data, index_line)

print([x for x in map(len, stacks)])
for line in data[index_line + 2:]:
    count, source, destination = map(int, line.split()[1::2])
    original = stacks[source - 1]
    stacks[source - 1] = original[:-count]
    stacks[destination - 1] += original[-count:]
print(f"If you have a CrateMover 9001 the top blocks are {''.join([x[-1] for x in stacks if len(x)])}")
