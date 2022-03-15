a = [1, 2, 3, 4, 2, 45, 2, 5]

print(enumerate(a))
print(list(enumerate(a)))

for index, value in enumerate(a):
    print(index, value)
