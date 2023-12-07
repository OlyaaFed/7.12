def fx(x, y):
    if x > 0:
        f = x + 1
        return f
    elif x <= 0:
        f = x * y -1
        return f

u = int(input())
v = int(input())
x1 = u + v
y1 = u - v
y2 = u * v
z1 = fx(x1, y1)
z2 = fx(u, y2)
z = z1 - z2
print(z)