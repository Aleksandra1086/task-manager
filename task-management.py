print("Example 1:")
import copy

a = [[1, 2, 3], [4, 5, 6]]
b = copy.copy(a)
c = a[:]
d = copy.deepcopy(a)

b[1][0] = 10
c[1][1] = 11
d[1][2] = 12

print("List a:")
print(a)
print("List b:")
print(b)
print("List c:")
print(c)
print("List d:")
print(d)

