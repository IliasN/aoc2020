def parse(filename):
    with open(filename, "r") as f:
        lines = [ line.replace("\n", "") for line in f if line != "\n" ]
    ids = [ x for x in lines[1].split(",")]
    return (int(lines[0]), ids)

def solve1(start, ids):
    counter = start
    while True:
        gen = ( int(x) for x in ids if x != "x")
        for i in gen:
            if counter % i == 0:
                return i * (counter - start)
        counter += 1

def get_values_remainder(arr):
    data = []
    for i,x in enumerate(arr):
        if x == "x":
            continue
        val = int(x)
        data.append((val, val - i))
    return data

def chinese_remainder(ids):
    data = get_values_remainder(ids)
    result = 0
    n = 1
    for value, remainder in data:
        n *= value
    for value, remainder in data:
        prod = n // value
        mod_n = mod_inv(prod, value)
        result += prod * remainder * mod_n
    return result % n

def mod_inv(a, m):
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return 1



depart, ids = parse("data")
res1 = solve1(depart, ids)
print("Part 1 :")
print(res1)


res2 = chinese_remainder(ids)
print("Part 2 :")
print(res2)
