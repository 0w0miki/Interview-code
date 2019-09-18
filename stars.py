n = int(input())
stars = {}
for i in range(n):
    s = input().split(' ')
    x = int(s[0])
    y = int(s[1])
    if x in stars:
        stars[x].append(y)
    else:
        stars[x] = [y]
for key in stars:
    sorted(stars[x])
m = int(input())
questions = []
for i in range(m):
    s = input().split(' ')
    questions.append(list(map(int,s)))
for question in questions:
    x1 = question[0]
    y1 = question[1]
    x2 = question[2]
    y2 = question[3]
    
