def find_unique_block(message, length):
    seen_codes = []
    for index, code in enumerate(message):
        seen_codes = seen_codes[-(length - 1):] + [code]
        if len(set(seen_codes)) == length:
            return index + 1
    return -1


def find_unique_block2(message, length):
    offset = ord('a')
    count = [0] * (ord('z') + 1)
    multiples = 0
    for index in range(length):
        code = ord(message[index]) - offset
        count[code] += 1
        if count[code] > 1:
            multiples += 1
    for index in range(len(message) - length):
        incoming = ord(message[index + length]) - offset
        outgoing = ord(message[index]) - offset
        count[outgoing] -= 1
        if count[outgoing] > 0:
            multiples -= 1
        count[incoming] += 1
        if count[incoming] > 1:
            multiples += 1
        if multiples == 0:
            return index + length + 1
    return -1


data = open("day06.txt").read()
print(f"Start of packet is at {find_unique_block(data, 4)}, start of message at {find_unique_block(data, 14)}")
print(f"Start of packet is at {find_unique_block2(data, 4)}, start of message at {find_unique_block2(data, 14)}")
