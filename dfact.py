def fact(i):
    if i==1:
        return 1
    else:
        return((i*fact(ni-1))
n=int(input("enter number"))
print("the fact of num is",n, "==",fact(n))
