a = input()
b = input()
c = int(input())

for i in range(c):
    if i == c // 2:
        print(b * c)
    else:
        print(a + b * (c - 2) + a)