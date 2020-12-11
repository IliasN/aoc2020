def parse(filename):
    with open(filename, "r") as f:
        lines = [line.replace("\n", "") for line in f if line != "\n" ]
    return lines

class day11:
    def __init__(self, w, h, data):
        self.arr = [[0 for _ in range(w)] for __ in range(h)]
        self.width = w
        self.height = h
        for y in range(self.height):
            for x in range(self.width):
                self.arr[y][x] = data[y][x]

    def get_occupied_close(self, x, y):
        occupied = 0
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i == 0 and j == 0:
                    continue
                if y + i >= 0 and x + j >= 0 and y + i < self.height and x + j < self.width:
                    if self.arr[y+i][x+j] == "#":
                        occupied += 1
        return occupied

    def get_occupied_far(self, x, y):
        occupied = 0
        for i in (-1, 0, 1):
            di = i
            for j in (-1, 0, 1):
                dj = j
                i = di
                if i == 0 and j == 0:
                    continue
                while y + i >= 0 and x + j >= 0 and y + i < self.height and x + j < self.width and self.arr[y+i][x+j] == ".":
                    i += di
                    j += dj
                if y + i >= 0 and x + j >= 0 and y + i < self.height and x + j < self.width:
                    if self.arr[y+i][x+j] == "#":
                        occupied += 1
        return occupied

    def round(self, occupied_func, n_to_leave):
        new_arr = [[0 for _ in range(self.width)] for __ in range(self.height)]
        changed = 0
        for y in range(self.height):
            for x in range(self.width):
                occupied = occupied_func(x, y)
                if self.arr[y][x] == "L" and occupied == 0:
                    new_arr[y][x] = "#"
                    changed += 1
                elif self.arr[y][x] == "#" and occupied >= n_to_leave:
                    new_arr[y][x] = "L"
                    changed += 1
                else:
                    new_arr[y][x] = self.arr[y][x]
        self.arr = new_arr
        return changed

    def stabilize(self, func, n_to_leave):
        res = self.round(func, n_to_leave)
        while res != 0:
            res = self.round(func, n_to_leave)

    def count(self):
        occupied = 0
        free = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.arr[y][x] == "#":
                    occupied += 1
                if self.arr[y][x] == "L":
                    free += 1
        return (occupied, free)


# Init
data = parse("data")
height = len(data)
width = len(data[0])
print("Dimensions :", width, height)

# Part 1
room = day11(width, height, data)
room.stabilize(room.get_occupied_close, 4)
occup, free = room.count()
print("Part 1 :")
print(occup)

# Part 2
room = day11(width, height, data)
room.stabilize(room.get_occupied_far, 5)
occup, free = room.count()
print("Part 2 :")
print(occup)

