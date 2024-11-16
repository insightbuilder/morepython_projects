import sys

a = [0] * 3
y = [0, 0, 0]
c = [0 for i in range(3)]

print(sys.getsizeof(a))
print(sys.getsizeof(y))
print(sys.getsizeof(c))
