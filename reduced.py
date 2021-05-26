import sys

def hasSpecial(word):
    specials = "`~!@#$%^&*()_-=+|]}[{':;/?>.<,"
    for c in word:
        if c in specials:
            return True
    return False
def hasNumber(word):
    numbers = "0123456789"
    for c in word:
        if c in numbers:
            return True
    return False
try:
    with open(sys.argv[1], 'r') as pwords:
        with open("reduced.txt", 'w') as red:
            for p in pwords:
                if len(p)>=8 and hasSpecial(p) and hasNumber(p):
                    red.write(p)
except IndexError:
    print("no file given")

