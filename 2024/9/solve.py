from tqdm import trange

with open('input.txt') as inp:
    data = inp.read()

def format_str(sequence):
    out = []
    for idx, char in enumerate(sequence):
        if not (idx % 2):
            for i in range(int(char)):
                out.append(idx//2)
        else:
            for i in range(int(char)):
                out.append(-1)
    return out

disk = list(format_str(data))

for i in trange(len(disk) - 1, 0, -1):
    if disk[i] != -1:
        if disk.index(-1) < i:
            disk[disk.index(-1)], disk[i] = disk[i], disk[disk.index(-1)]
        else:
            break
        
final_lst = [val for val in disk[:disk.index(-1)]]

checksum = 0
for idx, num in enumerate(final_lst):
    checksum += idx * int(num)

print(checksum)

### Part 2

def find_sublist_idx(main_list, sublist):
    n = len(sublist)
    for i in range(len(main_list) - n + 1):
        if main_list[i:i + n] == sublist:
            return i
    return -1

disk = format_str(data)

for i in trange(max(disk), 0, -1):
    chunk_sz = len(disk) - disk[::-1].index(i) - disk.index(i)
    chunk_start = disk.index(i)
    free_start = find_sublist_idx(disk, [-1 for _ in range(chunk_sz)])
    if free_start > -1 and free_start < chunk_start:
        for i in range(chunk_sz):
            disk[chunk_start + i], disk[free_start + i] = disk[free_start + i], disk[chunk_start + i]

for i in range(len(disk)):
    if disk[i] == -1:
        disk[i] = 0

checksum = 0
for idx, num in enumerate(disk):
    checksum += idx * int(num)
print(checksum)
