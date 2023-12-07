def f_x(f, p):
    a1 = p
    b1 = f/2
    a2 = (p + f)/2
    b2 = f
    g1 = (3 * (a1 * a1)) + (7 * b1)
    g2 = (3 * (a2 * a2)) + (7 * b2)
    g = g1 - g2
    return g
f, p = int(input()), int(input())
j = f_x(f, p)
print(j)