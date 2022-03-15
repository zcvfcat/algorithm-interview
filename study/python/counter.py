import collections


a = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 4, 1, 23, 4, 2]

b = collections.Counter(a)

print(b)

print(b.most_common(3))
