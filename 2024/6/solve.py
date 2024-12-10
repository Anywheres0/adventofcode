from tqdm import trange

with open('input.txt') as inp:
    data = inp.read()

rows = [list(line) for line in data.splitlines()]

pos = [data.replace("\n","").index("^") // len(rows[0]), data.replace("\n","").index("^") % len(rows[0])]
sym = "^"

states = ['^','>','v','<']

while True:
    if (sym == '^' and pos[0]-1 < 0) or (sym == 'v' and pos[0]+1 > len(rows) - 1) or (sym == '<' and pos[1]-1 < 0) or (sym == '>' and pos[1]+1 > len(rows[0]) - 1):
        rows[pos[0]][pos[1]] = "X"
        break
    match sym:
        case '^':
            ahead = rows[pos[0] - 1][pos[1]]
            if ahead == "#":
                sym = states[(states.index(sym) + 1) % 4]
            else:
                rows[pos[0]][pos[1]] = "X"
                pos[0] -= 1
        case '>':
            ahead = rows[pos[0]][pos[1] + 1]
            if ahead == "#":
                sym = states[(states.index(sym) + 1) % 4]
            else:
                rows[pos[0]][pos[1]] = "X"
                pos[1] += 1
        case 'v':
            ahead = rows[pos[0] + 1][pos[1]]
            if ahead == "#":
                sym = states[(states.index(sym) + 1) % 4]
            else:
                rows[pos[0]][pos[1]] = "X"
                pos[0] += 1
        case '<':
            ahead = rows[pos[0]][pos[1] - 1]
            if ahead == "#":
                sym = states[(states.index(sym) + 1) % 4]
            else:
                rows[pos[0]][pos[1]] = "X"
                pos[1] -= 1

print('\n'.join(''.join(row) for row in rows).count("X"))

### Part 2

loop_bricks = 0

for potential in trange(len(data.replace("\n",""))):    
    rows = [list(line) for line in data.splitlines()]

    pos = [data.replace("\n","").index("^") // len(rows[0]), data.replace("\n","").index("^") % len(rows[0])]
    sym = "^"

    if rows[potential // len(rows[0])][potential % len(rows[0])] == ".":
        rows[potential // len(rows[0])][potential % len(rows[0])] = "#"
        broke_bcs_repeat = False

        collisions = []

        while True:
            if (sym == '^' and pos[0]-1 < 0) or (sym == 'v' and pos[0]+1 > len(rows) - 1) or (sym == '<' and pos[1]-1 < 0) or (sym == '>' and pos[1]+1 > len(rows[0]) - 1):
                rows[pos[0]][pos[1]] = "X"
                break
            match sym:
                case '^':
                    ahead = rows[pos[0] - 1][pos[1]]
                    if ahead == "#":
                        current_coll = [sym, pos[0], pos[1]]
                        if current_coll in collisions:
                            broke_bcs_repeat = True
                            break
                        collisions.append(current_coll)
                        sym = states[(states.index(sym) + 1) % 4]
                    else:
                        rows[pos[0]][pos[1]] = "X"
                        pos[0] -= 1
                case '>':
                    ahead = rows[pos[0]][pos[1] + 1]
                    if ahead == "#":
                        current_coll = [sym, pos[0], pos[1]]
                        if current_coll in collisions:
                            broke_bcs_repeat = True
                            break
                        collisions.append(current_coll)
                        sym = states[(states.index(sym) + 1) % 4]
                    else:
                        rows[pos[0]][pos[1]] = "X"
                        pos[1] += 1
                case 'v':
                    ahead = rows[pos[0] + 1][pos[1]]
                    if ahead == "#":
                        current_coll = [sym, pos[0], pos[1]]
                        if current_coll in collisions:
                            broke_bcs_repeat = True
                            break
                        collisions.append(current_coll)
                        sym = states[(states.index(sym) + 1) % 4]
                    else:
                        rows[pos[0]][pos[1]] = "X"
                        pos[0] += 1
                case '<':
                    ahead = rows[pos[0]][pos[1] - 1]
                    if ahead == "#":
                        current_coll = [sym, pos[0], pos[1]]
                        if current_coll in collisions:
                            broke_bcs_repeat = True
                            break
                        collisions.append(current_coll)
                        sym = states[(states.index(sym) + 1) % 4]
                    else:
                        rows[pos[0]][pos[1]] = "X"
                        pos[1] -= 1
        loop_bricks += broke_bcs_repeat
print(loop_bricks)
