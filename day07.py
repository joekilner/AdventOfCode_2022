def parse_log(log):
    file_structure = {}
    current_folder = file_structure
    for line in data:
        if line.startswith("$"):
            command = line.split()[1:]
            if command[0] == "cd":
                if command[1] == "/":
                    current_folder = file_structure
                else:
                    current_folder = current_folder[command[1]]
        else:
            if line.startswith("dir"):
                current_folder[line.split()[1]] = {"..":current_folder}
            else:
                size, name = line.split()
                current_folder[name] = int(size)
    return file_structure

def get_folder_size(folder):
    total = 0
    for name, entry in folder.items():
        if type(entry) is int:
            total += entry
        elif name != "..":
            total += get_folder_size(entry)
    return total

def find_folders(folder, min_size, max_size):
    found_folders = []
    size = get_folder_size(folder)
    if min_size <= size <= max_size:
        found_folders.append(size)
    for name, entry in folder.items():
        if type(entry) is not int and name != "..":
            found_folders += find_folders(entry, min_size, max_size)
    return found_folders

data = open("day07.txt").read().splitlines()
file_structure = parse_log(data)
print(f"Sum of smallest file_systems is {sum(find_folders(file_structure, 0, 100000))}")

total_space = 70000000
space_required = 30000000
current_free_space = total_space - get_folder_size(file_structure)
extra_space_required = space_required - current_free_space
print(f"Smallest folder that's big enough is {min(find_folders(file_structure, extra_space_required, total_space))}")
