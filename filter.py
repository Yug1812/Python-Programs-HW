def divby5(n):
    return True if n%5==0 else False
lst1=["a","A","P","q","4","7","+","r","E","Z"]
f1=filter(str.isalpha,lst1)
print(list(f1))
lst2=[5,45,.23,45,855,93,69,11,10]
f2=filter(divby5,lst2)
print(list(f2))
