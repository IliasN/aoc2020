n1 = 12232269

n2 = 19452773

mod = 20201227


def euc(a, b):
    if a == 0 :
        return b,0,1
    gcd,x1,y1 = euc(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd,x % b,y % b

i = 1
while pow(7, i, mod) != n2:
    i += 1

print(f"Part 1 : {pow(n1, i, mod)}")
