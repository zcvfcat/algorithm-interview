e = [n * 2 for n in range(1, 50) if n % 2 == 1]
print(e)

t = [
    (x, y, z)
    for x in range(5)
    for y in range(5)
    if x != y
    for z in range(5)
    if y != z
]

print(t)
