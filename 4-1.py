a = input()
c = int(input())

for i in range(c):
    if i == 0 or i == c - 1:
        print(a * c)
    else:
        print(a + " " * (c - 2) + a)