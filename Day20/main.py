import copy
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

result = 1
imglist = parse("data")
print(len(imglist))
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
print(f"Part 1 : {result}")
