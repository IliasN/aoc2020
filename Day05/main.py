with open("data", "r") as f:
    lines = [line.replace("\n", "") for line in f]

conv = lambda x : int(x.replace("F","0").replace("B","1").replace("R", "1").replace("L","0"),2)

print("Part 1 :")
ids = sorted([conv(seat) for seat in lines])
part1 = ids[-1]
print(part1)

# Part 2 
print("Part 2 :")
for i,v in enumerate(ids[0:-1]):
    if ids[i + 1] - v > 1:
        print(v + 1)
        exit()
