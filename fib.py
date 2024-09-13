def fib(n):
    if n<=1:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
nterms=int(input("range"))
print("fibn series")
for i in range (nterms):
    print(fib(i))
