rev=0
a=12345
while(a>0):
    rem=int(a%10)
    rev=rev*10+rem
    a=int(a/10)
print(rev)
