# range 제네레이터

import sys


a = [n for n in range(100000)]

b = range(100000)

print(a)
print(b)

print(len(a) == len(b))

print(sys.getsizeof(a))
print(sys.getsizeof(b))

print(b[999])
