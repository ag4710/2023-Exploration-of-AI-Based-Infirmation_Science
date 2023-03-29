a = [-9, 77, 100]
b = a[:] # copy
c = list(a) # copy
d = a.copy() # copy
print(id(a), id(b))
b[1] = 16
c[1] = 0
d[1] = 55
print(a, b, c, d)
