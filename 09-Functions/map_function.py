import math
def func1(n):
    return n*n
lst=[5,10,15,20]
m1=map(math.radians,lst)
m2=map(math.factorial,lst)
m3=map(func1,lst)
print(set(m1))
print(list(m2))
print(list(m3))
