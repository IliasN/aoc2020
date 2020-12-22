import copy
import math

class Image:
    def __init__(self, ident: str, pixels: list, modif:str = ""):
        self.ident = ident
        self.pixels = pixels
        self.width = len(pixels[0])
        self.height = len(pixels)
        self.ntop = None
        self.nbot = None
        self.nright = None
        self.nleft = None
        self.modif = modif

    def print(self) -> None:
        print(f"ID : {self.ident}\nMODIFS : {self.modif}")
        for x in self.pixels:
            print(x)

    def get_right(self) -> list:
        arr = list()
        for i in range(self.height):
            arr.append(self.pixels[i][self.width - 1])
        return arr

    def get_left(self) -> list:
        arr = list()
        for i in range(self.height):
            arr.append(self.pixels[i][0])
        return arr
    
    def get_top(self) -> list:
        arr = list()
        for i in range(self.width):
            arr.append(self.pixels[0][i])
        return arr

    def get_bot(self) -> list:
        arr = list()
        for i in range(self.width):
            arr.append(self.pixels[self.height - 1][i])
        return arr
    
    def flip_horizontal(self):
        newpix = copy.deepcopy(self.pixels)
        for j in range(self.height):
            for i in range(self.width // 2):
                newpix[j][i] = self.pixels[j][self.width - 1 - i]
                newpix[j][self.width - 1 - i] = self.pixels[j][i]
        return Image(self.ident, newpix, self.modif + " Flipped horizontal")


    def flip_vertical(self):
        newpix = copy.deepcopy(self.pixels)
        for j in range(self.height // 2):
            for i in range(self.width):
                newpix[j][i] = self.pixels[self.height - 1 - j][i]
                newpix[self.height - 1 - j][i] = self.pixels[j][i]
        return Image(self.ident, newpix, self.modif + " Flipped horizontal")

    def rotate(self):
        newpix = copy.deepcopy(self.pixels)
        for j in range(self.height):
            for i in range(self.width):
                newpix[j][i] = self.pixels[self.width - i - 1][j]
        return Image(self.ident, newpix, self.modif + " Rotated")

    def get_sides(self) -> list:
        return [self.get_left(), self.get_right(), self.get_top(), self.get_bot()]

def parse(filename: str) -> list:
    with open(filename, "r") as f:
        data = f.read()
    tiles = data.split("\n\n")
    imglist = list()
    for tile in tiles:
        tile=tile.split("\n")
        ident = int(tile[0].split()[1].replace(":", ""))
        pixels = [ [ 1 if y == "#" else 0 for y in x ] for x in tile[1:] if x != "" ]
        img = Image(ident, pixels)
        imglist.append(img)
    return imglist

def get_match(src, side, imglist):
    for img in imglist:
        if img.ident == src.ident:
            continue
        if side in img.get_sides() or side[::-1] in img.get_sides():
            return img
    return None

def rotate(arr):
    newpix = copy.deepcopy(arr)
    for j in range(len(arr)):
        for i in range(len(arr)):
            newpix[j][i] = arr[len(arr) - i - 1][j]
    return newpix

result = 1
imglist = parse("data")
for img in imglist:
    sides = list()
    for im in imglist:
        if im != img:
            for side in im.get_sides():
                sides.append(side)
    count = 0
    for side in img.get_sides():
        if side[::-1] in sides or side in sides:
            count += 1
    if count == 2:
        result *= img.ident
        print(img.ident)
        corner = img
print(f"Part 1 : {result}")
full_size = int(math.sqrt(len(imglist)))
full_img = [ [None for x in range(full_size) ] for y in range(full_size) ]
while get_match(corner, corner.get_bot(), imglist) == None and get_match(corner, corner.get_right(), imglist) == None:
    corner = corner.rotate()
full_img[0][0] = corner
for j in range(full_size):
    for i in range(full_size):
        if i == 0 and j == 0:
            continue
        if i == 0:
            above = full_img[j - 1][0]
            candid = get_match(above, above.get_bot(), imglist)
            while candid.get_top() != above.get_bot() and candid.get_top()[::-1] != above.get_bot():
                candid = candid.rotate()
            if candid.get_top() != above.get_bot():
                candid = candid.flip_horizontal()
            full_img[j][i] = candid
        else:
            above = full_img[j][i - 1]
            candid = get_match(above, above.get_right(), imglist)
            while candid.get_left() != above.get_right() and candid.get_left()[::-1] != above.get_right():
                candid = candid.rotate()
            if candid.get_left() != above.get_right():
                candid = candid.flip_vertical()
            full_img[j][i] = candid

part_size = corner.width - 2
all_pix_n = part_size * full_size
all_pix = [ [0 for x in range(all_pix_n) ] for y in range(all_pix_n) ]
for j in range(full_size):
    for i in range(full_size):
        for y in range(part_size):
            for x in range(part_size):
                all_pix[j * part_size + y][i * part_size + x] = full_img[j][i].pixels[1+y][1+x]
d = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]


for _ in range(3): # bruteforce final rotation
    all_pix = rotate(all_pix)

total = 0
count = 0
for j in range(all_pix_n):
    for i in range(all_pix_n):
        if all_pix[j][i] == 1:
            total += 1
        valid = True
        for dj in range(3):
            for di in range(len(d[0])):
                if j + dj < all_pix_n and i + di < all_pix_n:
                    if d[dj][di] == "#" and all_pix[j + dj][i + di] != 1:
                        valid = False
                else:
                    valid = False
        if valid:
            count += 1
print(f"Part 2 : {count} monsters water roughness {total - 15 * count}")
