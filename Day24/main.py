def parse(filename):
    with open(filename, "r") as f:
        lines = [line.replace("\n", "") for line in f if line != ""]
    return lines


opp = {
        "e": (1, 0),
        "se": (0.5, -0.5),
        "sw": (-0.5, -0.5),
        "w": (-1, 0),
        "nw": (-0.5, 0.5),
        "ne": (0.5, 0.5)
        }


def line_to_arr(line):
    j = 0
    arr = list()
    while len(line) > 0:
        if line[:j] in opp:
            arr.append(line[:j])
            line = line[j:]
            j = 0
        else:
            j += 1
    return arr


def arr_to_coord(arr):
    ref = [0, 0]
    for key in arr:
        point = opp[key]
        ref[0] += point[0]
        ref[1] += point[1]
    return tuple(ref)


def generate_floor(n):
    floor = dict()
    for x in range(2*n):
        for y in range(2*n):
            floor[(x/2, y/2)] = False
    return floor


def solve1(lines, floor, center):
    for line in lines:
        line_arr = line_to_arr(line)
        key = arr_to_coord(line_arr)
        key = (key[0] + center, key[1] + center)
        if key in floor:
            floor[key] = not floor[key]
        else:
            floor[key] = True
    count = 0
    for key in floor:
        if floor[key]:
            count += 1
    return count


def solve2(floor, n):
    for _ in range(n):
        floor = day(floor)
    count = 0
    for key in floor:
        if floor[key]:
            count += 1
    return count


def day(floor):
    new_floor = floor.copy()
    for key in floor:
        count = 0
        for diff in opp:
            newkey = (key[0] + opp[diff][0], key[1] + opp[diff][1])
            if newkey in floor:
                if floor[newkey]:
                    count += 1
        if floor[key] and (count == 0 or count > 2):
            new_floor[key] = False
        elif not floor[key] and count == 2:
            new_floor[key] = True
        else:
            new_floor[key] = floor[key]
    return new_floor


n = 200
floor = generate_floor(n)
lines = parse("data")
res1 = solve1(lines, floor, n // 2)
print(res1)

res2 = solve2(floor, 100)
print(res2)
