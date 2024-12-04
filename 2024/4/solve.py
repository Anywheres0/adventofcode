
with open('input.txt') as inp:
    data = inp.read()

### Part 1

#Making arrays for the strings in all the different directions along the matrix + backwards versions suffixed with _bk 
horizontal = data.splitlines()
horizontal_bk = [i[::-1] for i in horizontal]

vert = ["".join(line[i] for line in horizontal) for i in range(len(horizontal[0]))]
vert_bk = [i[::-1] for i in vert]

diag = ['' for i in range(len(horizontal) + len(horizontal[0]) - 1)]
for row in range(len(horizontal)):
    for col in range(len(horizontal[0])):
        diag[row + col] += horizontal[row][col]
diag_bk = [i[::-1] for i in diag]

diag_tr = ['' for i in range(len(horizontal_bk) + len(horizontal_bk[0]) - 1)]
for row in range(len(horizontal_bk)):
    for col in range(len(horizontal_bk[0])):
        diag_tr[row + col] += horizontal_bk[row][col]
diag_tr_bk = [i[::-1] for i in diag_tr]

total = 0

to_go_through = [horizontal, horizontal_bk, vert, vert_bk, diag, diag_bk, diag_tr, diag_tr_bk]

for l in to_go_through:
    for string in l:
        total += string.count("XMAS")

print(total)

#################################

### Part 2

#returns list of all indices in a string with the given substring
def get_indices(string, substr):
    indices = []
    start = 0
    while True:
        start = string.find(substr, start)
        if start == -1:
            break
        indices.append(start)
        start += 1
    return indices

SIZE = len(horizontal[0])

#converting the number of the diagonal and the index within the diagonal back to a rectangular value
#using very cursed multiplying by booleans to detect if it's past the 'mid-way point' of the diagonals bcs i'm too lazy to use actual if statements and came up with this at 1am
def get_rect_loc(size, count, idx):
    return (count < size) * count + (count >= size) * (((count % size) + 2) * size - 1) + (idx * (size - 1))

#same idea, but even more cursed because now the diagonals go the other way 
def get_rect_loc_opp(size, count, idx):
    return (count < size) * (size - count - 1) + (count >= size) * ((count % size) + 1) * size + (idx * (size + 1))

#getting all "A"'s in the diag list which have SAM or MAS around them
locs_diag = []
for count, lane in enumerate(diag):
    indices = get_indices(lane, "MAS") + get_indices(lane, "SAM")
    indices = [i+1 for i in indices]
    for idx in indices:
        locs_diag.append(get_rect_loc(SIZE, count, idx)) #makes sure values are in rectangular form

#same thing but with diag_tr
locs_diag_tr = []
for count, lane in enumerate(diag_tr):
    indices_tr = get_indices(lane, "MAS") + get_indices(lane, "SAM")
    indices_tr = [i+1 for i in indices_tr]
    for idx in indices_tr:
        locs_diag_tr.append(get_rect_loc_opp(SIZE, count, idx)) 

# ampersand does intersection on sets, seeing which points are in both of the sets (if they are in both then it will be a cross due to the lists originally representing perpendicular directions
print(len(set(locs_diag) & set(locs_diag_tr)))
