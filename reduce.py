from functools import reduce
def sum(a,b):
    return a+b
def prod(a,b):
    return a*b
lst = [1,2,3,4,5]
s = reduce(sum,lst) 
p = reduce(prod,lst)
print(lst,s,p)
