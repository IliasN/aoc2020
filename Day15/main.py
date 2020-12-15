inp = [1,0,16,5,17,4]

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


res1 = solve1(inp.copy(), 2020)
print(res1)

res2 = solve1(inp.copy(), 30000000)
print(res2)
