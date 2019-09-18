import sys
cards = sys.stdin.readline()
cards = None
cards = cards.lower()
if len(cards) == 1:
    print(cards)
res = 129
for c in cards:
    if c.isalpha():
        c_index = ord(c)
        if c_index < res:
            res = c_index
if ord('a')<=res<=ord('z'):
    print(chr(res))
else:
    print('')
# return str(c)