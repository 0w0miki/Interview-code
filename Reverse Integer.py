# Reverse Integer
# Given a 32-bit signed integer, reverse digits of an integer.
# Input: 123 Output: 321
# Input: -123 Output: -321
x = -1563847412
print(int(str(abs(x))[::-1]))
y = 0
flag = 0
if x < 0:
    x = -x
    flag = 1
while x != 0:
    y = 10 * y + x%10
    x = int(x/10)
y *= (-1) ** flag
print(y)
if y>0xffffffff>>1 or y<-0xffffffff>>1:
    y = 0
print(y)
