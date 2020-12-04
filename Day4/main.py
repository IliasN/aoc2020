import re

with open("data", "r") as f:
    lines = [line for line in f]

# Récupère les données dans des dictionnaires
passeports = []
current_passport = dict()
for line in lines:
    if len(line) == 1:
        passeports.append(current_passport)
        current_passport = dict()
        continue
    line = line.replace("\n", "")
    datas = line.split(" ")
    for champ in datas:
        key = champ.split(":")[0]
        value = champ.split(":")[1]
        current_passport[key] = value
if current_passport and current_passport != passeports[-1]:
    passeports.append(current_passport)

# Définirions de fonctions de validations de champs
def check_height(s):
    if "in" in s:
        return len(s) == 4 and s[0:2].isnumeric() and int(s[0:2]) >= 59 and int(s[0:1]) <= 76
    elif "cm" in s:
        return len(s) == 5 and s[0:3].isnumeric() and int(s[0:3]) >= 150 and int(s[0:1]) <= 193
    else:
        return False

def check_year(s, mini, maxi):
    return len(s) == 4 and s.isnumeric() and int(s) <= maxi and int(s) >= mini

def check_pid(s):
    return len(s) == 9 and s.isnumeric()

def check_eye_color(s):
    return s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def check_hair_color(s):
    return len(s) == 7 and s[0] == "#" and re.match(r"#[0-9a-f]{6}",s) != None

def check_pass(p):
    if "byr" in p and "iyr" in p and "eyr" in p and "hgt" in p and "hcl" in p and "ecl" in p and "pid" in p:
        return check_year(p["byr"], 1920, 2002) and check_year(p["iyr"], 2010, 2020) and check_year(p["eyr"], 2020, 2030) and check_height(p["hgt"]) and check_hair_color(p["hcl"]) and check_eye_color(p["ecl"]) and check_pid(p["pid"])
    else:
        return False

# Compte
count = 0
count_full = 0
for p in passeports:
    if "byr" in p and "iyr" in p and "eyr" in p and "hgt" in p and "hcl" in p and "ecl" in p and "pid" in p:
        count += 1
    if check_pass(p):
        count_full += 1
# Part 1
print(count)
# Part 2
print(count_full)
