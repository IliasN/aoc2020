import time

inp = [1,0,16,5,17,4]

def solve_up(arr: list, limit: int) -> int:
    last_seen = dict()
    for i in range(limit - 1):
        if len(arr) - 1 == i:
            if arr[i] in last_seen:
                arr.append(i - last_seen[arr[i]])
            else:
                arr.append(0)
        last_seen[arr[i]] = i
    return arr[-1]

def solve1(arr: list, limit: int) -> int:
    seen = set()
    last_seen = dict()
    for i,x in enumerate(arr[:-1]):
        last_seen[x] = i
        seen.add(x)
    while len(arr) < limit:
        if arr[-1] in seen:
            new = len(arr) - last_seen[arr[-1]] - 1
            arr.append(new)
        else:
            arr.append(0)
        seen.add(arr[-2])
        last_seen[arr[-2]] = len(arr) - 2
    return arr[-1]

def index_from_end(arr: list, value : int) -> int:
    return arr[::-1].index(value) + 1



start = time.time()
res1 = solve1(inp.copy(), 30000000)
end = time.time()

print(f"Solution 1 : {end-start}s")

start = time.time()
res2 = solve_up(inp.copy(), 30000000)
end = time.time()

print(f"Solution 2 : {end-start}s")

assert res1 == 573522
assert res2 == 573522
