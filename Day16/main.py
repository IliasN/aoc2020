def parse(filename: str) -> tuple:
    with open(filename, "r") as f:
        text = f.read()
    rules = text.split("your ticket:")[0]
    rules = { line.split(":")[0].strip() : (line.split(":")[1].split("or")[0].strip(), line.split(":")[1].split("or")[1].strip()) for line in rules.split("\n") if line != "\n" and line != ""}
    remainder = text.split("your ticket:")[1]
    my_ticket = [ int(x) for x in remainder.split("nearby tickets:")[0].strip().split(",") ]
    tickets = [ list(map(int, t.strip().split(","))) for t in remainder.split("nearby tickets:")[1].split("\n") if t != ""]
    return (rules, my_ticket, tickets)

def solve1(tickets: list, rules: dict) -> int:
    rate = 0
    for ticket in tickets:
        for n in ticket:
            rate += check_n(n, rules)
    return rate

def check_n(n: int, rules: dict) -> int:
    for key in rules:
        rule1 = tuple(map(int, rules[key][0].split("-")))
        rule2 = tuple(map(int, rules[key][1].split("-")))
        if rule1[0] <= n <= rule1[1] or rule2[0] <= n <= rule2[1]:
            # BIG MISTAKE RIGHT HERE BECAUSE OF THE UNIQUE 0 IN THE WHOLE LIST OF TICKETS -> 2-3 HOURS OF DEBUGGING
            return 0
    return n

def get_faulty(n: int, rules: dict) -> list:
    faultys = []
    for key in rules:
        rule1 = tuple(map(int, rules[key][0].split("-")))
        rule2 = tuple(map(int, rules[key][1].split("-")))
        if rule1[0] <= n <= rule1[1] or rule2[0] <= n <= rule2[1]:
            continue
            print("True")
        else:
            faultys.append(key)
    return faultys

def solve2(tickets: list, rules: dict) -> list:
    valids = list()
    for ticket in tickets:
        valid = True
        for n in ticket:
            check = check_n(n, rules)
            if check or n == 0:
                valid = False
        if valid:
            valids.append(ticket)
    possible = [0] * len(tickets[0])
    for i in range(len(possible)):
        possible[i] = list()
        for key in rules:
            possible[i].append(key)
    for ticket in valids:
        for i, n in enumerate(ticket):
            faultys = get_faulty(n, rules)
            if len(faultys) > 0:
                if i == 15:
                    if n == 0:
                        print(ticket)
                for f in faultys:
                    if f in possible[i]:
                        possible[i].remove(f)
    return possible

def reduce_fields(fields: list) -> list:
    while sum(len(x) for x in fields) != len(fields):
        for f in fields:
            if len(f) == 1:
                todel = f[0]
                for fd in fields:
                    if len(fd) > 1 and todel in fd:
                        fd.remove(todel)
    return fields

def compute_res2(fields: list, ticket: list) -> int:
    res = 1
    for i, n in enumerate(ticket):
        if "departure" in fields[i][0]:
            res *= n
    return res

rules, my_ticket, tickets = parse("data")
res1 = solve1(tickets, rules)
print(res1)

remain = solve2(tickets, rules)
final = reduce_fields(remain)
res2 = compute_res2(final, my_ticket)
print(res2)
