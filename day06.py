def find_unique_block(message, length):
    seen_codes = []
    for index, code in enumerate(message):
        seen_codes = seen_codes[-(length - 1):] + [code]
        if len(set(seen_codes)) == length:
            return index + 1
    return -1


data = open("day06.txt").read()
print(f"Start of packet is at {find_unique_block(data, 4)}, start of message at {find_unique_block(data, 14)}")
