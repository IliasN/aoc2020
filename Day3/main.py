lines = []
with open("data", "r") as f:
    line = f.readline()
    while line:
        lines.append(line)
        line = f.readline()
WIDTH = len(lines[0]) - 1 # Attention aux newlines
HEIGHT = len(lines)


def trees_from_slope(right, down):
    x = 0
    count = 0
    for y in range(0, HEIGHT, down):
        c = lines[y][x]
        if c == "#":
            count += 1
        x = (x + right) % WIDTH
    return count

# PARTIE 1
print(f"Part one : {trees_from_slope(3,1)}")
# PARTIE 2
result = 1
result *= trees_from_slope(1,1)
result *= trees_from_slope(3,1)
result *= trees_from_slope(5,1)
result *= trees_from_slope(7,1)
result *= trees_from_slope(1,2)
print(f"Part two : {result}")
