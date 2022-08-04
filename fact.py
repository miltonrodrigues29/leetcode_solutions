n = 4

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
res = fact(n)    
print(res)


