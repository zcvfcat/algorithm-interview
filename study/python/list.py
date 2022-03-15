a = [1, 2, 3, 5, 4]
a.append('안녕')
a.append(True)

print(a)
print(a[3])
print(a[1:3])
print(a[:3])
print(a[4:])
print(a[1:4])
print(a[1:4:2])

try:
    print(a[9])
except IndexError:
    print('존재하지 않는 인덱스')

del a[1]

a.remove(3)

a.pop(3)
