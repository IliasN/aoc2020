def parse(filename: str) -> list:
    with open(filename, "r") as f:
        grid = [ list(line.replace("\n", "")) for line in f ]
    return grid

def solve1(grid: list, limit: int) -> int:
    space = generate_space(grid, limit)
    height = len(space)
    width = len(space[0])
    depth = len(space[0][0])
    zdepth = len(space[0][0][0])
    for _ in range(limit):
        space = round1(space, height, width, depth, zdepth)
    return count_active(space, height, width, depth, zdepth)

def count_active(space: list, h: int, w: int, d: int, z: int) -> int:
    count = 0
    for j in range(h):
        for i in range(w):
            for k in range(d):
                for l in range(z):
                    if space[j][i][k][l]== "#":
                        count += 1
    return count

def round1(space: list, h: int, w: int, d: int, z: int) -> list:
    return_space = [[[["." for _ in range(z)] for _ in range(d)] for _ in range(w)] for _ in range(h)]
    for j in range(h):
        for i in range(w):
            for k in range(d):
                for l in range(z):
                    count = count_neighbors(space, j, i, k, l, h, w, d, z)
                    if space[j][i][k][l] == "#" and not (count == 2 or count == 3):
                        return_space[j][i][k][l] = "."
                    elif space[j][i][k][l] == "." and count == 3:
                        return_space[j][i][k][l] = "#"
                    else:
                        return_space[j][i][k][l] = space[j][i][k][l]
    return return_space


def count_neighbors(space: list, j: int, i: int, k: int, l: int, h: int, w: int, d: int, z: int) -> int:
    count = 0
    for ja in (-1, 0, 1):
        for ia in (-1, 0, 1):
            for da in (-1, 0, 1):
                for la in (-1, 0, 1):
                    if 0 <= (j + ja) < h and 0 <= (i + ia) < w and 0 <= (k + da) < d and 0 <= (l + la) < z:
                        if ia == 0 and ja == 0 and da == 0 and la == 0:
                            continue
                        if space[j + ja][i + ia][k + da][l + la] == "#":
                            count += 1
    return count


def generate_space(grid: list, limit: int) -> list:
    width = len(grid[0]) + 2 * limit
    height = len(grid) + 2 * limit
    depth = 1 + 2 * limit
    space = [[[["." for _ in range(depth)] for z in range(depth)] for x in range(width)] for y in range(height)]
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            space[j + limit][i + limit][limit][limit] = grid[j][i]
    return space

def print_space(space: list) -> None:
    for z in range(len(space[0][0])):
        print(f"Depth : {z}")
        for j in range(len(space)):
            for i in range(len(space[0])):
                print(space[j][i][z], end="")
            print()
        print()

 
start_grid = parse("data")
res1 = solve1(start_grid, 6)
print(res1)

