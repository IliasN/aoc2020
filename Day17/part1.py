def parse(filename: str) -> list:
    with open(filename, "r") as f:
        grid = [ list(line.replace("\n", "")) for line in f ]
    return grid

def solve1(grid: list, limit: int) -> int:
    space = generate_space(grid, limit)
    height = len(space)
    width = len(space[0])
    depth = len(space[0][0])
    for _ in range(limit):
        space = round1(space, height, width, depth)
    return count_active(space, height, width, depth)

def count_active(space: list, h: int, w: int, d: int) -> int:
    count = 0
    for j in range(h):
        for i in range(w):
            for k in range(d):
                if space[j][i][k] == "#":
                    count += 1
    return count

def round1(space: list, h: int, w: int, d: int) -> list:
    return_space = [[["." for z in range(d)] for x in range(w)] for y in range(h)]
    for j in range(h):
        for i in range(w):
            for k in range(d):
                count = count_neighbors(space, j, i, k, h, w, d)
                if space[j][i][k] == "#" and not (count == 2 or count == 3):
                    return_space[j][i][k] = "."
                elif space[j][i][k] == "." and count == 3:
                    return_space[j][i][k] = "#"
                else:
                    return_space[j][i][k] = space[j][i][k]
    return return_space


def count_neighbors(space: list, j: int, i: int, k: int, h: int, w: int, d: int) -> int:
    count = 0
    for ja in (-1, 0, 1):
        for ia in (-1, 0, 1):
            for da in (-1, 0, 1):
                if 0 <= (j + ja) < h and 0 <= (i + ia) < w and 0 <= (k + da) < d:
                    if ia == 0 and ja == 0 and da == 0:
                        continue
                    if space[j + ja][i + ia][k + da] == "#":
                        count += 1
    return count


def generate_space(grid: list, limit: int) -> list:
    width = len(grid[0]) + 2 * limit
    height = len(grid) + 2 * limit
    depth = 1 + 2 * limit
    space = [[["." for z in range(depth)] for x in range(width)] for y in range(height)]
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            space[j + limit][i + limit][limit] = grid[j][i]
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

