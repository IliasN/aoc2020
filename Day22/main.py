def parse(filename):
    with open(filename, "r") as f:
        data = f.read()
    players_data = data.split("\n\n")
    p1 = [int(x) for x in players_data[0].split("\n")[1:] if x != ""]
    p2 = [int(x) for x in players_data[1].split("\n")[1:] if x != ""]
    return p1, p2

def play(p1, p2):
    while len(p1) != 0 and len(p2) != 0:
        c1 = p1[0]
        p1.remove(c1)
        c2 = p2[0]
        p2.remove(c2)
        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    if len(p1) == 0:
        return get_score(p2)
    else:
        return get_score(p1)

def get_score(deck):
    return sum( (i+1) * x for i, x in enumerate(deck[::-1]) )

def recursive_game(p1, p2):
    history = list()
    while len(p1) != 0 and len(p2) != 0:
        if (p1, p2) in history:
            return 1, p1, p2
        history.append((p1.copy(), p2.copy()))
        c1 = p1[0]
        p1.remove(c1)
        c2 = p2[0]
        p2.remove(c2)
        if len(p1) >= c1 and len(p2) >= c2:
            res, _, __ = recursive_game(p1[:c1], p2[:c2])
            if res == 1:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        else:
            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
    if len(p1) == 0:
        return 2, p1, p2
    else:
        return 1, p1, p2
    

p1, p2 = parse("data")
res1 = play(p1.copy(), p2.copy())
print(res1)
res, p1, p2 = recursive_game(p1,p2)
if res == 1:
    print(get_score(p1))
else:
    print(get_score(p2))
