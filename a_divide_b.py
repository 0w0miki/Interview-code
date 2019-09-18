a, b = map(int, input().strip().split())
integer = a//b
if integer*b == a:
    print(integer)
else:
    print(str(integer)+'.', end = '')
    exist = {}
    integer = (a - integer * b) * 10
    factorial, index = '', 0
    while integer != 0:
        if integer in exist:
            # cycle
            factorial = factorial[:exist[integer]]+'('+factorial[exist[integer]:]
            factorial += ')'
            print(factorial)
            break
        factorial += str(integer // b)
        exist[integer] = index
        integer = (integer - integer // b * b) * 10
        index += 1
    else:
        print(factorial)